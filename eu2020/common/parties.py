import copy
import statistics

import eu2020.data.colors as colors


class Parties:

    parties = {}
    parties_prev = {}

    def __init__(self, parties: dict):
        self.parties = parties
        self.parties_prev = copy.deepcopy(self.parties)

    def get_satisfaction_pct(self) -> float:
        return statistics.mean(
            party["satisfaction_pct"] for party in self.parties.values()
        )

    def get_detailed_satisfaction_report(self) -> str:
        result = ""
        w = 0
        for c in self.parties:
            t = len(self.parties[c]["name"])
            if w < t:
                w = t
        w += 3
        for c in self.parties:
            result += self.parties[c]["name"]
            for _ in range(w - len(self.parties[c]["name"])):
                result += " "
            result += "[{}]{:.2f} %[/{}]".format(colors.numbers, self.parties[c]["satisfaction_pct"], colors.numbers)
            diff = self.parties[c]["satisfaction_pct"] - self.parties_prev[c]["satisfaction_pct"]
            if diff > 0:
                result += "  ([{}]{:+.2f} %[/{}])".format(colors.positive_progress, diff, colors.positive_progress)
            if diff < 0:
                result += "  ([{}]{:+.2f} %[/{}])".format(colors.negative_progress, diff, colors.negative_progress)
            result += "\n"
        return result

    def update_satisfaction(self, satisfaction: dict) -> None:
        for c in satisfaction:
            self.parties[c]["satisfaction_pct"] += satisfaction[c]
            if self.parties[c]["satisfaction_pct"] < 0:
                self.parties[c]["satisfaction_pct"] = 0

    def get_budget_contribution(self) -> int:
        result = 0
        for c in self.parties:
            result += self.parties[c]["budget_contribution"]
        return result

    def get_budget_consumption(self) -> int:
        result = 0
        for c in self.parties:
            result += self.parties[c]["budget_consumption"]
        return result

    def next_period(self) -> None:
        self.parties_prev = copy.deepcopy(self.parties)
