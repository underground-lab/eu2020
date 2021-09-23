import copy


class Parties:

    parties = {}
    parties_prev = {}


    def __init__(self, parties: dict):
        self.parties = parties
        self.parties_prev = copy.deepcopy(self.parties)


    def get_satisfaction_pct(self) -> float:
        i = 0
        s = 0
        for c in self.parties.keys():
            s += self.parties[c]["satisfaction_pct"]
            i += 1
        return s / i


    def get_detailed_satisfaction_report(self) -> str:
        result = ""
        w = 0
        for c in self.parties.keys():
            t = len(self.parties[c]["name"])
            if w < t:
                w = t
        w += 3
        for c in self.parties.keys():
            result += self.parties[c]["name"]
            for _ in range(w - len(self.parties[c]["name"])):
                result += " "
            result += "{:.2f} %".format(self.parties[c]["satisfaction_pct"])
            diff = self.parties[c]["satisfaction_pct"] - self.parties_prev[c]["satisfaction_pct"]
            if diff != 0:
                result += "  ({:+.2f} %)".format(diff)
            result += "\n"
        return result


    def update_satisfaction(self, satisfaction: dict) -> None:
        for c in satisfaction.keys():
            self.parties[c]["satisfaction_pct"] += satisfaction[c]
            if self.parties[c]["satisfaction_pct"] < 0:
                self.parties[c]["satisfaction_pct"] = 0


    def get_budget_contribution(self) -> int:
        result = 0
        for c in self.parties.keys():
            result += self.parties[c]["budget_contribution"]
        return result


    def get_budget_consumption(self) -> int:
        result = 0
        for c in self.parties.keys():
            result += self.parties[c]["budget_consumption"]
        return result


    def next_period(self) -> None:
        self.parties_prev = copy.deepcopy(self.parties)
