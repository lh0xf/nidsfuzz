from thefuzz import fuzz

import utils
from scripts.post_analysis.GenericDiscrepancyAnalyzer import GenericDiscrepancyAnalyzer


class BlendingDiscrepancyAnalyzer(GenericDiscrepancyAnalyzer):

    def __init__(self, analyzed_file: str, rule_files: list[str]):

        super().__init__(analyzed_file, rule_files)

        self.max_num_of_alerts = 0

    def _analyze(self):
        self.analyze_max_alerts()

        for discrepancy in self.unique_discrepancy_counter.keys():
            self._analyze_chameleon_rules(discrepancy)
            self._analyze_stutter_rules(discrepancy)
            self._analyze_overlapping_and_orthogonal_rules(discrepancy)

    def analyze_max_alerts(self):
        description = "Max number of alerts that can be triggered by one test packet."

        for discrepancy in self.unique_discrepancy_counter.keys():
            for triggered_rules in discrepancy.triggered_rules.values():
                if self.max_num_of_alerts < len(triggered_rules):
                    self.max_num_of_alerts = len(triggered_rules)

        self.issue_rules.setdefault(description, set()).add(str(self.max_num_of_alerts))

    def _analyze_chameleon_rules(self, discrepancy):
        description = "Chameleon rules that exhibit inconsistent alert behavior across different NIDS platforms."
        chameleon_rules = []

        def check_rule_presence(elements, lists):
            for element in elements:
                if not all(element in lst for lst in lists):
                    return False
            return True

        elements = discrepancy.seed_rules
        lists = discrepancy.triggered_rules.values()

        if check_rule_presence(elements, lists):
            chameleon_rules.append(tuple(elements))

        self.issue_rules.setdefault(description, set()).update(chameleon_rules)

    def _analyze_stutter_rules(self, discrepancy):
        description = "Stutter rules that can't seem to say it just once, repeating the same alert over and over for a single incident."
        stutter_rules = []

        def check_elements_appear_twice(elements, lists):
            for element in elements:
                if any(lst.count(element) > 2 for lst in lists):
                    return True
            return False

        elements = discrepancy.seed_rules
        lists = discrepancy.triggered_rules.values()

        if check_elements_appear_twice(elements, lists):
            stutter_rules.append(tuple(elements))

        self.issue_rules.setdefault(description, set()).update(stutter_rules)

    def _analyze_overlapping_and_orthogonal_rules(self, discrepancy):
        description1 = "Overlapping rules with similar signatures and consecutive `sid`."
        description2 = "Overlapping rules with similar signatures and non-consecutive `sid`."

        overlapping_rules1, overlapping_rules2 = [], []

        description3 = "Orthogonal rules applied to different sticky buffers."
        description4 = "Orthogonal rules applied to the same sticky buffers but with compatible options."

        orthogonal_rules1, orthogonal_rules2 = [], []

        similarity_threshold = 70

        def check_similarity(seed_rule, triggered_rules):
            for rule_list in triggered_rules:
                if seed_rule not in rule_list:
                    continue  # No need to analyze
                # Remove the seed rule
                rule_list =  [rule for rule in rule_list if rule != seed_rule]
                # Remove rules that are triggered multiple times
                rule_list = [self.ruleset.find_rule(rule_id) for rule_id in sorted(set(rule_list))]

                seed_rule = self.ruleset.find_rule(seed_rule)
                for other_rule in rule_list:
                    levenshtein_similarity = fuzz.partial_ratio(seed_rule.fuzzy_signature, other_rule.fuzzy_signature)
                    jaccard_similarity = utils.jaccard_similarity(seed_rule.fuzzy_signature, other_rule.fuzzy_signature)

                    print(f'\n---------------------------------------------------\n')
                    print(f'{seed_rule.id}: {seed_rule.fuzzy_signature}')
                    print(f'{other_rule.id}: {other_rule.fuzzy_signature}')
                    print(f'levenshtein: {levenshtein_similarity}')
                    print(f'jaccard: {jaccard_similarity}')

                    if similarity_threshold < levenshtein_similarity < 100 or (
                            similarity_threshold / 100) < jaccard_similarity < 1.0:
                        sid_diff = abs(int(seed_rule.get('sid')) - int(other_rule.get('sid')))

                        if sid_diff <= 2:
                            overlapping_rules1.append((seed_rule.id, other_rule.id))
                        else:
                            overlapping_rules1.append((seed_rule.id, other_rule.id))

                    else:
                        buffer_diff = set(seed_rule.signature.keys()) & set(other_rule.signature.keys())

                        if not buffer_diff:
                            orthogonal_rules1.append((seed_rule.id, other_rule.id))
                        else:
                            orthogonal_rules2.append((seed_rule.id, other_rule.id))

        for seed_rule in discrepancy.seed_rules:
            triggered_rules = discrepancy.triggered_rules.values()
            check_similarity(seed_rule, triggered_rules)

        self.issue_rules.setdefault(description1, set()).update(overlapping_rules1)
        self.issue_rules.setdefault(description2, set()).update(overlapping_rules2)
        self.issue_rules.setdefault(description3, set()).update(orthogonal_rules1)
        self.issue_rules.setdefault(description4, set()).update(orthogonal_rules2)








