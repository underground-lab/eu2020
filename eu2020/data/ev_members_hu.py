# coding: utf-8

ev_member_country_hu = [
    {
        "party": "HU",
        "description": "Maďarsko zakázalo propagaci LGBT ve školách. LGBT aktivisté požadují odsoudit Maďarsko za porušování"
                       " práv menšin.",
        "options": [
            {
                "description": "přijmout deklaraci a odsoudit Maďarsko za porušování práv menšin LGBT",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -8, "PL": -3, "SK": -1},
                }
            },
            {
                "key": "k",
                "description": "udělit pokutu 200 000 000 EUR",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -8, "PL": -3, "SK": -1},
                    "budget": 200_000_000,
                }
            },
            {
                "description": "odmítnout deklaraci",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": 3, "HU": 8, "PL": 3, "SK": 1},
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                }
            },
        ]
    },
    {
        "party": "HU",
        "description": "Maďarsko postavilo plot proti uprchlíkům přicházejícím ze Srbska a Chorvatska. "
                       "Lidskoprávní organizace požadují okamžité odstranění plotu.",
        "condition": {
            "flag": ["turkey_refugee_agreement"],
        },
        "options": [
            {
                "key": "o",
                "description": "nařídit Maďarsku odstranění plotu",
                "delay": -1,
                "flag_set": "fence_hu",
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -8, "PL": -3, "SK": -1, "NEZ": 3, "SOR": 3},
                }
            },
            {
                "key": "s",
                "description": "odsouhlasit plot jako zlepšení ochrany vnějších hranic EU",
                "delay": -1,
                "flag_set": "fence_hu",
                "impact": {
                    "satisfaction": {"CZ": 3, "HU": 8, "PL": 3, "SK": 1, "NEZ": -5, "SOR": -5},
                    "budget": 200_000_000,
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                }
            },
        ]
    },
    {
        "party": "HU",
        "description": "Spokojenost veřejnosti s členstvím v EU je v Maďarsku velmi nízká. Maďarsko plánuje "
                       "referendum o vystoupení z EU.",
        "condition": {
            "satisfaction": {"op": "<", "value": 30},
        },
        "options": [
            {
                "description": "vzít na vědomí",
                "delay": -1,
                "impact": {
                    "satisfaction": {"WEF": -5, "SOR": -5, "NEZ": -5},
                }
            },
        ]
    },
    {
        "party": "HU",
        "description": "Maďaři se v referendu rozhodli pro odchod z EU. Maďarsko přestalo být členskou zemí EU.",
        "condition": {
            "satisfaction": {"op": "<", "value": 10},
        },
        "options": [
            {
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
