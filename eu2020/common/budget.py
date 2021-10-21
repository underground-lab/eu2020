import eu2020.data.colors as colors
from eu2020.common.parties import Parties


class Budget:

    parties = []
    budget = {
        "extra_income": 0,
        "extra_outcome": 0,
        "dept": 0,
        "guarantee": 0
    }

    def add_parties(self, parties: Parties) -> None:
        self.parties.append(parties)

    def get_balance(self) -> int:
        return self.get_income() - self.get_outcome()

    def get_dept(self) -> int:
        return self.budget["dept"]

    def get_income(self) -> int:
        result = 0
        for p in self.parties:
            result += p.get_budget_contribution()
        return result + self.budget["extra_income"]

    def get_outcome(self) -> int:
        result = 0
        for p in self.parties:
            result += p.get_budget_consumption()
        return result + self.budget["extra_outcome"]

    def add_extra_income(self, amt: int) -> None:
        self.budget["extra_income"] += amt

    def add_extra_outcome(self, amt: int) -> None:
        self.budget["extra_outcome"] += amt

    def add_guarantee(self, amt: int) -> None:
        self.budget["guarantee"] += amt

    def update_balance(self) -> None:
        self.budget["dept"] -= self.get_income() - self.get_outcome()
        self.budget["extra_income"] = 0
        self.budget["extra_outcome"] = 0

    def get_budget_report(self):
        result = ""

        result += "Příjmy:            [{}]{:20,} EUR[/{}]\n" \
            .format(colors.numbers, self.get_income(), colors.numbers)
        result += "Výdaje:            [{}]{:20,} EUR[/{}]\n" \
            .format(colors.numbers, self.get_outcome(), colors.numbers)

        diff = self.get_income() - self.get_outcome()
        color = colors.numbers
        if diff > 0:
            color = colors.positive_progress
        if diff < 0:
            color = colors.negative_progress
        result += "Bilance:           [{}]{:{}20,} EUR[/{}]\n".format(color, diff, '+' if diff else '', color)

        result += "Mimořádné příjmy:  [{}]{:20,} EUR[/{}]\n" \
            .format(colors.numbers, self.budget["extra_income"], colors.numbers)
        result += "Mimořádní výdaje:  [{}]{:20,} EUR[/{}]\n" \
            .format(colors.numbers, self.budget["extra_outcome"], colors.numbers)
        result += "Dluh:              [{}]{:20,} EUR[/{}]\n" \
            .format(colors.numbers, self.budget["dept"], colors.numbers)
        result += "Garance:           [{}]{:20,} EUR[/{}]\n" \
            .format(colors.numbers, self.budget["guarantee"], colors.numbers)

        return result
