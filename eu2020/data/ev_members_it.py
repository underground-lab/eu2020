# coding: utf-8

ev_member_country_it = [
    {
        "party": "IT",
        "description": "Itálie požaduje záruku za vydané státní dluhopisy ve výši 10 000 000 000 EUR.",
        "options": [
            {
                "description": "přijmout záruku",
                "delay": 12,
                "impact": {
                    "satisfaction": {"IT": 5},
                    "guarantee": 10_000_000_000
                }
            },
            {
                "description": "nepřijmout záruku",
                "delay": 3,
                "impact": {
                    "satisfaction": {"IT": -5},
                }
            },
        ]
    },
    {
        "party": "IT",
        "description": "V Itálii hrozí bankrot některých významných bank. Pokud by se tak stalo, znamenalo by to "
                       "nebezpečnou destabilizaci, která by mohla vyústit v odchod země z EU. Itálie proto požaduje "
                       "mimořádnou dotaci na sanaci bank ve výši 12 000 000 000 EUR.",
        "options": [
            {
                "description": "poskytnout mimořádnou dotaci ve výši 12 000 000 000 EUR",
                "delay": 24,
                "impact": {
                    "satisfaction": {"IT": 5},
                    "budget": -12_000_000_000
                }
            },
            {
                "description": "odmítnout poskytnutí dotace na sanaci italských bank",
                "delay": 3,
                "impact": {
                    "satisfaction": {"IT": -5},
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"IT": -1},
                }
            },
        ]
    },
    {
        "party": "IT",
        "description": "Spokojenost veřejnosti s členstvím v EU je v Itálii velmi nízká. Itálie plánuje "
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
        "party": "IT",
        "description": "Italové se v referendu rozhodli pro odchod z EU. Itálie přestala být členskou zemí EU.",
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
