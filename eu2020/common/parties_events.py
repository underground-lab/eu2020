from eu2020.common.parties import Parties


class PartiesEvents:

    events = []
    flags = set()
    parties = None

    def __init__(self, events: list, parties: Parties, flags: set):
        self.events = events
        self.flags = flags
        for ev in self.events:
            ev["wait"] = 0
        self.parties = parties

    def add_event(self, ev: dict) -> None:
        ev["wait"] = 0
        self.events.append(ev)

    def get_parties(self) -> Parties:
        return self.parties

    def next_period(self) -> None:
        for ev in self.events:
            if ev["wait"] > 0:
                ev["wait"] -= 1

        self.parties.next_period()

    def __str__(self):
        return f"{self.__class__.__name__}<{','.join(self.parties.parties)}>"
