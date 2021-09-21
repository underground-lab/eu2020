import random
from eu2020.common.higher_power_events import HigherPowerEvents
from eu2020.common.parties import Parties


class PartiesEvents:

    events = []
    parties = None
    hp_events = None


    def __init__(self, events: list, parties: Parties, hp_events: HigherPowerEvents):
        self.events = events
        for ev in self.events:
            ev["wait"] = 0
        self.parties = parties
        self.hp_events = hp_events


    def event_filter(self, ev: dict) -> bool:
        if "higher_power_cond" in ev:
            met = False
            for he in self.hp_events.active_events:
                if ev["higher_power_cond"] == he["key"]:
                    met = True
                    break
            if met == False:
                return False

        return ev["wait"] == 0


    def get_event(self) -> dict:
        filtered = list(filter(self.event_filter, self.events))
        if (len(filtered) > 0):
            n = random.randint(0, len(filtered) - 1)
            ev = filtered[n]
            return ev
        else:
            return None


    def get_parties(self) -> Parties:
        return self.parties


    def next_period(self) -> None:
        for ev in self.events:
            if ev["wait"] > 0:
                ev["wait"] -= 1

        self.parties.next_period()
