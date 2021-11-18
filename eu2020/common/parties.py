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
        w = 3 + max(len(party["name"]) for party in self.parties.values())

        for c in self.parties:
            result += self.parties[c]["name"]
            for _ in range(w - len(self.parties[c]["name"])):
                result += " "
            result += "[{0}]{1:.2f} %[/{0}]".format(colors.numbers, self.parties[c]["satisfaction_pct"])
            diff = self.parties[c]["satisfaction_pct"] - self.parties_prev[c]["satisfaction_pct"]
            if diff != 0:
                color = colors.positive_progress if diff > 0 else colors.negative_progress
                result += "  ([{0}]{1:+.2f} %[/{0}])".format(color, diff)
            result += "\n"
        return result

    def update_satisfaction(self, satisfaction: dict) -> None:
        for code, diff in satisfaction.items():
            party = self.parties[code]
            party["satisfaction_pct"] = max(0, party["satisfaction_pct"] + diff)

    def get_budget_contribution(self) -> int:
        return sum(party["budget_contribution"] for party in self.parties.values())

    def get_budget_consumption(self) -> int:
        return sum(party["budget_consumption"] for party in self.parties.values())

    def next_period(self) -> None:
        self.parties_prev = copy.deepcopy(self.parties)
