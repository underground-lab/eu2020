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
