from eu2020.common.budget import Budget


def test_budget():
    budget = Budget()
    budget.add_extra_income(500_000_000)
    budget.add_extra_income(500_000_000)
    budget.add_extra_outcome(200_000_000)
    budget.add_extra_outcome(200_000_000)
    assert 1_000_000_000 == budget.get_extra_income()
    assert 400_000_000 == budget.get_extra_outcome()
    assert 600_000_000 == budget.get_balance()
    assert 0 == budget.get_dept()
    budget.update_balance()
    assert 0 == budget.get_extra_income()
    assert 0 == budget.get_extra_outcome()
    assert 600_000_000 == budget.get_balance()
    assert -600_000_000 == budget.get_dept()
