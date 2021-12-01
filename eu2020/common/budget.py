from string import Template

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
            - self.get_guarantee() // 4
        self.budget["extra_income"] = 0
        self.budget["extra_outcome"] = 0
        self.budget["guarantee"] = self.get_guarantee() // 2

    def get_budget_report(self):
        number_format = "20,"
        color = colors.numbers
        budget_values = dict(
            income=f"{self.get_income():{number_format}}",
            outcome=f"{self.get_outcome():{number_format}}",
            extra_income=f"{self.get_extra_income():{number_format}}",
            extra_outcome=f"{self.get_extra_outcome():{number_format}}",
            dept=f"{self.get_dept():{number_format}}",
            guarantee=f"{self.get_guarantee():{number_format}}",
            number_color=color,
        )

        balance = self.get_balance()
        if balance:
            color = colors.positive_progress if balance > 0 else colors.negative_progress
            number_format = "+" + number_format
        budget_values.update(
            balance=f"{balance:{number_format}}",
            balance_color=color,
        )

        return Template(texts.budget_report_template).substitute(budget_values)
