from scripts.statistics.PassThroughIssues import passthrough_issues as passthrough
from scripts.statistics.ObfuscationIssues import obfuscation_issues as obfuscation
from scripts.statistics.RepetitionBlockIssues import repetition_block_issues as repetition_block
from scripts.statistics.RepetitionElementIssues import repetition_element_issues as repetition_element
from scripts.statistics.Blending2Issues import blending_2_issues as blending


def crude_rules_stats(*issues):
    http_crude_rules = set()
    ftp_crude_rules = set()
    dns_crude_rules = set()
    sip_crude_rules = set()
    for issue in issues:
        http_crude_rules.update(issue.http_crude_rules)
        ftp_crude_rules.update(issue.ftp_crude_rules)
        dns_crude_rules.update(issue.dns_crude_rules)
        sip_crude_rules.update(issue.sip_crude_rules)
    print('http_crude_rules:', len(http_crude_rules))
    print('ftp_crude_rules:', len(ftp_crude_rules))
    print('dns_crude_rules:', len(dns_crude_rules))
    print('sip_crude_rules:', len(sip_crude_rules))

    return http_crude_rules, ftp_crude_rules, dns_crude_rules, sip_crude_rules


def duplicate_rules_stats(*issues):
    http_duplicate_rules = set()
    ftp_duplicate_rules = set()
    dns_duplicate_rules = set()
    sip_duplicate_rules = set()
    for issue in issues:
        http_duplicate_rules.update(issue.http_duplicate_rules)
        ftp_duplicate_rules.update(issue.ftp_duplicate_rules)
        dns_duplicate_rules.update(issue.dns_duplicate_rules)
        sip_duplicate_rules.update(issue.sip_duplicate_rules)
    print('http_duplicate_rules:', len(http_duplicate_rules))
    print('ftp_duplicate_rules:', len(ftp_duplicate_rules))
    print('dns_duplicate_rules:', len(dns_duplicate_rules))
    print('sip_duplicate_rules:', len(sip_duplicate_rules))

    return http_duplicate_rules, ftp_duplicate_rules, dns_duplicate_rules, sip_duplicate_rules


def stutter_rules_stats(*issues):
    http_stutter_rules = set()
    ftp_stutter_rules = set()
    dns_stutter_rules = set()
    sip_stutter_rules = set()
    for issue in issues:
        http_stutter_rules.update(issue.http_stutter_rules)
        ftp_stutter_rules.update(issue.ftp_stutter_rules)
        dns_stutter_rules.update(issue.dns_stutter_rules)
        sip_stutter_rules.update(issue.sip_stutter_rules)
    print('http_stutter_rules:', len(http_stutter_rules))
    print('ftp_stutter_rules:', len(ftp_stutter_rules))
    print('dns_stutter_rules:', len(dns_stutter_rules))
    print('sip_stutter_rules:', len(sip_stutter_rules))

    return http_stutter_rules, ftp_stutter_rules, dns_stutter_rules, sip_stutter_rules


def orthogonal_rules_stats(*issues):
    http_orthogonal_rules = set()
    ftp_orthogonal_rules = set()
    dns_orthogonal_rules = set()
    sip_orthogonal_rules = set()
    for issue in issues:
        http_orthogonal_rules.update(issue.http_orthogonal_rules)
        ftp_orthogonal_rules.update(issue.ftp_orthogonal_rules)
        dns_orthogonal_rules.update(issue.dns_orthogonal_rules)
        sip_orthogonal_rules.update(issue.sip_orthogonal_rules)
    print('http_orthogonal_rules:', len(http_orthogonal_rules))
    print('ftp_orthogonal_rules:', len(ftp_orthogonal_rules))
    print('dns_orthogonal_rules:', len(dns_orthogonal_rules))
    print('sip_orthogonal_rules:', len(sip_orthogonal_rules))

    return http_orthogonal_rules, ftp_orthogonal_rules, dns_orthogonal_rules, sip_orthogonal_rules


def effective_issues():
    passthrough_dns_effective_issues = passthrough.dns_crude_rules | passthrough.dns_chameleon_rules | passthrough.dns_stutter_rules
    passthrough_ftp_effective_issues = passthrough.ftp_crude_rules | passthrough.ftp_chameleon_rules | passthrough.ftp_stutter_rules
    passthrough_sip_effective_issues = passthrough.sip_crude_rules | passthrough.sip_stutter_rules
    passthrough_http_effective_issues = passthrough.http_crude_rules | passthrough.http_chameleon_rules | passthrough.http_stutter_rules

    print(
        f"PassThrough | HTTP: {len(passthrough_http_effective_issues)}")
    print(
        f"PassThrough | FTP: {len(passthrough_ftp_effective_issues)}")
    print(
        f"PassThrough | DNS: {len(passthrough_dns_effective_issues)}")
    print(
        f"PassThrough | SIP: {len(passthrough_sip_effective_issues)}")


    print(f'\n=============================================================\n')

    obfuscation_dns_effective_issues = obfuscation.dns_crude_rules | obfuscation.dns_chameleon_rules | obfuscation.dns_stutter_rules - passthrough_dns_effective_issues
    obfuscation_ftp_effective_issues = obfuscation.ftp_crude_rules | obfuscation.ftp_chameleon_rules | obfuscation.ftp_stutter_rules - passthrough_ftp_effective_issues
    obfuscation_sip_effective_issues = obfuscation.sip_crude_rules | obfuscation.sip_stutter_rules - passthrough_sip_effective_issues
    obfuscation_http_effective_issues = obfuscation.http_crude_rules | obfuscation.http_chameleon_rules | obfuscation.http_stutter_rules - passthrough_http_effective_issues

    print(
        f"Obfuscation | HTTP: {len(obfuscation_http_effective_issues)}")
    print(
        f"Obfuscation | FTP: {len(obfuscation_ftp_effective_issues)}")
    print(
        f"Obfuscation | DNS: {len(obfuscation_dns_effective_issues)}")
    print(
        f"Obfuscation | SIP: {len(obfuscation_sip_effective_issues)}")


    print(f'\n=============================================================\n')

    print(
        f"RepetitionBlock | HTTP: {len(repetition_block.http_crude_rules | repetition_block.http_chameleon_rules | repetition_block.http_stutter_rules - passthrough_http_effective_issues)}")
    print(
        f"RepetitionBlock | FTP: {len(repetition_block.ftp_crude_rules | repetition_block.ftp_chameleon_rules | repetition_block.ftp_stutter_rules - passthrough_ftp_effective_issues)}")
    print(
        f"RepetitionBlock | DNS: {len(repetition_block.dns_crude_rules | repetition_block.dns_chameleon_rules | repetition_block.dns_stutter_rules - passthrough_dns_effective_issues)}")
    print(
        f"RepetitionBlock | SIP: {len(repetition_block.sip_crude_rules | repetition_block.sip_stutter_rules - passthrough_sip_effective_issues)}")

    print(f'\n=============================================================\n')

    print(
        f"RepetitionElement | HTTP: {len(repetition_element.http_crude_rules | repetition_element.http_chameleon_rules | repetition_element.http_stutter_rules - passthrough_http_effective_issues)}")
    print(
        f"RepetitionElement | FTP: {len(repetition_element.ftp_crude_rules | repetition_element.ftp_chameleon_rules | repetition_element.ftp_stutter_rules - passthrough_ftp_effective_issues)}")
    print(
        f"RepetitionElement | DNS: {len(repetition_element.dns_crude_rules | repetition_element.dns_chameleon_rules | repetition_element.dns_stutter_rules - passthrough_dns_effective_issues)}")
    print(
        f"RepetitionElement | SIP: {len(repetition_element.sip_crude_rules | repetition_element.sip_stutter_rules - passthrough_sip_effective_issues)}")

    print(f'\n=============================================================\n')

    print(
        f"Blending | HTTP: {len(blending.http_crude_rules | blending.http_chameleon_rules | blending.http_stutter_rules - passthrough_http_effective_issues)}")
    print(
        f"Blending | FTP: {len(blending.ftp_crude_rules | blending.ftp_chameleon_rules | blending.ftp_stutter_rules - passthrough_ftp_effective_issues)}")
    print(
        f"Blending | DNS: {len(blending.dns_crude_rules | blending.dns_chameleon_rules | blending.dns_stutter_rules - passthrough_dns_effective_issues)}")
    print(
        f"Blending | SIP: {len(blending.sip_crude_rules | blending.sip_stutter_rules - passthrough_sip_effective_issues)}")


if __name__ == '__main__':
    issues = [passthrough, obfuscation, repetition_block, repetition_element, blending]

    # crude_rules_stats(*issues)
    # stutter_rules_stats(*issues)
    duplicate_rules_stats(*issues)
    orthogonal_rules_stats(*issues)

