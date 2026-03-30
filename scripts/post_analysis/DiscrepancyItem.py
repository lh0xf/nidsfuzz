import collections


class DiscrepancyItem:

    def __init__(self,
                 seed_rules: list[str],
                 triggered_rules: dict[str, list[str]]):
        self.seed_rules = seed_rules
        self.triggered_rules = triggered_rules

    def __str__(self):
        return f'{self.__class__.__name__ + "(seed_rules=" + repr(self.seed_rules) + ", triggered_rules=" + repr(self.triggered_rules) + ")"}'

    def shallow_equal(self, other) -> bool:
        """
        Check for seed rules equality.
        """
        if not isinstance(other, DiscrepancyItem):
            return False

        if collections.Counter(self.seed_rules) != collections.Counter(other.seed_rules):
            return False

        return True

    def deep_equal(self, other) -> bool:
        return self == other

    def __eq__(self, other):
        """
        Both seed rules and triggered rules must match exactly for equality.
        """
        if not isinstance(other, DiscrepancyItem):
            return False

        # Check seed_rules for equality.
        if collections.Counter(self.seed_rules) != collections.Counter(other.seed_rules):
            return False

        if self.triggered_rules.keys() != other.triggered_rules.keys():
            return False

        # Check triggered_rules for equality.
        for platform in self.triggered_rules:
            if collections.Counter(self.triggered_rules[platform]) != collections.Counter(
                    other.triggered_rules[platform]):
                return False

        return True

    def __hash__(self):
        # Create a hashable, order-independent representation of seed_rules.
        seed_rules_hash = frozenset(collections.Counter(self.seed_rules).items())

        # Create a hashable representation of triggered_rules
        triggered_rules_hash = frozenset(
            (platform, frozenset(collections.Counter(rules).items()))
            for platform, rules in self.triggered_rules.items()
        )

        # Combine the hashes of each component
        return hash((seed_rules_hash, triggered_rules_hash))