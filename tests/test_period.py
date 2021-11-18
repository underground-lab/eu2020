# coding: utf-8

import pytest
from eu2020.common.period import Period


@pytest.fixture(scope="module")
def period():
    period = Period(2020, 0)
    return period


@pytest.mark.parametrize(
    'year, month',
    (
        (2020, "Leden"),
        (2020, "Únor"),
        (2020, "Březen"),
        (2020, "Duben"),
        (2020, "Květen"),
        (2020, "Červen"),
        (2020, "Červenec"),
        (2020, "Srpen"),
        (2020, "Září"),
        (2020, "Říjen"),
        (2020, "Listopad"),
        (2020, "Prosinec"),
        (2021, "Leden"),
    )
)
def test_next(period, year, month):
    assert year == period.get_year()
    assert month == period.get_month()
    period.next()
