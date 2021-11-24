import eu2020.data.colors as colors
import eu2020.data.texts as texts
from eu2020.common.parties import Parties


class Budget:
    def __init__(self):
        self.parties = []
        self.budget = {
            "extra_income": 0,
            "extra_outcome": 0,
            "dept": 0,
            "guarantee": 0
        }

    def add_parties(self, parties: Parties) -> None:
        self.parties.append(parties)

    def get_balance(self) -> int:
        return self.get_income() + self.get_extra_income() \
            - self.get_outcome() - self.get_extra_outcome() - self.get_dept()

    def get_dept(self) -> int:
        return self.budget["dept"]

    def get_income(self) -> int:
        return sum(p.get_budget_contribution() for p in self.parties)

    def get_outcome(self) -> int:
        return sum(p.get_budget_consumption() for p in self.parties)

    def get_extra_income(self):
        return self.budget["extra_income"]

    def get_extra_outcome(self):
        return self.budget["extra_outcome"]

    def get_guarantee(self):
        return self.budget["guarantee"]

    def add_extra_income(self, amt: int) -> None:
        self.budget["extra_income"] += amt

    def add_extra_outcome(self, amt: int) -> None:
        self.budget["extra_outcome"] += amt

    def add_guarantee(self, amt: int) -> None:
        self.budget["guarantee"] += amt

    def update_balance(self) -> None:
        self.budget["dept"] -= self.get_income() + self.get_extra_income() \
            - self.get_outcome() - self.get_extra_outcome() \
            - int(self.get_guarantee() * 0.25)
        self.budget["extra_income"] = 0
        self.budget["extra_outcome"] = 0
        self.budget["guarantee"] = int(self.get_guarantee() * 0.5)

    def get_budget_report(self):
        result = ""

        result += "{0} [{1}]{2:20,} EUR[/{1}]\n" \
            .format(texts.budget_income, colors.numbers, self.get_income())
        result += "{0} [{1}]{2:20,} EUR[/{1}]\n" \
            .format(texts.budget_outcome, colors.numbers, self.get_outcome())
        result += "{0} [{1}]{2:20,} EUR[/{1}]\n" \
            .format(texts.budget_extra_income, colors.numbers, self.get_extra_income())
        result += "{0} [{1}]{2:20,} EUR[/{1}]\n" \
            .format(texts.budget_extra_outcome, colors.numbers, self.get_extra_outcome())
        result += "{0} [{1}]{2:20,} EUR[/{1}]\n" \
            .format(texts.budget_dept, colors.numbers, self.get_dept())

        diff = self.get_balance()
        color = colors.numbers
        if diff > 0:
            color = colors.positive_progress
        if diff < 0:
            color = colors.negative_progress
        result += "{0} [{1}]{2:{3}20,} EUR[/{1}]\n".format(texts.budget_balance, color, diff, '+' if diff else '')

        result += "{0} [{1}]{2:20,} EUR[/{1}]\n" \
            .format(texts.budget_guarantee, colors.numbers, self.get_guarantee())

        return result
