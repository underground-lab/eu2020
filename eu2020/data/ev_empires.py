# coding: utf-8

from eu2020.common.utils import auto_set_option_keys
from eu2020.data.ev_empires_ru import ev_empires_ru

ev_empires = [
    *ev_empires_ru,
]

auto_set_option_keys(ev_empires)

empires = {
    "RU": {
        "name": "Rusko",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 0,
    },
    "CN": {
        "name": "Čína",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 0,
    },
    "US": {
        "name": "USA",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 0,
    },
}
