import random
from typing import Optional

import eu2020.data.texts as texts
import eu2020.common.utils as utils
from eu2020.common.budget import Budget
from eu2020.common.parties import Parties
from eu2020 import print_log


class EventProcessor:

    flags = set()
    parties = list()
    all_parties = Parties({}, "ALL")
    all_events = list()

    def __init__(self, flags: set):
        self.flags = flags

    def add_parties(self, parties: Parties) -> None:
        self.parties.append(parties)
        for p in parties.parties:
            if p not in self.all_parties.parties:
                self.all_parties.parties[p] = parties.parties[p]

    def add_events(self, events: list) -> None:
        for ev in events:
            ev["wait"] = 0
            ev["enabled"] = True
            if ev["party"] not in self.all_parties.parties:
                raise ValueError(f"party not found: {ev['party']}")
        self.all_events += events

    def event_filter(self, ev: dict) -> bool:
        if not ev["enabled"] or ev["wait"] != 0:
            return False

        if "condition" in ev:
            if "flag" in ev["condition"]:
                for c in ev["condition"]["flag"]:
                    if c not in self.flags:
                        return False

            if "satisfaction" in ev["condition"]:
                if ev["condition"]["satisfaction"]["op"] == "<":
                    if self.all_parties.parties[ev["party"]]["satisfaction_pct"] >= ev["condition"]["satisfaction"]["value"]:
                        return False
                if ev["condition"]["satisfaction"]["op"] == ">":
                    if self.all_parties.parties[ev["party"]]["satisfaction_pct"] <= ev["condition"]["satisfaction"]["value"]:
                        return False
        return True

    def get_event(self) -> Optional[dict]:
        filtered = list(filter(self.event_filter, self.all_events))
        if filtered:
            return random.choice(filtered)
        return None

    def process_events(self, budget: Budget) -> None:
        for _ in range(random.randint(1, 3)):
            ev = self.get_event()
            if ev is not None:
                country = self.all_parties.parties[ev["party"]]
                utils.print_text_in_box(country["name"])
                self.make_decision(ev, self.all_parties, budget)

    def make_decision(self, ev: dict, members: Parties, budget: Budget) -> None:
        print_log(ev["description"])
        print()
        options = {option["key"]: option for option in ev["options"]}
        descriptions = {key: option["description"] for key, option in options.items()}
        g = utils.input_with_options(texts.options, descriptions)
        option = options[g]
        key = option["key"]
        desc = option["description"]
        print_log(f"({key}) => {desc}", print=False)

        # Set delay
        ev["wait"] = option["delay"]

        # Flag set
        if "flag_set" in option:
            self.flags.add(option["flag_set"])

        if "impact" in option:
            option_impact = option["impact"]

            # Satisfaction
            if "satisfaction" in option_impact:
                members.update_satisfaction(option_impact["satisfaction"])

            # Budget
            if "budget" in option_impact:
                if option_impact["budget"] > 0:
                    budget.add_extra_income(option_impact["budget"])
                else:
                    budget.add_extra_outcome(-1 * option_impact["budget"])
            # Guarantee
            if "guarantee" in option_impact:
                budget.add_guarantee(option_impact["guarantee"])

            # Operation
            if "operation" in option_impact:
                # Remove from party
                if "remove_from_party" == option_impact["operation"]["cmd"]:
                    self.remove_from_party(ev["party"], option_impact["operation"]["party"])

    def remove_from_party(self, member_code: str, party_name: str) -> None:
        self.all_parties.parties[member_code]["enabled"] = False
        for p in self.parties:
            if p.name == party_name:
                p.parties.pop(member_code)
                break

    def next_period(self) -> None:
        for ev in self.all_events:
            if ev["wait"] > 0:
                ev["wait"] -= 1

        for p in self.parties:
            p.next_period()
