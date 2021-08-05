class Parties:

    parties = {}


    def __init__(self, parties):
        self.parties = parties


    def get_satisfaction_pct(self):
        i = 0
        s = 0
        for c in self.parties.keys():
            s += self.parties[c]["satisfaction_pct"]
            i += 1
        return s / i


    def update_satisfaction(self, satisfaction):
        for c in satisfaction.keys():
            self.parties[c]["satisfaction_pct"] += satisfaction[c]
            if self.parties[c]["satisfaction_pct"] < 0:
                self.parties[c]["satisfaction_pct"] = 0
