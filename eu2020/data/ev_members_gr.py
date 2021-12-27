# coding: utf-8

ev_member_country_gr = [
    {
        "party": "GR",
        "description": "Řecko se potýká s náporem uprchlíků přicházejících z Turecka a požaduje přijmutí urychleného plánu"
                       " na přerozdělování uprchlíků v Evropě.",
        "options": [
            {
                "description": "přijmout urychleně plán pro spravedlivé přerozdělování uprchlíků",
                "delay": -1,
                "flag_set": "refugee_distribution",
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -3, "SK": -1, "AT": -3, "GR": 5, "IT": 4, "ES": 4},
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"GR": -5},
                }
            },
        ]
    },
    {
        "party": "GR",
        "description": "Řecko požaduje záruku za vydané státní dluhopisy ve výši 5 000 000 000 EUR.",
        "options": [
            {
                "description": "přijmout záruku",
                "delay": 12,
                "impact": {
                    "satisfaction": {"GR": 5},
                    "guarantee": 5_000_000_000
                }
            },
            {
                "description": "nepřijmout záruku",
                "delay": 2,
                "impact": {
                    "satisfaction": {"GR": -5},
                }
            },
        ]
    },
    {
        "party": "GR",
        "description": "Řecko požaduje mimořádnou pomoc ve výši 500 000 000 EUR na zvládnutí lesních požárů.",
        "condition": {
            "flag": ["fires_gr"],
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
        "party": "GR",
        "description": "Řecko zaznamenává masivní vlny přílivu uprchlíků přes Středozemní moře. Požaduje uzavření dohody"
                       " s Tureckem a zaplacení 6 mld EUR aby zadržovalo uprchlíky.",
        "options": [
            {
                "description": "uzavřít dohodu a zaplatit Turecku 6 mld EUR aby zadržovalo uprchlíky",
                "delay": -1,
                "flag_set": "turkey_refugee_agreement",
                "impact": {
                    "satisfaction": {
                        "BE": -1, "BG": -1, "CZ": -2, "DK": -1, "EE": -2, "FI": -2, "FR": 2, "HR": 1, "IT": 2, "CY": -10,
                        "LT": -2, "ES": -2, "SE": -2, "HU": -2, "MT": 1, "DE": -1, "NL": -2, "PL": -2, "PT": -1, "AT": -2,
                        "RO": -3, "GR": 5, "SK": 1, "LV": -2, "LU": -2,
                    },
                    "budget": -6_000_000_000,
                }
            },
            {
                "description": "odmítnout uzavření dohody s Tureckem",
                "delay": 12,
                "impact": {
                    "satisfaction": {"GR": -5, "CY": 3},
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
        "party": "GR",
        "description": "Spokojenost veřejnosti s členstvím v EU je v Řecku velmi nízká. Řecko plánuje "
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
        "party": "GR",
        "description": "Řekové se v referendu rozhodli pro odchod z EU. Řecko přestalo být členskou zemí EU.",
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
