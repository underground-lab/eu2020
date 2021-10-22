import pytest

from eu2020.common.parties import Parties


@pytest.mark.parametrize(
    'parties_data, expected',
    (
        ({"X": {"satisfaction_pct": 68}}, 68),
        (
            {
                "A": {"satisfaction_pct": 46},
                "B": {"satisfaction_pct": 57},
                "C": {"satisfaction_pct": 67},
            },
            56.67
        ),
    )
)
def test_average_satisfaction(parties_data, expected):
    parties = Parties(parties_data)
    average = parties.get_satisfaction_pct()
    assert round(average, 2) == expected
