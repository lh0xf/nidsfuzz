import collections
import itertools

import numpy as np
from thefuzz import fuzz

import utils
from scripts.post_analysis.DiscrepancyItem import DiscrepancyItem
from scripts.post_analysis.GenericDiscrepancyAnalyzer import GenericDiscrepancyAnalyzer


class PassThroughDiscrepancyAnalyzer(GenericDiscrepancyAnalyzer):

    def _analyze(self):
        self._analyze_crude_rules()

        for discrepancy in self.unique_discrepancy_counter.keys():
            self._analyze_chameleon_rules(discrepancy)
            self._analyze_stutter_rules(discrepancy)
            self._analyze_duplicate_rules(discrepancy)
            self._analyze_overlapping_and_orthogonal_rules(discrepancy)

    def _analyze_crude_rules(self):
        description = "Crude rules with overly broad signatures that can be triggered by almost any packet."
        crude_rules: list[str] = []

        rule_counter: dict[str, int] = collections.defaultdict(int)

        for discrepancy, frequency in self.unique_discrepancy_counter.items():
            all_triggered_rules: list[str] = []
            for triggered_rules in discrepancy.triggered_rules.values():
                all_triggered_rules.extend(triggered_rules)

            for rule in sorted(set(all_triggered_rules)):
                rule_counter[rule] += 1 * frequency

        # Interquartile Range Method
        rule_occurrence = list(rule_counter.values())
        q1 = np.percentile(rule_occurrence, 25)
        q3 = np.percentile(rule_occurrence, 75)
        iqr = q3 - q1
        upper_bound = q3 + 3.0 * iqr

        print(f'data: {rule_occurrence}')
        print(f'q1: {q1}')
        print(f'q3: {q3}')
        print(f'upper bound: {upper_bound}')

        for rule, occurrence in rule_counter.items():
            if occurrence > upper_bound:
                crude_rules.append(rule)
                print(f'{rule}: {occurrence}')

        self.issue_rules.setdefault(description, set()).update(crude_rules)

    def _analyze_chameleon_rules(self, discrepancy: DiscrepancyItem):
        description = "Chameleon rules that exhibit inconsistent alert behavior across different NIDS platforms."
        chameleon_rules = []

        for rule in discrepancy.seed_rules:
            presence_count = 0
            for triggered_rules in discrepancy.triggered_rules.values():
                if rule in triggered_rules:
                    presence_count += 1

            if 0 < presence_count < len(discrepancy.triggered_rules):
                chameleon_rules.append(rule)

        self.issue_rules.setdefault(description, set()).update(chameleon_rules)

    def _analyze_stutter_rules(self, discrepancy: DiscrepancyItem):
        description = "Stutter rules that can't seem to say it just once, repeating the same alert over and over for a single incident."
        stutter_rules = []

        for _, triggered_rules in discrepancy.triggered_rules.items():
            counter = collections.Counter(triggered_rules)
            stutter_rules.extend(
                [rule for rule, count in counter.items() if count > 1]
            )

        self.issue_rules.setdefault(description, set()).update(stutter_rules)

    def _analyze_duplicate_rules(self, discrepancy: DiscrepancyItem):
        description = "Duplicate rules with identical signatures but distinct `sid`."
        duplicate_rules = []

        # For example:

        # alert tcp $EXTERNAL_NET any -> $HOME_NET $SIP_PORTS (
        # msg:"PROTOCOL-VOIP SIP Torture missing CSeq header attempt";
        # flow:to_server,established;
        # content:"SIP/2.0",fast_pattern,nocase;
        # content:!"CSeq:",nocase;
        # metadata:policy max-detect-ips drop;
        # service:sip;
        # reference:url,tools.ietf.org/html/rfc4475;
        # classtype:misc-activity;
        # sid:51767; rev:4; )

        # alert udp $EXTERNAL_NET any -> $HOME_NET $SIP_PORTS (
        # msg:"PROTOCOL-VOIP SIP Torture missing CSeq header attempt";
        # flow:to_server;
        # content:"SIP/2.0",fast_pattern,nocase;
        # content:!"CSeq:",nocase;
        # metadata:policy max-detect-ips drop;
        # service:sip;
        # reference:url,tools.ietf.org/html/rfc4475;
        # classtype:misc-activity;
        # sid:51504; rev:4; )

        for _, triggered_rules in discrepancy.triggered_rules.items():
            deduplicate_triggered_rules = [self.ruleset.find_rule(rule_id) for rule_id in sorted(set(triggered_rules))]
            deduplicate_triggered_rules = [rule for rule in deduplicate_triggered_rules if rule is not None]

            index_map = {}
            for idx, rule in enumerate(deduplicate_triggered_rules):
                # if rule is None:
                #     print()
                fuzzy_signature = rule.fuzzy_signature
                if fuzzy_signature in index_map:
                    index_map[fuzzy_signature].append(idx)
                else:
                    index_map[fuzzy_signature] = [idx]

            for _, idxs in index_map.items():
                if len(idxs) > 1:
                    duplicate_rules.append(
                        tuple([deduplicate_triggered_rules[idx].id for idx in idxs])
                    )

        self.issue_rules.setdefault(description, set()).update(duplicate_rules)

    def _analyze_overlapping_and_orthogonal_rules(self, discrepancy: DiscrepancyItem):
        description1 = "Overlapping rules with similar signatures and consecutive `sid`."
        description2 = "Overlapping rules with similar signatures and non-consecutive `sid`."

        overlapping_rules1, overlapping_rules2 = [], []

        description3 = "Orthogonal rules applied to different sticky buffers."
        description4 = "Orthogonal rules applied to the same sticky buffers but with compatible options."

        orthogonal_rules1, orthogonal_rules2 = [], []

        similarity_threshold = 70
        for triggered_rules in discrepancy.triggered_rules.values():
            unique_rules = [self.ruleset.find_rule(rule_id) for rule_id in sorted(set(triggered_rules))]
            unique_rules = [rule for rule in unique_rules if rule is not None]

            for rule1, rule2 in itertools.combinations(unique_rules, 2):
                levenshtein_similarity = fuzz.partial_ratio(rule1.fuzzy_signature, rule2.fuzzy_signature)
                jaccard_similarity = utils.jaccard_similarity(rule1.fuzzy_signature, rule2.fuzzy_signature)

                print(f'\n---------------------------------------------------\n')
                print(f'{rule1.id}: {rule1.fuzzy_signature}')
                print(f'{rule2.id}: {rule2.fuzzy_signature}')
                print(f'levenshtein: {levenshtein_similarity}')
                print(f'jaccard: {jaccard_similarity}')

                if similarity_threshold < levenshtein_similarity < 100 or (
                        similarity_threshold / 100) < jaccard_similarity < 1.0:
                    sid_diff = abs(int(rule1.get('sid')) - int(rule2.get('sid')))

                    if sid_diff <= 2:
                        overlapping_rules1.append((rule1.id, rule2.id))
                    else:
                        overlapping_rules1.append((rule1.id, rule2.id))

                else:
                    rule1_buffers = set(rule1.signature.keys())
                    rule2_buffers = set(rule2.signature.keys())

                    if not (rule1_buffers & rule2_buffers):
                        orthogonal_rules1.append((rule1.id, rule2.id))
                    else:
                        orthogonal_rules2.append((rule1.id, rule2.id))

        self.issue_rules.setdefault(description1, set()).update(overlapping_rules1)
        self.issue_rules.setdefault(description2, set()).update(overlapping_rules2)
        self.issue_rules.setdefault(description3, set()).update(orthogonal_rules1)
        self.issue_rules.setdefault(description4, set()).update(orthogonal_rules2)


