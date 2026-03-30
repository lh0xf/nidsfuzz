import pathlib
import re
from collections import defaultdict
from typing import Generator

from logger import logger
from sanitization import AlertMonitor, test_oracle


class FuzzerLogReader:

    Selection_Pattern = r'Selection phase finished: (?P<proto>[a-z]+) >>> \[(?P<selected_rules>.*?)]'
    Injection_Pattern = r'Connecting to responder with address: (?P<ip>\d+\.\d+\.\d+\.\d+):(?P<allocated_port>\d+)'

    def __init__(self, log_path: str):
        self.log_path = pathlib.Path(log_path)

        self.selected_rules: list[list[str]] = []
        self.allocated_ports: list[int] = []

        ###### State variables #####
        self.match_flags = {
            'selection': 0,
            'injection': 0,
        }

        self.match_content = {
            'selection': None,
            'injection': None,
        }

    def reset_state(self):
        self.match_flags = {
            'selection': 0,
            'injection': 0,
        }

        self.match_content = {
            'selection': None,
            'injection': None,
        }

    @property
    def name(self):
        return self.log_path.name

    def read(self):
        selection_pattern = re.compile(self.Selection_Pattern)
        injection_pattern = re.compile(self.Injection_Pattern)

        with open(self.log_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                match = re.search(selection_pattern, line)
                if match:
                    proto = match.group("proto")
                    selected_rules = [r.strip("'") for r in match.group("selected_rules").split(',')]
                    self.match_flags['selection'] += 1
                    self.match_content['selection'] = selected_rules
                    # print(f'{proto}: {selected_rules}')
                    continue

                match = re.search(injection_pattern, line)
                if match:
                    ip = match.group("ip")
                    allocated_port = int(match.group("allocated_port"))
                    self.match_flags['injection'] += 1
                    self.match_content['injection'] = allocated_port
                    # print(f'{ip}: {allocated_port}')
                    continue

                if self.match_flags['selection'] == 1 and self.match_flags['injection'] == 1:
                    self.selected_rules.append(self.match_content['selection'])
                    self.allocated_ports.append(self.match_content['injection'])

                    self.reset_state()
                elif self.match_flags['selection'] > 1 or self.match_flags['injection'] > 1:
                    self.reset_state()

        assert len(self.selected_rules) == len(self.allocated_ports)
        print(f'{self.name}: found {len(self.selected_rules)} cases.')

    def iterator(self) -> Generator[tuple[list[str], int], None, None]:
        for rule, port in zip(self.selected_rules, self.allocated_ports):
            yield rule, port


class NIDSLogReader:

    Alert_Pattern = AlertMonitor.ALERT_PATTERN

    def __init__(self, log_path: str):
        self.log_path = pathlib.Path(log_path)

        self.triggered_rules: list[str] = []
        self.monitored_ports: list[int] = []

    @property
    def name(self):
        return self.log_path.name

    def read(self, client_ip, server_ip):
        alert_pattern = re.compile(self.Alert_Pattern)
        with open(self.log_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()

                match = re.match(alert_pattern, line)
                if match:
                    rule_id, src_ip, src_port, dst_ip, dst_port = match.groups()
                    self.triggered_rules.append(rule_id)
                    monitored_port = src_port if src_ip == client_ip else dst_port
                    self.monitored_ports.append(int(monitored_port))
                    # print(f'{rule_id} --- {monitored_port}')

        assert len(self.triggered_rules) == len(self.monitored_ports)
        print(f'{self.name}: found {len(self.triggered_rules)} alerts.')

    def iterator(self) -> Generator[tuple[str, int], None, None]:
        for rule, port in zip(self.triggered_rules, self.monitored_ports):
            yield rule, port


class OfflineAlertValidator:

    # TODO: The MAX_NUM_OF_FUZZING_ITERATION should match the memory span
    #  of the Port Allocator used in fuzzing process.
    MAX_NUM_OF_FUZZING_ITERATION = 1000

    MOCK_INITIATOR_IP = '172.18.0.10'
    MOCK_RESPONDER_IP = '192.168.0.10'

    OUTPUT = 'offline_validation_results.txt'

    def __init__(self, log_dir: str):
        self.anchor = pathlib.Path(log_dir)
        self.fuzz_logfile = (
                self.anchor / 'initiator' / 'log' / 'fuzzing.log'
        )
        self.nids_logfiles = [
            self.anchor / 'snort3' / 'log' / 'snort3.log',
            self.anchor / 'suricata' / 'log' / 'fast.log',
            self.anchor / 'snort2' / 'log' / 'snort2.log',
        ]

        ################
        self.fuzz_bundle: list[tuple[list[str], int]] = None
        self.nids_bundles: dict[str, list[tuple[str, int]]] = None

        self.aligned_bundle: dict[str, dict[str, str]] = None

    def parse(self):
        reader = FuzzerLogReader(str(self.fuzz_logfile))
        reader.read()
        self.fuzz_bundle = list(reader.iterator())

        if len(self.fuzz_bundle) > self.MAX_NUM_OF_FUZZING_ITERATION:
            raise RuntimeError(f'The number of executed test cases ({len(self.fuzz_bundle)}) '
                               f'has surpassed the allowed memory span ({self.MAX_NUM_OF_FUZZING_ITERATION}).')

        self.nids_bundles = {}
        for log_file in self.nids_logfiles:
            reader = NIDSLogReader(str(log_file))
            reader.read(client_ip=self.MOCK_INITIATOR_IP, server_ip=self.MOCK_RESPONDER_IP)
            self.nids_bundles[reader.name] = list(reader.iterator())

    def align(self, out_dir: str = None):
        if self.fuzz_bundle is None or self.nids_bundles is None:
            raise RuntimeError(f'Please doing parse() before align().')

        def find_matched_rules(nids_bundle: list[tuple[str, int]], used_port: int) -> list[str]:
            result: list[str] = []
            for rule, port in nids_bundle:
                if port == used_port:
                    result.append(rule)
            return result

        self.aligned_bundle: list[tuple[str, dict[str, str]]] = []
        for selected_rules, allocated_port in self.fuzz_bundle:
            all_nids_triggered_rules = {}
            for nids_name, nids_bundle in self.nids_bundles.items():
                triggered_rules = find_matched_rules(nids_bundle, allocated_port)
                all_nids_triggered_rules[nids_name] = ", ".join(triggered_rules)
            self.aligned_bundle.append(
                (", ".join(selected_rules), all_nids_triggered_rules)
            )

        assert len(self.aligned_bundle) == len(self.fuzz_bundle)

        if out_dir is not None:
            out_file = pathlib.Path(out_dir) / self.OUTPUT
            out_file.parent.mkdir(parents=True, exist_ok=True)
            with open(out_file, 'w', encoding='utf-8') as f:
                for selected_rules, all_nids_rules in self.aligned_bundle:
                    print(f'{"seeds:":<15}{selected_rules}', file=f)
                    for nids_name, nids_rules in all_nids_rules.items():
                        print(f'{nids_name + ":":<15}{nids_rules}', file=f)
                    f.write('\n')


    def validate(self):
        if self.fuzz_bundle is None or self.nids_bundles is None:
            raise RuntimeError(f'Please doing parse() before align().')
        if self.aligned_bundle is None:
            raise RuntimeError(f'Please doing align() before validate().')

        oracle_hit_num: dict[str, int] = defaultdict(int)
        for oracle_method in test_oracle.oracle_methods:
            oracle_hit_num[oracle_method.__name__] = 0
            for selected_rules, all_nids_rules in self.aligned_bundle:
                input_rules = selected_rules.split(", ")
                output_rules = []

                for nids_name, nids_rules in all_nids_rules.items():
                    if nids_rules == '':
                        output_rules.append([])
                    else:
                        output_rules.append(nids_rules.split(", "))
                is_passed = oracle_method(input_rules, output_rules)
                if not is_passed:
                    oracle_hit_num[oracle_method.__name__] += 1
                    # print(f'{oracle_method.__name__} triggered: {selected_rules}')
                # else:
                #     print(f'{oracle_method.__name__} passed: {selected_rules}')

        for oracle_name, hit_num in oracle_hit_num.items():
            print(f'The hit probability of {oracle_name} is : {hit_num} / {len(self.fuzz_bundle)} = {hit_num / len(self.fuzz_bundle):.4f}')


    ############################################################################
    ############################################################################

    @staticmethod
    @test_oracle.register
    def render_accuracy_oracle(
            input_rules: list[str],
            output_rules: list[list[str]],
    ) -> bool:
        """
        We assume that a packet derived from seed rules should at least trigger the corresponding rules on
        all NIDS platforms. Missing alerts from a NIDS platform are treated as abnormal.
        """
        for platform_rules in output_rules:
            if set(input_rules).issubset(set(platform_rules)):
                return False
        return True


if __name__ == '__main__':
    logger.remove()

    log_dir = pathlib.Path(__file__).parent.parent / 'benchmark' / 'fuzzing-results'
    offline_alert_validator = OfflineAlertValidator(log_dir=str(log_dir))

    offline_alert_validator.parse()
    offline_alert_validator.align(out_dir=str(log_dir))
    offline_alert_validator.validate()
















