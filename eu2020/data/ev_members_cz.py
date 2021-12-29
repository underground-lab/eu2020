# coding: utf-8

ev_member_country_cz = [
    {
        "party": "CZ",
        "description": "České opoziční strany požadují deklaraci proti střetu zájmů českého premiéra.",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -3, "SK": -1},
                }
            },
            {
                "key": "o",
                "description": "odmítnout deklaraci",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": 1, "HU": 1, "PL": 1, "SK": 1},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                }
            },
        ]
    },
    {
        "party": "CZ",
        "description": "Spokojenost veřejnosti s členstvím v EU je v Česku velmi nízká. Česko plánuje "
                       "referendum o vystoupení z EU.",
        "condition": {
            "satisfaction": {"op": "<", "value": 30},
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
                "impact": {
                    "satisfaction": {"WEF": -5, "SOR": -5, "NEZ": -5},
                }
            },
        ]
    },
    {
        "party": "CZ",
        "description": "Češi se v referendu rozhodli pro odchod z EU. Česko přestalo být členskou zemí EU.",
        "condition": {
            "satisfaction": {"op": "<", "value": 10},
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
                "operation": {"cmd": "remove_from_party", "party": "EU_MEMBERS"},
                "impact": {
                    "satisfaction": {"WEF": -5, "SOR": -5, "NEZ": -5},
                }
            },
        ]
    },
]
