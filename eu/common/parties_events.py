import random

class PartiesEvents:

    events = []
    parties = None
    hp_events = None


    def __init__(self, events, parties, hp_events):
        self.events = events
        for ev in self.events:
            ev["wait"] = 0
        self.parties = parties
        self.hp_events = hp_events


    def event_filter(self, ev):
        if "higher_power_cond" in ev:
            met = False
            for he in self.hp_events.active_events:
                if ev["higher_power_cond"] == he["key"]:
                    met = True
                    break
            if met == False:
                return False

        return ev["wait"] == 0


    def get_event(self):
        filtered = list(filter(self.event_filter, self.events))
        if (len(filtered) > 0):
            n = random.randint(0, len(filtered) - 1)
            ev = filtered[n]
            ev["wait"] = 1
            return ev
        else:
            return None


    def get_parties(self):
        return self.parties


    def next_period(self):
        for ev in self.events:
            if ev["wait"] > 0:
                ev["wait"] -= 1
