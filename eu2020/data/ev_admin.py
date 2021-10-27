# coding: utf-8

from eu2020.data.ev_admin_ek import ev_admin_ek

ev_admin = []
ev_admin += ev_admin_ek

eu_administration = {
    "EK": {
        "name": "Evropská komise",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 3_000_000_000,
    },
    "ER": {
        "name": "Rada Evropy",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 0,
    },
    "EP": {
        "name": "Evropský parlament",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 10_000_000_000,
    },
    "AD": {
        "name": "Administrativa",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 5_000_000_000,
    },
    "PR": {
        "name": "EU Propagace",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 5_000_000_000,
    },
    "ED": {
        "name": "Evropská obranná Agentura",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 5_000_000_000,
    },
}
