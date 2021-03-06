import random


class HigherPowerEvents:

    events = []
    flags = set()

    def __init__(self, events: list, flags: set):
        self.events = events
        self.flags = flags

    def get_event(self) -> str:
        result = None
        i = random.randint(0, 2)
        if i == 0:
            ev = random.choice(self.events)
            if ev["key"] in self.flags:
                if ev["wait"] == 0:
                    self.flags.remove(ev["key"])
                    result = ev["end"]
            else:
                self.flags.add(ev["key"])
                ev["wait"] = ev["duration"]
                result = ev["start"]
        return result

    def get_current_events(self) -> str:
        return ", ".join(ev["name"] for ev in self.events if ev["key"] in self.flags)

    def next_period(self) -> None:
        for ev in self.events:
            if ev["key"] in self.flags and ev["wait"] > 0:
                ev["wait"] -= 1
