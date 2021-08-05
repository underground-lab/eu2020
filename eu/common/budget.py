class Budget:

    countries = {}
    extra_income = 0
    extra_outcome = 0


    def __init__(self, countries):
        self.countries = countries


    def get_balance(self):
        return self.countries.get_budget_contribution()


    def get_income(self):
        return self.get_balance() + self.extra_income


    def get_outcome(self):
        return self.get_balance() + self.extra_outcome


    def add_extra_income(self, amt):
        self.extra_income += amt


    def add_extra_outcome(self, amt):
        self.extra_outcome += amt
