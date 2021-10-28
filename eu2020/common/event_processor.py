import random
import eu2020.data.texts as texts
import eu2020.common.utils as utils
from eu2020.common.budget import Budget
from eu2020.common.parties import Parties
from eu2020.common.parties_events import PartiesEvents


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

    def process_events(self, budget: Budget) -> None:
        for evs in self.events:
            for _ in range(random.randint(1, 2)):
                ev = evs.get_event()
                if ev is not None:
                    country = evs.get_parties().parties[ev["party"]]
                    utils.print_text_in_box(country["name"])
                    self.make_decision(ev, self.all_parties, budget)

    def make_decision(self, ev: dict, members: Parties, budget: Budget) -> None:
        print(ev["description"])
        print()
        dopt = {}
        for opt in ev["options"]:
            dopt[opt["key"]] = opt["description"]
        g = utils.input_with_options(texts.options, dopt)
        options = list(filter(lambda o: o["key"] == g, ev["options"]))

        # Set delay
        ev["wait"] = options[0]["delay"]

        # Satisfaction
        if "satisfaction" in options[0]["impact"]:
            members.update_satisfaction(options[0]["impact"]["satisfaction"])

        # Budget
        if "budget" in options[0]["impact"]:
            if options[0]["impact"]["budget"] > 0:
                budget.add_extra_income(options[0]["impact"]["budget"])
            else:
                budget.add_extra_outcome(-1 * options[0]["impact"]["budget"])
        if "guarantee" in options[0]["impact"]:
            budget.add_guarantee(options[0]["impact"]["guarantee"])

        # Flag set
        if "flag_set" in options[0]:
            self.flags.add(options[0]["flag_set"])

    def next_period(self) -> None:
        for evs in self.events:
            evs.next_period()
