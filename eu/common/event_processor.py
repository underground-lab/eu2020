import random
import eu.data.data as data
import eu.data.texts as texts
import eu.common.utils as utils


class EventProcessor:

    events = []


    def add_events(self, events):
        self.events.append(events)


    def process_events(self, budget):
        for evs in self.events:
            for _ in range(random.randint(1, 2)):
                ev = evs.get_event()
                country = data.member_countries[ev["party"]]
                utils.print_text_in_box(country["name"])
                self.make_decision(ev, evs.get_parties(), budget)


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
