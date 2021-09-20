ev_member_country = [
    {
        "party": "CZ",
        "description": "Některé české strany požadují deklaraci proti střetu zájmů českého premiéra.",
        "period": 12,
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci",
                "impact": {
                    "satisfaction": {"CZ": -5, "HU": -3, "PL": -3, "SK": -1},
                    "budget": 0,
                }
            },
            {
                "key": "o",
                "description": "odmítnout deklaraci",
                "impact": {
                    "satisfaction": {"CZ": 5, "HU": 1, "PL": 1, "SK": 1},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
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
        "period": 12,
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a odsoudit Maďarsko za porušování práv menšin LGBT",
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -8, "PL": -3, "SK": -1},
                    "budget": 0,
                }
            },
            {
                "key": "k",
                "description": "udělit pokutu 200 000 000 EUR",
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -8, "PL": -3, "SK": -1},
                    "budget": 200_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout deklaraci",
                "impact": {
                    "satisfaction": {"CZ": 3, "HU": 8, "PL": 3, "SK": 1},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
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
        "period": 12,
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a odsoudit Polsko",
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -10, "SK": -1},
                    "budget": 0,
                }
            },
            {
                "key": "k",
                "description": "udělit pokutu 200 000 000 EUR",
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -10, "SK": -1},
                    "budget": 200_000_000,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
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
        "period": 6,
        "options": [
            {
                "key": "p",
                "description": "přijmout urychleně plán pro spravedlivé přerozdělování uprchlíků",
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -3, "SK": -1, "AT": -3, "GR": 5, "IT": 4, "ES": 4},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
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
        "period": 3,
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "impact": {
                    "satisfaction": {"GR": 5},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
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
        "period": 3,
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "impact": {
                    "satisfaction": {"ES": 5},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
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
        "period": 3,
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "impact": {
                    "satisfaction": {"IT": 5},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
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
        "period": 6,
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "impact": {
                    "satisfaction": {"FR": 5},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
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
        "period": 12,
        "options": [
            {
                "key": "p",
                "description": "poskytnout dotaci",
                "impact": {
                    "satisfaction": {"GR": 2},
                    "budget": -500_000_000,
                }
            },
            {
                "key": "n",
                "description": "neposkytnout dotaci",
                "impact": {
                    "satisfaction": {"GR": -5},
                    "budget": 0,
                }
            },
        ]
    },
]
