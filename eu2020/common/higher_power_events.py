import random


class HigherPowerEvents:

    events = []
    active_events = []

    def __init__(self, events: list):
        self.events = events

    def get_event(self) -> str:
        result = None
        i = random.randint(0, 2)
        if i == 0:
            ev = random.choice(self.events)
            if ev in self.active_events:
                self.active_events.remove(ev)
                result = ev["end"]
            else:
                self.active_events.append(ev)
                result = ev["start"]
        return result

    def get_current_events(self) -> str:
        return ", ".join(ev["name"] for ev in self.active_events)
