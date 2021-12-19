import random
import eu2020.data.texts as texts
import eu2020.common.utils as utils
from eu2020.common.budget import Budget
from eu2020.common.parties import Parties
from eu2020.common.parties_events import PartiesEvents
from eu2020 import print_log


class EventProcessor:

    events = set()
    flags = set()
    all_parties = Parties({})

    def __init__(self, flags: set):
        self.flags = flags

    def add_events(self, events: PartiesEvents) -> None:
        self.events.add(events)
        parties = events.get_parties().parties
        for p in parties:
            if p not in self.all_parties.parties:
                self.all_parties.parties[p] = parties[p]

    def add_stories(self, stories: list) -> None:
        for s in stories:
            sorted = False
            for pe in self.events:
                p = pe.get_parties()
                if s["party"] in p.parties:
                    pe.add_event(s)
                    sorted = True
                    continue
            assert(sorted is True)

    def process_events(self, budget: Budget) -> None:
        for party_evs in self.events:
            for _ in range(random.randint(0, 2)):
                ev = party_evs.get_event()
                if ev is not None:
                    country = party_evs.get_parties().parties[ev["party"]]
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

    def next_period(self) -> None:
        for evs in self.events:
            evs.next_period()
