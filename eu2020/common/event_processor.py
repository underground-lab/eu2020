import random
import eu2020.data.texts as texts
import eu2020.common.utils as utils
from eu2020.common.parties import Parties


class EventProcessor:

    events = []
    all_parties = Parties({})


    def add_events(self, events):
        self.events.append(events)
        parties = events.get_parties().parties
        for p in parties.keys():
            if p not in self.all_parties.parties.keys():
                self.all_parties.parties[p] = parties[p]


    def process_events(self, budget):
        for evs in self.events:
            for _ in range(random.randint(1, 3)):
                ev = evs.get_event()
                if ev is not None:
                    country = evs.get_parties().parties[ev["party"]]
                    utils.print_text_in_box(country["name"])
                    self.make_decision(ev, self.all_parties, budget)


    def make_decision(self, ev, members, budget):
        print(ev["description"])
        print()
        dopt = {}
        for opt in ev["options"]:
            dopt[opt["key"]] = opt["description"]
        g = utils.input_with_options(texts.options, dopt)
        options = list(filter(lambda o: o["key"] == g, ev["options"]))
        
        # Satisfaction
        members.update_satisfaction(options[0]["impact"]["satisfaction"])

        # Budget
        b = options[0]["impact"]["budget"]
        budget.add_extra_income(b)


    def next_period(self):
        for evs in self.events:
            evs.next_period()
