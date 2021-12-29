# coding: utf-8

ev_member_country_lu = [
    {
        "party": "LU",
        "description": "Lucemburský šéf diplomacie požaduje vyloučení Maďarska z EU kvůli přístupu k uprchlíkům.",
        "condition": {
            "flag": ["fence_hu"],
        },
        "options": [
            {
                "key": "z",
                "description": "zahájit kroky k vyloučení Maďarska z EU",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -10, "PL": -3, "SK": -1, "LU": 3},
                }
            },
            {
                "key": "k",
                "description": "udělit Maďarsku pokutu 200 000 000 EUR",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -10, "PL": -3, "SK": -1, "LU": 3},
                    "budget": 200_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout požadavek",
                "delay": -1,
                "impact": {
                    "satisfaction": {"HU": 3, "LU": -3, },
                    "budget": 200_000_000,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"LU": -1},
                }
            },
        ]
    },
    {
        "party": "LU",
        "description": "Spokojenost veřejnosti s členstvím v EU je v Lucembursku velmi nízká. Lucembursko plánuje "
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
        "party": "LU",
        "description": "Lucembursko se v referendu rozhodlo pro odchod z EU. Lucembursko přestalo být členskou zemí EU.",
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
