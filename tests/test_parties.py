import pytest

from eu2020.common.parties import Parties


@pytest.fixture
def parties():
    data = {
        "EP": {
            "name": "Evropský parlament",
            "satisfaction_pct": 48,
            "budget_contribution": 0,
            "budget_consumption": 9_900_000_000,
        },
        "CZ": {
            "name": "Česko",
            "satisfaction_pct": 64,
            "budget_contribution": 2_345_000_001,
            "budget_consumption": 3_456_000_001,
        },
        "DK": {
            "name": "Dánsko",
            "satisfaction_pct": 57,
            "budget_contribution": 2_001_000_000,
            "budget_consumption": 888_000_099,
        },
        "IE": {
            "name": "Irsko",
            "satisfaction_pct": 72,
            "budget_contribution": 2_222_000_001,
            "budget_consumption": 1_555_000_001,
        },
        "CN": {
            "name": "Čína",
            "satisfaction_pct": 67,
            "budget_contribution": 0,
            "budget_consumption": 0,
        },
    }

    return Parties(data)


@pytest.fixture
def satisfaction_change():
    return {"CZ": -2, "DK": -3, "CN": -70, "IE": 2}


def test_get_satisfaction_pct(parties):
    result = parties.get_satisfaction_pct()
    assert result == pytest.approx((48 + 64 + 57 + 72 + 67) / 5)


def test_get_detailed_satisfaction_report(parties):
    result = parties.get_detailed_satisfaction_report()
    assert result == (
        "Evropský parlament   [magenta]48.00 %[/magenta]\n"
        "Česko                [magenta]64.00 %[/magenta]\n"
        "Dánsko               [magenta]57.00 %[/magenta]\n"
        "Irsko                [magenta]72.00 %[/magenta]\n"
        "Čína                 [magenta]67.00 %[/magenta]\n"
    )


def test_get_detailed_satisfaction_report_with_diff(parties, satisfaction_change):
    parties.update_satisfaction(satisfaction_change)
    result = parties.get_detailed_satisfaction_report()
    assert result == (
        "Evropský parlament   [magenta]48.00 %[/magenta]\n"
        "Česko                [magenta]62.00 %[/magenta]  ([red]-2.00 %[/red])\n"
        "Dánsko               [magenta]54.00 %[/magenta]  ([red]-3.00 %[/red])\n"
        "Irsko                [magenta]74.00 %[/magenta]  ([green]+2.00 %[/green])\n"
        "Čína                 [magenta]0.00 %[/magenta]  ([red]-67.00 %[/red])\n"
    )


def test_update_satisfaction(parties, satisfaction_change):
    parties.update_satisfaction(satisfaction_change)
    assert parties.parties["EP"]["satisfaction_pct"] == 48
    assert parties.parties["CZ"]["satisfaction_pct"] == 62
    assert parties.parties["DK"]["satisfaction_pct"] == 54
    assert parties.parties["IE"]["satisfaction_pct"] == 74
    assert parties.parties["CN"]["satisfaction_pct"] == 0


def test_get_budget_contribution(parties):
    result = parties.get_budget_contribution()
    assert result == 2_345_000_001 + 2_001_000_000 + 2_222_000_001


def test_get_budget_consumption(parties):
    result = parties.get_budget_consumption()
    assert result == 9_900_000_000 + 3_456_000_001 + 888_000_099 + 1_555_000_001
