# coding: utf-8

ev_member_country_gr = [
    {
        "party": "GR",
        "description": "Řecko se potýká s náporem uprchlíků přicházejících z Turecka a požaduje příjmutí urychleného plánu"
                       " na přerozdělování uprchlíků v Evropě.",
        "options": [
            {
                "key": "p",
                "description": "přijmout urychleně plán pro spravedlivé přerozdělování uprchlíků",
                "delay": -1,
                "flag_set": "refugee_distribution",
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -3, "SK": -1, "AT": -3, "GR": 5, "IT": 4, "ES": 4},
                }
            },
            {
                "key": "n",
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
                "key": "p",
                "description": "přijmout záruku",
                "delay": 12,
                "impact": {
                    "satisfaction": {"GR": 5},
                    "guarantee": 5_000_000_000
                }
            },
            {
                "key": "n",
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
        "description": "Řecko požaduje mimořádnou dotaci ve výši 500 000 000 EUR na zvládnutí lesních požárů.",
        "flag": "fires_gr",
        "options": [
            {
                "key": "p",
                "description": "poskytnout dotaci",
                "delay": 12,
                "impact": {
                    "satisfaction": {"GR": 2},
                    "budget": -500_000_000,
                }
            },
            {
                "key": "n",
                "description": "neposkytnout dotaci",
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
                "key": "u",
                "description": "uzavřít dohodu a zaplatit Turecku 6 mld EUR aby zadržovlo uprchlíky",
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
                "key": "o",
                "description": "odmítnout uzavření dohody s Tureckem",
                "delay": 12,
                "impact": {
                    "satisfaction": {"GR": -5, "CY": 3},
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
]
