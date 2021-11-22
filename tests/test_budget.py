# coding: utf-8

from eu2020.common.budget import Budget


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
