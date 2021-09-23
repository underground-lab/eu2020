import random
import eu2020.data.texts as texts
import eu2020.common.utils as utils
from eu2020.common.budget import Budget
from eu2020.common.parties import Parties
from eu2020.common.parties_events import PartiesEvents


class EventProcessor:

    events = []
    all_parties = Parties({})


    def add_events(self, events: PartiesEvents) -> None:
        self.events.append(events)
        parties = events.get_parties().parties
        for p in parties.keys():
            if p not in self.all_parties.parties.keys():
                self.all_parties.parties[p] = parties[p]


    def process_events(self, budget: Budget) -> None:
        for evs in self.events:
            for _ in range(random.randint(1, 3)):
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
            budget.add_extra_income(options[0]["impact"]["budget"])
        if "guarantee" in options[0]["impact"]:
            budget.add_guarantee(options[0]["impact"]["guarantee"])


    def next_period(self) -> None:
        for evs in self.events:
            evs.next_period()
