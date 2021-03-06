# coding: utf-8

ev_member_country_fr = [
    {
        "party": "FR",
        "description": "Francie požaduje záruku za vydané státní dluhopisy ve výši 20 000 000 000 EUR.",
        "options": [
            {
                "description": "přijmout záruku",
                "delay": 12,
                "impact": {
                    "satisfaction": {"FR": 5},
                    "guarantee": 20_000_000_000
                }
            },
            {
                "description": "nepřijmout záruku",
                "delay": 3,
                "impact": {
                    "satisfaction": {"FR": -5},
                }
            },
        ]
    },
    {
        "party": "FR",
        "description": "Spokojenost veřejnosti s členstvím v EU je ve Francii velmi nízká. Francie plánuje "
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
        "party": "FR",
        "description": "Francouzi se v referendu rozhodli pro odchod z EU. Francie přestala být členskou zemí EU.",
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
