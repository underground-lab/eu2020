import random

class PartiesEvents:

    events = []
    parties = None


    def __init__(self, events, parties):
        self.events = events
        for ev in self.events:
            ev["wait"] = 0
        self.parties = parties


    def get_event(self):
        filtered = list(filter(lambda ev: ev["wait"] == 0, self.events))
        n = random.randint(0, len(filtered) - 1)
        ev = filtered[n]
        ev["wait"] = 1
        return ev


    def get_parties(self):
        return self.parties


    def next_period(self):
        for ev in self.events:
            if ev["wait"] > 0:
                ev["wait"] -= 1
