import eu2020.data.colors as colors
import eu2020.data.ev_admin as ead
import eu2020.data.ev_deep_state as eds
import eu2020.data.ev_members as ems
import eu2020.data.ev_others as eot
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
from eu2020.data.ev_higher_power import ev_higher_power
from eu2020 import console


def main() -> None:
    flags = set()

    eu_members = Parties(ems.member_countries)
    eu_admin = Parties(ead.eu_administration)
    deep_state = Parties(eds.deep_state)
    others = Parties(eot.deep_others)

    high_power_events = HigherPowerEvents(ev_higher_power, flags)
    eu_members_events = PartiesEvents(ems.ev_member_country, eu_members, flags)
    eu_admin_events = PartiesEvents(ead.ev_admin, eu_admin, flags)
    deep_events = PartiesEvents(eds.ev_deep_state, deep_state, flags)
    others_events = PartiesEvents(eot.ev_others, others, flags)

    event_processor = EventProcessor(flags)
    event_processor.add_events(eu_members_events)
    event_processor.add_events(eu_admin_events)
    event_processor.add_events(deep_events)
    event_processor.add_events(others_events)

    budget = Budget()
    budget.add_parties(eu_members)
    budget.add_parties(eu_admin)
    budget.add_parties(deep_state)

    data.period = Period(2020, 0)

    utils.clear()
    print_app_name()

    setup()
    print(texts.intro.format(data.name.get_name5p(), data.name.translate("stal"), len(ems.member_countries)))
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
        if hpe is not None:
            utils.print_text_in_box(texts.higher_power_event, "!")
            print(hpe + "\n")
            utils.proceed()

        utils.print_text_in_box(texts.membership_satisfaction_header)
        console.print(eu_members.get_detailed_satisfaction_report())
        utils.proceed()

        utils.print_text_in_box(texts.deep_state_satisfaction_header)
        console.print(deep_state.get_detailed_satisfaction_report())
        utils.proceed()

        data.period.next()
        event_processor.next_period()
        if data.period.month == 0:
            budget.update_balance()


def print_budget(budget: Budget) -> None:
    console.print(budget.get_budget_report())


def print_membership_satisfaction(members: Parties) -> None:
    console.print(texts.membership_satisfaction.format(colors.numbers, members.get_satisfaction_pct(), colors.numbers))


def print_hp_events(hp_events: HigherPowerEvents) -> None:
    ev = hp_events.get_current_events()
    if ev != "":
        console.print()
        console.print(texts.higher_power_events.format(colors.high_power_events, ev, colors.high_power_events))


def setup() -> None:
    n = console.input(f"{texts.what_is_your_name}\n{texts.cursor}")
    print()
    g = utils.input_with_options(texts.what_is_your_gender, data.gender)
    data.name = Name(n, g)


def print_app_name() -> None:
    utils.print_text_in_box(texts.app_name)
