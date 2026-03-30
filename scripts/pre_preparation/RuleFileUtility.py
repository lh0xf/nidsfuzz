import itertools
import pathlib
import re
from collections import defaultdict

from rule import RuleSet


class RuleFileUtility:

    """
    Example Usage:
    >>> snort3_rule_path = pathlib.Path('./snort3-protocol-http.rules')
    >>> snort3_rule_file = RuleFileUtility(snort3_rule_path)

    >>> snort3_rule_file.display_option_statistics()
    >>> snort3_rule_file.display_flowbits_information()
    >>> snort3_rule_file.display_service_contributions()
    >>> snort3_rule_file.activate_all_rules()
    >>> snort3_rule_file.remove_rules(removed_rules=['1:1377:24'])

    >>> snort2_rule_path = pathlib.Path('./snort2-protocol-http.rules')
    >>> snort2_rule_file = RuleFileUtility(snort2_rule_path)

    >>> snort2_rule_file.compare(snort3_rule_file)
    """

    def __init__(self, rule_file):
        if isinstance(rule_file, str):
            self.rule_file: pathlib.Path = pathlib.Path(rule_file)
        elif isinstance(rule_file, pathlib.Path):
            self.rule_file: pathlib.Path = rule_file
        else:
            raise TypeError(f'rule_file must be either str or pathlib.Path, but got {type(rule_file)}')

    @property
    def rules_id_list(self) -> list[str]:
        rules_id_list: list[str] = []

        sid_pattern = re.compile(r"sid:(\d+);")
        rev_pattern = re.compile(r"rev:(\d+);")
        gid_pattern = re.compile(r"gid:(\d+);")

        with open(self.rule_file) as f:
            for line in f:
                sid_match = sid_pattern.search(line)
                if not sid_match:
                    continue
                sid_val = sid_match.group(1)

                gid_match = gid_pattern.search(line)
                gid_val = gid_match.group(1) if gid_match else '1'

                rev_match = rev_pattern.search(line)
                rev_val = rev_match.group(1) if rev_match else '1'

                rules_id_list.append(f'{gid_val}:{sid_val}:{rev_val}')

        return rules_id_list

    def compare(self, other):
        if not isinstance(other, RuleFileUtility):
            raise TypeError(f'other must be RuleFileUtility, not {type(other)}')

        self_rules_id = set(self.rules_id_list)
        other_rules_id = set(other.rules_id_list)

        common_rule_id = self_rules_id & other_rules_id
        print(f'The number of rules that are present in both rule files is {len(common_rule_id)}.')
        print(f'{list(itertools.islice(common_rule_id, 10))}......')

        self_exclusive_rule_id = self_rules_id - other_rules_id
        print(f'The number of rules that appear only in {self.rule_file}: {len(self_exclusive_rule_id)}.')
        print(f'{list(itertools.islice(self_exclusive_rule_id, 100))}')

        other_exclusive_rule_id = other_rules_id - self_rules_id
        print(f'The number of rules that appear only in {other.rule_file}: {len(other_exclusive_rule_id)}.')
        print(f'{list(itertools.islice(other_exclusive_rule_id, 100))}')

    def activate_all_rules(self):
        num_of_activated_rules = 0

        import tempfile, os, shutil
        temp_fd, temp_path = tempfile.mkstemp()

        try:
            with open(self.rule_file, 'r', encoding='utf-8') as source_file, os.fdopen(temp_fd, 'w',
                                                                                  encoding='utf-8') as temp_file:
                for line in source_file:
                    if "sid:" in line and line.startswith("# "):
                        modified_line = line[2:]
                        num_of_activated_rules += 1
                    else:
                        modified_line = line
                    temp_file.write(modified_line)
            shutil.move(temp_path, self.rule_file)
        except Exception as e:
            print(f"An error happened: {e}")
            os.remove(temp_path)
        finally:
            print(f'The number of activated rules: {num_of_activated_rules}')

    def remove_rules(self, removed_rules: list[str]):
        num_of_removed_rules = 0

        import tempfile, os, shutil
        temp_fd, temp_path = tempfile.mkstemp()

        patterns = {
            'gid': r'gid\s*:\s*(\d+)',
            'sid': r'sid\s*:\s*(\d+)',
            'rev': r'rev\s*:\s*(\d+)',
        }

        try:
            with open(self.rule_file, 'r', encoding='utf-8') as source_file, os.fdopen(temp_fd, 'w',
                                                                                  encoding='utf-8') as temp_file:
                for line in source_file:

                    has_sid = re.search(patterns['sid'], line)
                    has_rev = re.search(patterns['rev'], line)

                    if not (has_sid and has_rev):
                        temp_file.write(line)
                        continue

                    sid = has_sid.group(1)
                    rev = has_rev.group(1)

                    has_gid = re.search(patterns['gid'], line)
                    gid = has_gid.group(1) if has_gid else '1'

                    rule_id = f"{gid}:{sid}:{rev}"

                    if rule_id in removed_rules:
                        num_of_removed_rules += 1
                    else:
                        temp_file.write(line)

            shutil.move(temp_path, self.rule_file)
        except Exception as e:
            print(f"An error happened: {e}")
            os.remove(temp_path)
        finally:
            print(f'The number of removed rules: {num_of_removed_rules}')

    def display_option_statistics(self, service: str = None):
        if service is None:
            target_ruleset = RuleSet.from_file(str(self.rule_file))
        else:
            target_ruleset = RuleSet.from_file(str(self.rule_file)).group(service=service)

        statistics = defaultdict(int)

        for rule in target_ruleset.activated_rules:
            for option in rule._rule_body["options"]:
                statistics[option["name"]] += 1

        for option, count in statistics.items():
            print(f"{option}: {count}")

    def display_flowbits_information(self, service: str = None):
        if service is None:
            target_ruleset = RuleSet.from_file(str(self.rule_file))
        else:
            target_ruleset = RuleSet.from_file(str(self.rule_file)).group(service=service)

        print(target_ruleset.flowbits)

    def display_service_contributions(self, services: list[str]=None):

        if services is None:
            services = ['http', 'ftp', 'dns', 'sip']

        target_ruleset = RuleSet.from_file(str(self.rule_file))
        rule_num = len(target_ruleset.rules)

        for proto in services:
            proto_ruleset = target_ruleset.group(service=proto)
            proto_rule_num = len(proto_ruleset.rules)
            print(f'The proportion of {proto} rules is: {proto_rule_num} / {rule_num} = {proto_rule_num / rule_num:.4f}')


if __name__ == '__main__':
    rules_dir = pathlib.Path(__file__).parent.parent.parent / "resources" / 'rules'
    http_rules = {
        'snort3': RuleFileUtility(rules_dir / "snort3-browser-chrome.rules"),
        'snort2': RuleFileUtility(rules_dir / "snort2-browser-chrome.rules"),
    }
    sip_rules = {
        'snort3': RuleFileUtility(rules_dir / "snort3-protocol-voip.rules"),
        'snort2': RuleFileUtility(rules_dir / "snort2-protocol-voip.rules"),
    }
    ftp_rules = {
        'snort3': RuleFileUtility(rules_dir / "snort3-protocol-ftp.rules"),
        'snort2': RuleFileUtility(rules_dir / "snort2-protocol-ftp.rules"),
    }
    dns_rules = {
        'snort3': RuleFileUtility(rules_dir / "snort3-protocol-dns.rules"),
        'snort2': RuleFileUtility(rules_dir / "snort2-protocol-dns.rules"),
    }
    community_rules = {
        'snort3': RuleFileUtility(rules_dir / "snort3-community.rules"),
        'snort2': RuleFileUtility(rules_dir / "snort2-community.rules"),
    }

    ftp_rules['snort3'].display_option_statistics()
    print(f'\n---------------------------------------------------------\n')

    ftp_rules['snort3'].display_flowbits_information()
    print(f'\n---------------------------------------------------------\n')

    ftp_rules['snort3'].display_service_contributions()
    print(f'\n---------------------------------------------------------\n')

    ftp_rules['snort3'].compare(ftp_rules['snort2'])
    print(f'\n---------------------------------------------------------\n')





