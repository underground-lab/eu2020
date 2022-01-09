# coding: utf-8

ev_member_country_pl = [
    {
        "party": "PL",
        "description": "Polsko zavádí zóny bez LGBT. Aktivisté požadují přísné potrestání Polska.",
        "options": [
            {
                "description": "přijmout deklaraci a odsoudit Polsko",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -10, "SK": -1},
                }
            },
            {
                "description": "udělit pokutu 200 000 000 EUR",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -10, "SK": -1},
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
        "party": "PL",
        "description": "Polsko udělalo krok k odchodu z Evropské unie. Ústavní soud rozhodl, že polské právo "
                       "je nadřazené unijnímu. Postavení ústav a jejich ustanovení jsou předmětem vášnivé debaty "
                       "v právnické komunitě v celé Evropské unii.",
        "options": [
            {
                "description": "udělit pokutu 200 000 000 EUR a zahájit kroky k vyloučení Polska z EU",
                "delay": -1,
                "impact": {
                    "satisfaction": {"PL": -5},
                    "budget": 200_000_000,
                }
            },
            {
                "description": "přijmout deklaraci proti Polsku a udělit pokutu 200 000 000 EUR",
                "delay": -1,
                "impact": {
                    "satisfaction": {"PL": -5},
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
        "party": "PL",
        "description": "Spokojenost veřejnosti s členstvím v EU je v Polsku velmi nízká. Polsko plánuje "
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
        "party": "PL",
        "description": "Poláci se v referendu rozhodli pro odchod z EU. Polsko přestalo být členskou zemí EU.",
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
