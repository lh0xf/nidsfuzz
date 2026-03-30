import pathlib

from scripts.post_analysis.BlendingDiscrepancyAnalyzer import BlendingDiscrepancyAnalyzer
from scripts.post_analysis.PassThroughDiscrepancyAnalyzer import PassThroughDiscrepancyAnalyzer



mutation_strategy = 'blending-3'

############################################
############################################

fuzzing_results = {
    'pass-through': pathlib.Path(__file__).parent.parent.parent / 'benchmark' / 'fuzzing-results-pass',
    'obfuscation': pathlib.Path(__file__).parent.parent.parent / 'benchmark' / 'fuzzing-results-obf',
    'repetition-block': pathlib.Path(__file__).parent.parent.parent / 'benchmark' / 'fuzzing-results-repe_block',
    'repetition-element': pathlib.Path(__file__).parent.parent.parent / 'benchmark' / 'fuzzing-results-repe_element',
    'blending-2': pathlib.Path(__file__).parent.parent.parent / 'benchmark' / 'fuzzing-results-blending_2',
    'blending-3': pathlib.Path(__file__).parent.parent.parent / 'benchmark' / 'fuzzing-results-blending_3',
}

discrepancy_analyzer = {
    'pass-through': PassThroughDiscrepancyAnalyzer,
    'obfuscation': PassThroughDiscrepancyAnalyzer,
    'repetition-block': PassThroughDiscrepancyAnalyzer,
    'repetition-element': PassThroughDiscrepancyAnalyzer,
    'blending-2': BlendingDiscrepancyAnalyzer,
    'blending-3': BlendingDiscrepancyAnalyzer,
    'blending-4': BlendingDiscrepancyAnalyzer,
}

rule_dir = pathlib.Path(__file__).parent.parent.parent / 'benchmark' / 'raw_rules'

tasks = [
    # HTTP fuzzing results
    (
        fuzzing_results[mutation_strategy] / 'http_chrome/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-browser-chrome.rules'
    ),
    (
        fuzzing_results[mutation_strategy] / 'http_firefox/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-browser-firefox.rules'
    ),
    (
        fuzzing_results[mutation_strategy] / 'http_other/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-browser-other.rules'
    ),
    (
        fuzzing_results[mutation_strategy] / 'http_webkit/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-browser-webkit.rules'
    ),
    (
        fuzzing_results[mutation_strategy] / 'http_plugins/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-browser-plugins.rules'
    ),
    (
        fuzzing_results[mutation_strategy] / 'http_ie/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-browser-ie.rules'
    ),

    # FTP fuzzing results
    (
        fuzzing_results[mutation_strategy] / 'ftp_community/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-community.rules'
    ),
    (
        fuzzing_results[mutation_strategy] / 'ftp_ftp/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-protocol-ftp.rules'
    ),

    # DNS fuzzing results
    (
        fuzzing_results[mutation_strategy] / 'dns_community/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-community.rules'
    ),
    (
        fuzzing_results[mutation_strategy] / 'dns_dns/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-protocol-dns.rules'
    ),

    # SIP fuzzing results
    (
        fuzzing_results[mutation_strategy] / 'sip_voip/initiator/log/discrepancies.txt',
        rule_dir / 'snort3-protocol-voip.rules'
    ),
]


def main():
    for discrepancy_file, rule_file in tasks:
        if not discrepancy_file.exists():
            print(f'File not found: {discrepancy_file}')
            continue
        print(f'Analyzing file: {discrepancy_file}')
        analyzer = discrepancy_analyzer[mutation_strategy](analyzed_file=str(discrepancy_file), rule_files=[str(rule_file)], )
        analyzer.analyze()


if __name__ == '__main__':
    main()
