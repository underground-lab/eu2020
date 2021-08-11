import eu.data.texts as texts
import eu.data.data as data
import eu.data.events as events
import eu.common.utils as utils
from eu.common.name import Name
from eu.common.period import Period
from eu.common.higher_power_events import HigherPowerEvents
from eu.common.parties_events import PartiesEvents
from eu.common.parties import Parties
from eu.common.budget import Budget
from eu.common.event_processor import EventProcessor


def main():
    members = Parties(data.member_countries)
    administration = Parties(data.eu_administration)
    deep_state = Parties(data.deep_state)

    hp_events = HigherPowerEvents(events.higher_power_events)
    m_events = PartiesEvents(events.member_country_events, members)
    deep_events = PartiesEvents(events.deep_state_events, deep_state)

    event_processor = EventProcessor()
    event_processor.add_events(m_events)
    event_processor.add_events(deep_events)

    budget = Budget()
    budget.add_parties(members)
    budget.add_parties(administration)
    budget.add_parties(deep_state)

    data.period = Period(2020, 0)

    utils.clear()
    print_app_name()

    setup()
    print(texts.intro.format(data.name.get_name5p(), data.name.translate("stal"), len(data.member_countries)))
    utils.proceed()

    while True:
        utils.print_text_in_box(texts.period.format(data.period.get_month(), data.period.get_year()))
        print_budget(budget)
        print_membership_satisfaction(members)
        print_hp_events(hp_events)
        print()
        utils.proceed()

        event_processor.process_events(budget)

        hpev = hp_events.get_event()
        if hpev != None:
            utils.print_text_in_box(texts.higher_power_event, "!")
            print(hpev + "\n")
            utils.proceed()

        data.period.next()
        event_processor.next_period()
        if data.period.month == 0:
            budget.update_balance()


def print_budget(budget):
    print(texts.budget.format(data.period.get_year(), budget.get_income(), budget.get_balance(), budget.get_dept()))


def print_membership_satisfaction(members):
    print(texts.membership_satisfaction.format(members.get_satisfaction_pct()))


def print_hp_events(hp_events):
    ev = hp_events.get_current_events()
    if ev != "":
        print(texts.higher_power_events.format(hp_events.get_current_events()))


def setup():
    n = input(f"{texts.what_is_your_name}\n> ")
    print()
    g = utils.input_with_options(texts.what_is_your_gender, data.gender)
    data.name = Name(n, g)


def print_app_name():
    utils.print_text_in_box(texts.app_name)
