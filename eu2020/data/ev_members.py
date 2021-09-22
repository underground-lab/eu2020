ev_member_country = [
    {
        "party": "CZ",
        "description": "Některé české strany požadují deklaraci proti střetu zájmů českého premiéra.",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci",
                "delay": 12,
                "impact": {
                    "satisfaction": {"CZ": -5, "HU": -3, "PL": -3, "SK": -1},
                    "budget": 0,
                }
            },
            {
                "key": "o",
                "description": "odmítnout deklaraci",
                "delay": 6,
                "impact": {
                    "satisfaction": {"CZ": 5, "HU": 1, "PL": 1, "SK": 1},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                    "satisfaction": {},
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "HU",
        "description": "Maďarsko zakázalo propagaci LGBT ve školách. LGBT aktivisté požadují odsoudit Maďarsko za porušování práv menšin",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a odsoudit Maďarsko za porušování práv menšin LGBT",
                "delay": 12,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -8, "PL": -3, "SK": -1},
                    "budget": 0,
                }
            },
            {
                "key": "k",
                "description": "udělit pokutu 200 000 000 EUR",
                "delay": 12,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -8, "PL": -3, "SK": -1},
                    "budget": 200_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout deklaraci",
                "delay": 6,
                "impact": {
                    "satisfaction": {"CZ": 3, "HU": 8, "PL": 3, "SK": 1},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                    "satisfaction": {},
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "PL",
        "description": "Polsko zavádí zóny bez LGBT. Aktivisté požadují přísné potrestání Polska.",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a odsoudit Polsko",
                "delay": 12,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -10, "SK": -1},
                    "budget": 0,
                }
            },
            {
                "key": "k",
                "description": "udělit pokutu 200 000 000 EUR",
                "delay": 12,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -10, "SK": -1},
                    "budget": 200_000_000,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                    "satisfaction": {},
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "GR",
        "description": "Řecko se potýká s náporem uprchlíků přicházejících z Turecka a požaduje příjmutí urychleného plánu na přerozdělování uprchlíků v Evropě.",
        "options": [
            {
                "key": "p",
                "description": "přijmout urychleně plán pro spravedlivé přerozdělování uprchlíků",
                "delay": 6,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -3, "SK": -1, "AT": -3, "GR": 5, "IT": 4, "ES": 4},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                    "satisfaction": {"GR": -5},
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "GR",
        "description": "Řecko požaduje záruku za vydané státní dluhopisy ve výši 5 000 000 000 EUR",
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "delay": 6,
                "impact": {
                    "satisfaction": {"GR": 5},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
                "delay": 3,
                "impact": {
                    "satisfaction": {"GR": -5},
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "ES",
        "description": "Španělsko požaduje záruku za vydané státní dluhopisy ve výši 10 000 000 000 EUR",
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "delay": 6,
                "impact": {
                    "satisfaction": {"ES": 5},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
                "delay": 3,
                "impact": {
                    "satisfaction": {"ES": -5},
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "IT",
        "description": "Itálie požaduje záruku za vydané státní dluhopisy ve výši 10 000 000 000 EUR",
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "delay": 6,
                "impact": {
                    "satisfaction": {"IT": 5},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
                "delay": 3,
                "impact": {
                    "satisfaction": {"IT": -5},
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "FR",
        "description": "Francie požaduje záruku za vydané státní dluhopisy ve výši 20 000 000 000 EUR",
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "delay": 6,
                "impact": {
                    "satisfaction": {"FR": 5},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
                "delay": 3,
                "impact": {
                    "satisfaction": {"FR": -5},
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "GR",
        "description": "Řecko požaduje mimořádnou dotaci ve výši 500 000 000 EUR na zvládnutí lesních požárů",
        "higher_power_cond": "PGR",
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
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "LU",
        "description": "Lucemburský šéf diplomacie požaduje vyloučení Maďarska z EU kvůli přístupu k uprchlíkům.",
        "options": [
            {
                "key": "z",
                "description": "zahájit kroky k vyloučení Maďarska z EU",
                "delay": 12,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -10, "PL": -3, "SK": -1, "LU": 3},
                    "budget": 12,
                }
            },
            {
                "key": "k",
                "description": "udělit Maďarsku pokutu 200 000 000 EUR",
                "delay": 12,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -10, "PL": -3, "SK": -1, "LU": 3},
                    "budget": 200_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout požadavek",
                "delay": 12,
                "impact": {
                    "satisfaction": {"HU": 3,"LU": -3,},
                    "budget": 200_000_000,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                    "satisfaction": {"LU": -1},
                    "budget": 0,
                }
            },
        ]
    },
]
