# coding: utf-8

ev_member_country_sk = [
    {
        "party": "SK",
        "description": "Spokojenost veřejnosti s členstvím v EU je na Slovensku velmi nízká. Slovensko plánuje "
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
        "party": "SK",
        "description": "Slováci se v referendu rozhodli pro odchod z EU. Slovensko přestalo být členskou zemí EU.",
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
