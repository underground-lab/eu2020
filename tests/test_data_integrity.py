from collections import Counter
from itertools import chain

from jsonschema import validate
import pytest

from eu2020.common.utils import auto_set_option_keys
from eu2020.data.ev_admin import ev_admin, eu_administration
from eu2020.data.ev_deep_state import ev_deep_state, deep_state
from eu2020.data.ev_higher_power import ev_higher_power
from eu2020.data.ev_members import ev_member_country, member_countries
from eu2020.data.ev_empires import ev_empires, empires
from eu2020.data.ev_story import ev_story

EVENTS = tuple(chain(ev_admin, ev_deep_state, ev_member_country, ev_empires, ev_story))
for event in EVENTS:
    auto_set_option_keys(event)

PARTY_CODES = tuple(chain(eu_administration, deep_state, member_countries, empires))


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


def test_ev_empires_all_parties_exists():
    for event in ev_empires:
        assert "party" in event
        assert event["party"] in empires


def test_ev_story_all_parties_exists():
    for event in ev_story:
        assert "party" in event
        assert event["party"] in PARTY_CODES


@pytest.fixture
def required_flags():
    flags = set()
    for event in EVENTS:
        flags.update(event.get("condition", {}).get("flag", []))
    return flags


@pytest.fixture
def provided_flags():
    flags = set()
    for event in EVENTS:
        for option in event.get("options", []):
            if "flag_set" in option:
                flags.add(option["flag_set"])
    return flags


@pytest.fixture
def higher_power_flags():
    return set(event["key"] for event in ev_higher_power)


def test_all_required_flags_are_provided(required_flags, provided_flags, higher_power_flags):
    # some events depend on higher power flags
    diff = required_flags - (provided_flags | higher_power_flags)
    assert not diff, f"not provided in data: {', '.join(diff)}"


def test_all_provided_flags_are_required(required_flags, provided_flags):
    diff = provided_flags - required_flags
    assert not diff, f"not required in data: {', '.join(diff)}"


def test_all_higher_power_flags_are_required(required_flags, provided_flags, higher_power_flags):
    diff = higher_power_flags - required_flags
    assert not diff, f"not required in data: {', '.join(diff)}"


def test_unique_party_codes():
    code_counts = Counter(PARTY_CODES)
    duplicate = [code for code, count in code_counts.items() if count > 1]
    assert not duplicate, f"duplicate codes: {', '.join(duplicate)}"


def test_satisfaction_impact_all_parties_exists():
    for event in EVENTS:
        for option in event["options"]:
            if "impact" in option:
                for code in option["impact"].get("satisfaction", {}):
                    assert code in PARTY_CODES, f"unknown code: {code}"


def test_all_event_options_have_lowercase_single_letter_keys():
    for event in EVENTS:
        for option in event["options"]:
            assert option["key"].islower()
            assert len(option["key"]) == 1


def test_options_of_one_event_have_unique_keys():
    for event in EVENTS:
        keys = [option["key"] for option in event["options"]]
        assert len(keys) == len(set(keys))


EVENT_SCHEMA = {
    "type": "object",
    "properties": {
        "party": {"type": "string"},
        "description": {"type": "string"},
        "condition": {
            "type": "object",
            "properties": {
                "flag": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 1,
                    "uniqueItems": True,
                },
                "satisfaction": {
                    "type": "object",
                    "properties": {
                        "op": {"type": "string"},
                        "value": {"type": "integer"},
                    },
                    "required": ["op", "value"],
                    "additionalProperties": False,
                },
            },
            "minProperties": 1,
            "additionalProperties": False,
        },
        "options": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "key": {"type": "string"},
                    "description": {"type": "string"},
                    "delay": {"type": "integer"},
                    "flag_set": {"type": "string"},
                    "operation": {
                        "type": "object",
                        "properties": {
                            "cmd": {"type": "string"},
                            "party": {"type": "string"},
                        },
                        "required": ["cmd", "party"],
                        "additionalProperties": False,
                    },
                    "impact": {
                        "type": "object",
                        "properties": {
                            "satisfaction": {
                                "type": "object",
                                "properties": {
                                    code: {"type": "integer"} for code in PARTY_CODES
                                },
                                "minProperties": 1,
                                "additionalProperties": False,
                            },
                            "budget": {"type": "integer"},
                            "guarantee": {"type": "integer"},
                        },
                        "minProperties": 1,
                        "additionalProperties": False,
                    },
                },
                "required": ["key", "description", "delay"],
                "additionalProperties": False,
            },
            "minItems": 1,
            "uniqueItems": True,
        },
    },
    "required": ["party", "description", "options"],
    "additionalProperties": False,
}


def test_all_events_have_valid_schema():
    for event in EVENTS:
        validate(event, schema=EVENT_SCHEMA)
