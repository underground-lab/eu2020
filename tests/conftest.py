import pytest

from eu2020.common.parties import Parties


@pytest.fixture
def parties():
    data = {
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
    }

    return Parties(data)
