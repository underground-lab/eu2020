import random
import eu.data.texts as texts
import eu.data.data as data
import eu.data.events as events
from eu.common.name import Name
from eu.common.period import Period


def main():
    print(f"\n{texts.app_name}\n")

    n = input(f"{texts.what_is_your_name}\n> ")
    print()
    g = input_with_options(texts.what_is_your_gender, data.gender)
    print()
    name = Name(n, g)

    print(texts.intro.format(name.get_name5p(), name.translate("stal"), len(data.member_countries)))
    proceed()

    period = Period(2020, 0)
    print(texts.period.format(period.get_month(), period.get_year()))
    print(texts.budget.format(data.budget_income, data.budget_outcome))
    proceed()

    for i in range(2):
        filtered = list(filter(lambda ev: ev["wait"] == 0, events.events))
        n = random.randint(0, len(filtered) - 1)
        make_decision(filtered[n])


def make_decision(ev):
    print(ev["description"])
    dopt = {}
    for opt in ev["options"]:
        dopt[opt["key"]] = opt["description"]
    g = input_with_options(texts.options, dopt)
    options = list(filter(lambda o: o["key"] == g, ev["options"]))
    
    #Satisfaction
    s = options[0]["impact"]["satisfaction"]
    for c in s.keys():
        data.member_countries[c]["membership_satisfaction_pct"] += s[c]
        if data.member_countries[c]["membership_satisfaction_pct"] < 0:
            data.member_countries[c]["membership_satisfaction_pct"] = 0

    #Budget
    b = options[0]["impact"]["budget"]
    if b > 0:
        data.budget_income += b
    else:
        data.budget_outcome -= b

    ev["wait"] = 1


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
