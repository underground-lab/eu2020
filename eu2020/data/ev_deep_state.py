# coding: utf-8

from eu2020.data.ev_deep_state_nbm import ev_deep_state_nbm
from eu2020.data.ev_deep_state_nez import ev_deep_state_nez
from eu2020.data.ev_deep_state_sor import ev_deep_state_sor
from eu2020.data.ev_deep_state_who import ev_deep_state_who

ev_deep_state = []
ev_deep_state += ev_deep_state_nbm
ev_deep_state += ev_deep_state_nez
ev_deep_state += ev_deep_state_sor
ev_deep_state += ev_deep_state_who

deep_state = {
    "GDA": {
        "name": "Globalisti z Davosu",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 0,
    },
    "SOR": {
        "name": "George Soros",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 0,
    },
    "NBM": {
        "name": "Nadace Billa a Melindy Gatesových",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 0,
    },
    "NEZ": {
        "name": "Neziskové organizace",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 4_816_000_000,
    },
    "WHO": {
        "name": "Světová Zdravotnická Organizace",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 2_000_000_000,
    },
    "BIT": {
        "name": "Big Tech Korporace",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 0,
    },
    "BIP": {
        "name": "Big Pharma Korporace",
        "satisfaction_pct": 50,
        "budget_contribution": 0,
        "budget_consumption": 0,
    },
}
