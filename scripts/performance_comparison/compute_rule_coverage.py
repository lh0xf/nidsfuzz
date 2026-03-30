import pathlib
import re

total_rules = 4661
print("-" * 20)
print(f"Total rules: {total_rules}")


alert_dir = pathlib.Path(__file__).resolve().parent / 'logs-boofuzz' / 'Suricata'
print("-" * 20)
print(f"Alert dir: {alert_dir}")


ALERT_PATTERN = (r'^.*? \[\*\*] \[(?P<rule_id>\d+:\d+:\d+)] .*? \[\*\*] \[Classification.*?] \[Priority.*?] \{.*?} '
                     r'(?P<src_ip>\d+\.\d+\.\d+.\d+):(?P<src_port>\d+) -> (?P<dst_ip>\d+\.\d+\.\d+.\d+):('
                     r'?P<dst_port>\d+)')
alert_pattern = re.compile(ALERT_PATTERN)

alert_file_extensions = ['fast.log', 'snort3.log', 'snort2.log']

rule_coverage = set()

for filename in sorted(alert_dir.rglob('*.log')):
    if not filename.is_file():
        continue

    if any(p in filename.name for p in alert_file_extensions):
        unique_rules = set()
        print(f'\tProcessing {filename}')
        with open(filename) as f:
            for line in f:
                match = alert_pattern.match(line)
                if match:
                    rule_id, src_ip, src_port, dst_ip, dst_port = match.groups()
                    unique_rules.add(rule_id)
        print(f'\tFound {len(unique_rules)} unique rules')
        rule_coverage.update(unique_rules)


print("-" * 20)
print(f'Triggered rules: {len(rule_coverage)}')


print("-" * 20)
print(f'Rule coverage: {(len(rule_coverage) / total_rules):.2%}')
