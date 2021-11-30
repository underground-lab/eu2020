# coding: utf-8

import pytest

from eu2020.common.budget import Budget
from eu2020.common.parties import Parties


@pytest.fixture
def parties_non_eu():
    data = {
        "CN": {
            "name": "Čína",
            "satisfaction_pct": 42,
            "budget_contribution": 0,
            "budget_consumption": 0,
        },
        "US": {
            "name": "USA",
            "satisfaction_pct": 68,
            "budget_contribution": 0,
            "budget_consumption": 0,
        },
    }

    return Parties(data)


@pytest.fixture
def budget(parties, parties_non_eu):
    b = Budget()
    b.add_parties(parties)
    b.add_parties(parties_non_eu)
    return b


def test_get_income(budget):
    result = budget.get_income()
    assert result == 2_345_000_001 + 2_001_000_000 + 2_222_000_001


def test_get_outcome(budget):
    result = budget.get_outcome()
    assert result == 3_456_000_001 + 888_000_099 + 1_555_000_001


def test_budget():
    budget = Budget()
    budget.add_extra_income(500_000_000)
    budget.add_extra_income(500_000_000)
    budget.add_extra_outcome(200_000_000)
    budget.add_extra_outcome(200_000_000)
    budget.add_guarantee(5_000_000_000)
    budget.add_guarantee(5_000_000_000)
    assert 1_000_000_000 == budget.get_extra_income()
    assert 400_000_000 == budget.get_extra_outcome()
    assert 600_000_000 == budget.get_balance()
    assert 10_000_000_000 == budget.get_guarantee()
    assert 0 == budget.get_dept()

    budget.update_balance()
    assert 0 == budget.get_extra_income()
    assert 0 == budget.get_extra_outcome()
    assert 5_000_000_000 == budget.get_guarantee()
    assert -600_000_000 + 2_500_000_000 == budget.get_dept()
    assert 600_000_000 - 2_500_000_000 == budget.get_balance()
    budget.add_extra_income(500_000_000)
    budget.add_extra_outcome(200_000_000)

    budget.update_balance()
    assert 0 == budget.get_extra_income()
    assert 0 == budget.get_extra_outcome()
    assert 2_500_000_000 == budget.get_guarantee()
    assert -900_000_000 + 2_500_000_000 + 1_250_000_000 == budget.get_dept()
    assert 900_000_000 - 2_500_000_000 - 1_250_000_000 == budget.get_balance()


def test_get_budget_report():
    budget = Budget()
    budget.add_parties(Parties({
        "XY": {"budget_contribution": 800_000_000, "budget_consumption": 800_000_000}
    }))
    assert budget.get_budget_report() == (
        "Příjmy:                  [magenta]         800,000,000 EUR[/magenta]\n"
        "Výdaje:                  [magenta]         800,000,000 EUR[/magenta]\n"
        "Mimořádné příjmy:        [magenta]                   0 EUR[/magenta]\n"
        "Mimořádné výdaje:        [magenta]                   0 EUR[/magenta]\n"
        "Dluh z minulých období:  [magenta]                   0 EUR[/magenta]\n"

        # default color
        "Bilance:                 [magenta]                   0 EUR[/magenta]\n"
        "Poskytnuté garance:      [magenta]                   0 EUR[/magenta]\n"
    )

    budget.add_extra_income(1_400_000_000)
    assert budget.get_budget_report() == (
        "Příjmy:                  [magenta]         800,000,000 EUR[/magenta]\n"
        "Výdaje:                  [magenta]         800,000,000 EUR[/magenta]\n"
        "Mimořádné příjmy:        [magenta]       1,400,000,000 EUR[/magenta]\n"
        "Mimořádné výdaje:        [magenta]                   0 EUR[/magenta]\n"
        "Dluh z minulých období:  [magenta]                   0 EUR[/magenta]\n"

        # positive progress color
        "Bilance:                 [green]      +1,400,000,000 EUR[/green]\n"
        "Poskytnuté garance:      [magenta]                   0 EUR[/magenta]\n"
    )

    budget.add_extra_outcome(2_900_000_000)
    assert budget.get_budget_report() == (
        "Příjmy:                  [magenta]         800,000,000 EUR[/magenta]\n"
        "Výdaje:                  [magenta]         800,000,000 EUR[/magenta]\n"
        "Mimořádné příjmy:        [magenta]       1,400,000,000 EUR[/magenta]\n"
        "Mimořádné výdaje:        [magenta]       2,900,000,000 EUR[/magenta]\n"
        "Dluh z minulých období:  [magenta]                   0 EUR[/magenta]\n"

        # negative progress color
        "Bilance:                 [red]      -1,500,000,000 EUR[/red]\n"
        "Poskytnuté garance:      [magenta]                   0 EUR[/magenta]\n"
    )
