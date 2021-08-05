
import os
import random
import eu.data.texts as texts
import eu.data.data as data
import eu.data.events as events
from eu.common.name import Name
from eu.common.period import Period
from eu.common.higher_power_events import HigherPowerEvents
from eu.common.members_events import MembersEvents


def main():
    hp_events = HigherPowerEvents(events.higher_power_events)
    m_events = MembersEvents(events.member_country_events)
    data.period = Period(2020, 0)

    clear()
    print_app_name()

    setup()
    print(texts.intro.format(data.name.get_name5p(), data.name.translate("stal"), len(data.member_countries)))
    proceed()

    while True:
        print_text_in_box(texts.period.format(data.period.get_month(), data.period.get_year()))
        print_budget()
        print_membership_satisfaction()
        print_hp_events(hp_events)
        print()
        proceed()

        for i in range(random.randint(1, 2)):
            ev = m_events.get_event()
            country = data.member_countries[ev["party"]]
            print_text_in_box(country["name"])
            make_decision(ev)

        hpev = hp_events.get_event()
        if hpev != None:
            print_text_in_box(texts.higher_power_event, "!")
            print(hpev + "\n")
            proceed()

        data.period.next()
        m_events.next_period()


def make_decision(ev):
    print(ev["description"])
    print()
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
    n = input(f"{texts.what_is_your_name}\n> ")
    print()
    g = input_with_options(texts.what_is_your_gender, data.gender)
    data.name = Name(n, g)


def print_app_name():
    print_text_in_box(texts.app_name)


def print_text_in_box(text, ch="*"):
    boxw = len(text) + 4
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
    clear()
    return a


def proceed():
    input(texts.proceed)
    clear()


def clear():
    clr = lambda: os.system('cls')
    clr()

