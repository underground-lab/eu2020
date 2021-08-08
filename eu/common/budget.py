class Budget:

    countries = {}
    extra_income = 0
    extra_outcome = 0
    dept = 0


    def __init__(self, countries):
        self.countries = countries


    def get_balance(self):
            return self.get_income() - self.get_outcome()


    def get_dept(self):
            return self.dept


    def get_income(self):
        return self.countries.get_budget_contribution() + self.extra_income


    def get_outcome(self):
        return self.countries.get_budget_consumption() + self.extra_outcome


    def add_extra_income(self, amt):
        self.extra_income += amt


    def add_extra_outcome(self, amt):
        self.extra_outcome += amt


    def update_balance(self):
        self.dept -= self.get_income() - self.get_outcome()
        self.extra_income = 0
        self.extra_outcome = 0
    