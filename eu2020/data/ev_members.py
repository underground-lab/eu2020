# coding: utf-8

from eu2020.data.ev_members_cz import ev_member_country_cz
from eu2020.data.ev_members_de import ev_member_country_de
from eu2020.data.ev_members_es import ev_member_country_es
from eu2020.data.ev_members_fr import ev_member_country_fr
from eu2020.data.ev_members_gr import ev_member_country_gr
from eu2020.data.ev_members_hu import ev_member_country_hu
from eu2020.data.ev_members_it import ev_member_country_it
from eu2020.data.ev_members_lu import ev_member_country_lu
from eu2020.data.ev_members_pl import ev_member_country_pl

ev_member_country = []
ev_member_country += ev_member_country_cz
ev_member_country += ev_member_country_de
ev_member_country += ev_member_country_es
ev_member_country += ev_member_country_fr
ev_member_country += ev_member_country_gr
ev_member_country += ev_member_country_hu
ev_member_country += ev_member_country_it
ev_member_country += ev_member_country_lu
ev_member_country += ev_member_country_pl


member_countries = {
    "BE": {
        "name": "Belgie",
        "satisfaction_pct": 67,
        "budget_contribution": 5_664_000_000,
        "budget_consumption": 3_664_000_000,
    },
    "BG": {
        "name": "Bulharsko",
        "satisfaction_pct": 77,
        "budget_contribution": 560_000_000,
        "budget_consumption": 1_000_000_000,
    },
    "CZ": {
        "name": "Česko",
        "satisfaction_pct": 52,
        "budget_contribution": 2_224_000_000,
        "budget_consumption": 3_000_000_000,
    },
    "DK": {
        "name": "Dánsko",
        "satisfaction_pct": 67,
        "budget_contribution": 2_224_000_000,
        "budget_consumption": 1_224_000_000,
    },
    "EE": {
        "name": "Estonsko",
        "satisfaction_pct": 67,
        "budget_contribution": 224_000_000,
        "budget_consumption": 500_000_000,
    },
    "FI": {
        "name": "Finsko",
        "satisfaction_pct": 67,
        "budget_contribution": 2_896_000_000,
        "budget_consumption": 2_000_000_000,
    },
    "FR": {
        "name": "Francie",
        "satisfaction_pct": 51,
        "budget_contribution": 32_288_000_000,
        "budget_consumption": 20_000_000_000,
    },
    "HR": {
        "name": "Chorvatsko",
        "satisfaction_pct": 67,
        "budget_contribution": 96_000_000,
        "budget_consumption": 150_000_000,
    },
    "IE": {
        "name": "Irsko",
        "satisfaction_pct": 67,
        "budget_contribution": 2_144_000_000,
        "budget_consumption": 1_500_000_000,
    },
    "IT": {
        "name": "Itálie",
        "satisfaction_pct": 58,
        "budget_contribution": 24_576_000_000,
        "budget_consumption": 20_000_000_000,
    },
    "CY": {
        "name": "Kypr",
        "satisfaction_pct": 67,
        "budget_contribution": 272_000_000,
        "budget_consumption": 500_000_000,
    },
    "LT": {
        "name": "Litva",
        "satisfaction_pct": 83,
        "budget_contribution": 432_000_000,
        "budget_consumption": 800_000_000,
    },
    "ES": {
        "name": "Španělsko",
        "satisfaction_pct": 66,
        "budget_contribution": 16_288_000_000,
        "budget_consumption": 12_000_000_000,
    },
    "SE": {
        "name": "Švédsko",
        "satisfaction_pct": 72,
        "budget_contribution": 4_528_000_000,
        "budget_consumption": 3_528_000_000,
    },
    "HU": {
        "name": "Maďarsko",
        "satisfaction_pct": 67,
        "budget_contribution": 1_568_000_000,
        "budget_consumption": 2_568_000_000,
    },
    "MT": {
        "name": "Malta",
        "satisfaction_pct": 67,
        "budget_contribution": 96_000_000,
        "budget_consumption": 70_000_000,
    },
    "DE": {
        "name": "Německo",
        "satisfaction_pct": 69,
        "budget_contribution": 35_856_000_000,
        "budget_consumption": 23_856_000_000,
    },
    "NL": {
        "name": "Nizozemsko",
        "satisfaction_pct": 66,
        "budget_contribution": 7_216_000_000,
        "budget_consumption": 6_000_000_000,
    },
    "PL": {
        "name": "Polsko",
        "satisfaction_pct": 84,
        "budget_contribution": 5_920_000_000,
        "budget_consumption": 7_920_000_000,
    },
    "PT": {
        "name": "Portugalsko",
        "satisfaction_pct": 67,
        "budget_contribution": 2_624_000_000,
        "budget_consumption": 2_000_000_000,
    },
    "AT": {
        "name": "Rakousko",
        "satisfaction_pct": 67,
        "budget_contribution": 4_240_000_000,
        "budget_consumption": 3_240_000_000,
    },
    "RO": {
        "name": "Rumunsko",
        "satisfaction_pct": 67,
        "budget_contribution": 1_984_000_000,
        "budget_consumption": 2_984_000_000,
    },
    "GR": {
        "name": "Řecko",
        "satisfaction_pct": 53,
        "budget_contribution": 3_696_000_000,
        "budget_consumption": 3_000_000_000,
    },
    "SK": {
        "name": "Slovensko",
        "satisfaction_pct": 70,
        "budget_contribution": 1_072_000_000,
        "budget_consumption": 1_800_000_000,
    },
    "SI": {
        "name": "Slovinsko",
        "satisfaction_pct": 67,
        "budget_contribution": 576_000_000,
        "budget_consumption": 1_000_000_000,
    },
    "LV": {
        "name": "Lotyšsko",
        "satisfaction_pct": 67,
        "budget_contribution": 272_000_000,
        "budget_consumption": 500_000_000,
    },
    "LU": {
        "name": "Lucembursko",
        "satisfaction_pct": 67,
        "budget_contribution": 464_000_000,
        "budget_consumption": 380_000_000,
    },
}
