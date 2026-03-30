import pathlib

from rule import RuleSet
from scripts.issues.BlendingIssues import BlendingIssues, blending_issues
from scripts.pre_preparation.RuleFileUtility import RuleFileUtility

anchor = pathlib.Path(__file__).parent.parent.parent / 'benchmark' / 'rules'

http_chrome_rules = {
    'snort3': anchor / 'snort3-browser-chrome.rules',
    'snort2': anchor / 'snort2-browser-chrome.rules',
}
http_firefox_rules = {
    'snort3': anchor / 'snort3-browser-firefox.rules',
    'snort2': anchor / 'snort2-browser-firefox.rules',
}
http_other_rules = {
    'snort3': anchor / 'snort3-browser-other.rules',
    'snort2': anchor / 'snort2-browser-other.rules',
}
http_ie_rules = {
    'snort3': anchor / 'snort3-browser-ie.rules',
    'snort2': anchor / 'snort2-browser-ie.rules',
}
http_plugins_rules = {
    'snort3': anchor / 'snort3-browser-plugins.rules',
    'snort2': anchor / 'snort2-browser-plugins.rules',
}
http_webkit_rules = {
    'snort3': anchor / 'snort3-browser-webkit.rules',
    'snort2': anchor / 'snort2-browser-webkit.rules',
}

ftp_ftp_rules = {
    'snort3': anchor / 'snort3-protocol-ftp.rules',
    'snort2': anchor / 'snort2-protocol-ftp.rules',
}
ftp_community_rules = {
    'snort3': anchor / 'snort3-community.rules',
    'snort2': anchor / 'snort2-community.rules',
}

dns_dns_rules = {
    'snort3': anchor / 'snort3-protocol-dns.rules',
    'snort2': anchor / 'snort2-protocol-dns.rules',
}

dns_community_rules = {
    'snort3': anchor / 'snort3-community.rules',
    'snort2': anchor / 'snort2-community.rules',
}

sip_voip_rules = {
    'snort3': anchor / 'snort3-protocol-voip.rules',
    'snort2': anchor / 'snort2-protocol-voip.rules',
}


all_http_rules = [
    http_chrome_rules,
    http_firefox_rules,
    http_other_rules,
    http_ie_rules,
    http_plugins_rules,
    http_webkit_rules,
]

all_ftp_rules = [
    ftp_ftp_rules,
    ftp_community_rules,
]

all_dns_rules = [
    dns_dns_rules,
    dns_community_rules,
]

all_sip_rules = [
    sip_voip_rules,
]

def preparation():
    # Define parameters
    removed_rules = blending_issues.sip_removed_rules
    # print(f'{len(removed_rules)}')
    rule_files = sip_voip_rules

    # Initialise file handlers
    snort3_rule_file = RuleFileUtility(rule_files['snort3'])
    snort2_rule_file = RuleFileUtility(rule_files['snort2'])

    # Step 1: Activate all rules in both snort3 and snort2 files.
    snort3_rule_file.activate_all_rules()
    snort2_rule_file.activate_all_rules()

    print(f'\n---------------------------------------------------------\n')

    # Step 2: Remove rules with enforcement issues identified by the pass-through strategy.
    snort2_rule_file.remove_rules(removed_rules)
    snort3_rule_file.remove_rules(removed_rules)

    print(f'\n---------------------------------------------------------\n')

    # Step 3: Compare the files to confirm they contain the same rules.
    snort3_rule_file.compare(snort2_rule_file)

    print(f'\n---------------------------------------------------------\n')


if __name__ == '__main__':
    preparation()
