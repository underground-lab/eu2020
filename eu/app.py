import random
import eu.data.texts as texts
import eu.data.data as data
import eu.data.events as events
from eu.common.name import Name
from eu.common.period import Period
from eu.common.higher_power_events import HigherPowerEvents


def main():
    print_app_name()
    hp_events = HigherPowerEvents(events.higher_power_events)
    setup()

    print(texts.intro.format(data.name.get_name5p(), data.name.translate("stal"), len(data.member_countries)))
    proceed()

    data.period = Period(2020, 0)

    while True:
        print_app_name()
        print(texts.period.format(data.period.get_month(), data.period.get_year()))
        print_budget()
        print_membership_satisfaction()
        print_hp_events(hp_events)
        print()
        proceed()

        for i in range(2):
            filtered = list(filter(lambda ev: ev["wait"] == 0, events.member_country_events))
            n = random.randint(0, len(filtered) - 1)
            make_decision(filtered[n])

        hpev = hp_events.get_event()
        if hpev != "":
            print_text_in_box(texts.higher_power_event, "!")
            print(hpev + "\n")
            proceed()

        next_period()


def make_decision(ev):
    print(ev["description"])
    dopt = {}
    for opt in ev["options"]:
        dopt[opt["key"]] = opt["description"]
    g = input_with_options(texts.options, dopt)
    options = list(filter(lambda o: o["key"] == g, ev["options"]))
    
    # Satisfaction
    s = options[0]["impact"]["satisfaction"]
    for c in s.keys():
        data.member_countries[c]["membership_satisfaction_pct"] += s[c]
        if data.member_countries[c]["membership_satisfaction_pct"] < 0:
            data.member_countries[c]["membership_satisfaction_pct"] = 0

    # Budget
    b = options[0]["impact"]["budget"]
    data.budget["balance"] += b

    ev["wait"] = 1


def print_budget():
    print(texts.budget.format(data.budget["balance"], data.budget["income"] - data.budget["outcome"]))


def print_membership_satisfaction():
    print(texts.membership_satisfaction.format(count_membership_satisfaction_pct()))


def print_hp_events(hp_events):
    ev = hp_events.get_current_events()
    if ev != "":
        print(texts.higher_power_events.format(hp_events.get_current_events()))


def count_membership_satisfaction_pct():
    i = 0
    s = 0
    for c in data.member_countries.keys():
        s += data.member_countries[c]["membership_satisfaction_pct"]
        i += 1
    return s / i


def setup():
    for ev in events.member_country_events:
        ev["wait"] = 0

    n = input(f"{texts.what_is_your_name}\n> ")
    print()
    g = input_with_options(texts.what_is_your_gender, data.gender)
    print()
    data.name = Name(n, g)


def next_period():
    data.period.next()

    for ev in events.member_country_events:
        if ev["wait"] > 0:
            ev["wait"] -= 1

def print_app_name():
    print_text_in_box(texts.app_name)


def print_text_in_box(text, ch="*"):
    boxw = len(text) + 4
    print("\n")
    for _ in range(boxw):
        print(ch, end = "")
    print("\n{} {} {}".format(ch, text, ch))
    for _ in range(boxw):
        print(ch, end = "")
    print("\n")


def input_with_options(question, options):
    a = None
    while a not in options.keys():
        print(question)
        for o in options.keys():
            print(f"{o} - {options[o]}")
        a = input("> ")
    return a


def proceed():
    input(texts.proceed)
    print()
