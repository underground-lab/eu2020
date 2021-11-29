# coding: utf-8

import pytest


@pytest.fixture
def satisfaction_change():
    return {"CZ": -2, "IE": 3}


def test_get_satisfaction_pct(parties):
    result = parties.get_satisfaction_pct()
    assert result == pytest.approx((64 + 57 + 72) / 3)


def test_get_detailed_satisfaction_report(parties):
    result = parties.get_detailed_satisfaction_report()
    assert result == (
        "Česko    [magenta]64.00 %[/magenta]\n"
        "Dánsko   [magenta]57.00 %[/magenta]\n"
        "Irsko    [magenta]72.00 %[/magenta]\n"
    )


def test_get_detailed_satisfaction_report_with_diff(parties, satisfaction_change):
    parties.update_satisfaction(satisfaction_change)
    result = parties.get_detailed_satisfaction_report()
    assert result == (
        "Česko    [magenta]62.00 %[/magenta]  ([red]-2.00 %[/red])\n"
        "Dánsko   [magenta]57.00 %[/magenta]\n"  # unaffected party, no change
        "Irsko    [magenta]75.00 %[/magenta]  ([green]+3.00 %[/green])\n"
    )


def test_update_satisfaction(parties, satisfaction_change):
    parties.update_satisfaction(satisfaction_change)
    assert parties.parties["CZ"]["satisfaction_pct"] == 62
    assert parties.parties["IE"]["satisfaction_pct"] == 75

    # unaffected party, no change
    assert parties.parties["DK"]["satisfaction_pct"] == 57


def test_update_satisfaction_does_not_exceed_limits(parties):
    parties.update_satisfaction({"CZ": -70, "DK": 50})
    assert parties.parties["CZ"]["satisfaction_pct"] == 0  # must not be < 0
    assert parties.parties["DK"]["satisfaction_pct"] == 100  # must not be > 100

    # unaffected party, no change
    assert parties.parties["IE"]["satisfaction_pct"] == 72


def test_get_budget_contribution(parties):
    result = parties.get_budget_contribution()
    assert result == 2_345_000_001 + 2_001_000_000 + 2_222_000_001


def test_get_budget_consumption(parties):
    result = parties.get_budget_consumption()
    assert result == 3_456_000_001 + 888_000_099 + 1_555_000_001
