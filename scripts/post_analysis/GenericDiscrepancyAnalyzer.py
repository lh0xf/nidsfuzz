import abc
import collections
import itertools
import pathlib

from rule import RuleSet
from scripts.post_analysis.DiscrepancyItem import DiscrepancyItem


class GenericDiscrepancyAnalyzer(abc.ABC):


    def __init__(self, analyzed_file: str, rule_files: list[str]):
        self.analyzed_file = pathlib.Path(analyzed_file)
        self.ruleset = RuleSet.from_files(rule_files)

        # state variables
        self.num_of_all_discrepancies = 0
        self.unique_discrepancy_counter: dict[DiscrepancyItem, int] = collections.defaultdict(int)

        # A dictionary where each key is a string detailing an enforcement issue,
        # and the corresponding value is the rules that failed.
        self.issue_rules: dict[str, set[str]] = {}

    def _reset(self):
        self.num_of_all_discrepancies = 0
        self.unique_discrepancy_counter = collections.defaultdict(int)
        self.issue_rules = {}

    def analyze(self):
        self._reset()

        discrepancy_generator = self.read_discrepancies(str(self.analyzed_file), ignored_num=5)
        while True:
            try:
                seed_rules, triggered_rules = next(discrepancy_generator)
                self.unique_discrepancy_counter[DiscrepancyItem(seed_rules, triggered_rules)] += 1
                self.num_of_all_discrepancies += 1
            except StopIteration:
                break

        self._analyze()

        self._generate_report()

    def _generate_report(self, filename: str = "report.txt"):

        def insert(file, text: str, num: int = 1):
            print(f'\n{text * num}\n', file=file)

        file_path = self.analyzed_file.parent / filename
        with open(file_path, 'w') as f:
            section_number = 1

            print(f'# {section_number}. Number of all discrepancies\n{self.num_of_all_discrepancies}', file=f)
            section_number += 1

            insert(f, text='======', num=10)

            for i, (description, rules) in enumerate(self.issue_rules.items()):
                if i > 0:
                    insert(f, text='------', num=10)
                print(f'# {section_number}. {description}\n{", ".join(str(item) for item in sorted(rules))}', file=f)
                section_number += 1

            insert(f, text='======', num=10)

            print(f'# {section_number}. Frequency of unique discrepancies', file=f)
            for discrepancy_item, frequency in self.unique_discrepancy_counter.items():
                print(f'{", ".join(discrepancy_item.seed_rules):<35}: {frequency}', file=f)
            section_number += 1


    @staticmethod
    def read_discrepancies(discrepancy_file: str,  ignored_num: int = 0):

        def calculate_discrepancy_line_counts():
            with open(discrepancy_file, 'r', encoding='utf-8') as f:
                for line_count, line in enumerate(f, 1):
                    if line.strip() == "":
                        return line_count
            return 1

        group_size = calculate_discrepancy_line_counts()
        lines_to_skip = ignored_num * group_size + 1

        with open(discrepancy_file, 'r') as f:

            lines = f.readlines()
            lines = lines[:-lines_to_skip]

            for is_seperator, group in itertools.groupby(lines, key=lambda line: line.strip() == ""):
                if is_seperator:
                    continue

                first_line = next(group).strip()
                _, seed_rules = first_line.split(": ", 1)
                seed_rules = seed_rules.split(", ")

                triggered_rules = {}
                for line in group:
                    platform, rules = line.strip().split(":", 1)
                    triggered_rules[platform.strip()] = rules.strip().split(", ") if rules.strip() != '' else []

                yield seed_rules, triggered_rules

    @abc.abstractmethod
    def _analyze(self):
        """This method identifies issue rules from the provided discrepancy items."""
        pass

