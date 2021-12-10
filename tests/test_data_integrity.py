from itertools import chain

import pytest

from eu2020.data.ev_admin import ev_admin, eu_administration
from eu2020.data.ev_deep_state import ev_deep_state, deep_state
from eu2020.data.ev_higher_power import ev_higher_power
from eu2020.data.ev_members import ev_member_country, member_countries
from eu2020.data.ev_others import ev_others, deep_others


def test_ev_admin_all_parties_exists():
    for event in ev_admin:
        assert "party" in event
        assert event["party"] in eu_administration


def test_ev_deep_state_all_parties_exists():
    for event in ev_deep_state:
        assert "party" in event
        assert event["party"] in deep_state


def test_ev_members_country_all_parties_exists():
    for event in ev_member_country:
        assert "party" in event
        assert event["party"] in member_countries


def test_ev_others_all_parties_exists():
    for event in ev_others:
        assert "party" in event
        assert event["party"] in deep_others


@pytest.fixture
def required_flags():
    flags = set()
    for event in chain(ev_admin, ev_deep_state, ev_member_country, ev_others):
        flags.update(event.get("condition", {}).get("flag", []))
    return flags


@pytest.fixture
def provided_flags():
    flags = set()
    for event in chain(ev_admin, ev_deep_state, ev_member_country, ev_others):
        for option in event.get("options", []):
            if "flag_set" in option:
                flags.add(option["flag_set"])
    return flags


@pytest.fixture
def higher_power_flags():
    return set(event["key"] for event in ev_higher_power)


def test_all_required_flags_are_provided(required_flags, provided_flags, higher_power_flags):
    # some events depend on higher power flags
    assert required_flags.issubset(provided_flags | higher_power_flags)


def test_all_provided_flags_are_required(required_flags, provided_flags):
    assert provided_flags.issubset(required_flags)


def test_all_higher_power_flags_are_required(required_flags, provided_flags, higher_power_flags):
    assert higher_power_flags.issubset(required_flags)
