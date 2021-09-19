from eu2020.common.parties import Parties


class Budget:

    parties = []
    extra_income = 0
    extra_outcome = 0
    dept = 0


    def add_parties(self, parties: Parties) -> None:
        self.parties.append(parties)


    def get_balance(self) -> int:
            return self.get_income() - self.get_outcome()


    def get_dept(self) -> int:
            return self.dept


    def get_income(self) -> int:
        result = 0
        for p in self.parties:
            result += p.get_budget_contribution()
        return result + self.extra_income


    def get_outcome(self) -> int:
        result = 0
        for p in self.parties:
            result += p.get_budget_consumption()
        return result + self.extra_outcome


    def add_extra_income(self, amt: int) -> None:
        self.extra_income += amt


    def add_extra_outcome(self, amt: int) -> None:
        self.extra_outcome += amt


    def update_balance(self) -> None:
        self.dept -= self.get_income() - self.get_outcome()
        self.extra_income = 0
        self.extra_outcome = 0
