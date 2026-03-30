from collections import Counter


class InterRulesIssue:

    def __init__(self, *rules: str):
        self._rules = rules
        self._hash = hash(frozenset(Counter(self._rules).items()))

    @property
    def rules(self) -> list[str]:
        return list(self._rules)

    def __eq__(self, other):
        if not isinstance(other, InterRulesIssue):
            raise TypeError(f'not an InterRulesIssue: {type(other)}')

        return Counter(self.rules) == Counter(other.rules)

    def __hash__(self):
        return self._hash