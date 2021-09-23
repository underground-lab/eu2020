import eu2020.data.texts as texts
import eu2020.data.data as data
import eu2020.common.utils as utils
from eu2020.common.name import Name
from eu2020.common.period import Period
from eu2020.common.higher_power_events import HigherPowerEvents
from eu2020.common.parties_events import PartiesEvents
from eu2020.common.parties import Parties
from eu2020.common.budget import Budget
from eu2020.common.event_processor import EventProcessor
from eu2020.data.ev_deep_state import ev_deep_state
from eu2020.data.ev_higher_power import ev_higher_power
from eu2020.data.ev_members import ev_member_country


def main() -> None:
    eu_members = Parties(data.member_countries)
    eu_administration = Parties(data.eu_administration)
    deep_state = Parties(data.deep_state)

    high_power_events = HigherPowerEvents(ev_higher_power)
    eu_members_events = PartiesEvents(ev_member_country, eu_members, high_power_events)
    deep_events = PartiesEvents(ev_deep_state, deep_state, high_power_events)

    event_processor = EventProcessor()
    event_processor.add_events(eu_members_events)
    event_processor.add_events(deep_events)

    budget = Budget()
    budget.add_parties(eu_members)
    budget.add_parties(eu_administration)
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
        print_membership_satisfaction(eu_members)
        print_hp_events(high_power_events)
        print()
        utils.proceed()

        event_processor.process_events(budget)

        hpe = high_power_events.get_event()
        if hpe != None:
            utils.print_text_in_box(texts.higher_power_event, "!")
            print(hpe + "\n")
            utils.proceed()

        utils.print_text_in_box(texts.membership_satisfaction_header)
        print(eu_members.get_detailed_satisfaction_report())
        utils.proceed()

        utils.print_text_in_box(texts.deep_state_satisfaction_header)
        print(deep_state.get_detailed_satisfaction_report())
        utils.proceed()

        data.period.next()
        event_processor.next_period()
        if data.period.month == 0:
            budget.update_balance()


def print_budget(budget: Budget) -> None:
    #print(texts.budget.format(data.period.get_year(), budget.get_income(), budget.get_balance(), budget.get_dept()))
    print(budget.get_budget_report())


def print_membership_satisfaction(members: Parties) -> None:
    print(texts.membership_satisfaction.format(members.get_satisfaction_pct()))


def print_hp_events(hp_events: PartiesEvents) -> None:
    ev = hp_events.get_current_events()
    if ev != "":
        print(texts.higher_power_events.format(hp_events.get_current_events()))


def setup() -> None:
    n = input(f"{texts.what_is_your_name}\n> ")
    print()
    g = utils.input_with_options(texts.what_is_your_gender, data.gender)
    data.name = Name(n, g)


def print_app_name() -> None:
    utils.print_text_in_box(texts.app_name)
