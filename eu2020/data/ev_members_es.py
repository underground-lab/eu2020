# coding: utf-8

ev_member_country_es = [
    {
        "party": "ES",
        "description": "Španělsko požaduje záruku za vydané státní dluhopisy ve výši 10 000 000 000 EUR.",
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "delay": 12,
                "impact": {
                    "satisfaction": {"ES": 5},
                    "guarantee": 10_000_000_000
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
                "delay": 2,
                "impact": {
                    "satisfaction": {"ES": -5},
                }
            },
        ]
    },
    {
        "party": "ES",
        "description": "Spokojenost veřejnosti s členstvím v EU je ve Španělsku velmi nízká. Španělsko plánuje "
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
        "party": "ES",
        "description": "Španělé se v referendu rozhodli pro odchod z EU. Španělsko přestalo být členskou zemí EU.",
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
