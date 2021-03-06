# coding: utf-8

ev_member_country_de = [
    {
        "party": "DE",
        "description": "Němečtí Zelení chtějí prosadit uzavření všech fosilních elektráren v EU.",
        "condition": {
            "flag": ["local_energy_distributors"]
        },
        "options": [
            {
                "description": "přijmout rozhodnutí o uzavření fosilních elektráren",
                "delay": -1,
                "flag_set": "coal_power_stations_closure",
                "impact": {
                    "satisfaction": {
                        "BE": -1, "BG": -1, "CZ": -3, "DK": -1, "EE": -2, "FI": -2, "FR": -2, "HR": -1, "IE": -1, "IT": -2,
                        "CY": -1, "LT": -2, "ES": -2, "SE": -2, "HU": -3, "MT": -1, "DE": +2, "NL": -2, "PL": -3, "PT": -1,
                        "AT": -2, "RO": -3, "GR": -1, "SK": -3, "SI": -2, "LV": -2, "LU": -2,
                    },
                }
            },
            {
                "description": "odmítnout rozhodnutí o uzavření fosilních elektráren",
                "delay": 12,
                "impact": {
                    "satisfaction": {"DE": -5, },
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 2,
            },
        ]
    },
    {
        "party": "DE",
        "description": "Německo požaduje mimořádnou pomoc ve výši 500 000 000 EUR na zvládnutí povodní.",
        "condition": {
            "flag": ["floods_de"],
        },
        "options": [
            {
                "description": "poskytnout pomoc",
                "delay": 12,
                "impact": {
                    "satisfaction": {"GR": 2},
                    "budget": -500_000_000,
                }
            },
            {
                "description": "neposkytnout pomoc",
                "delay": 3,
                "impact": {
                    "satisfaction": {"GR": -5},
                }
            },
        ]
    },
    {
        "party": "DE",
        "description": "Spokojenost veřejnosti s členstvím v EU je v Německu velmi nízká. Německo plánuje "
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
        "party": "DE",
        "description": "Němci se v referendu rozhodli pro odchod z EU. Německo přestalo být členskou zemí EU.",
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
