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
                }
            },
            {
                "key": "o",
                "description": "odmítnout deklaraci",
                "delay": 6,
                "impact": {
                    "satisfaction": {"CZ": 5, "HU": 1, "PL": 1, "SK": 1},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
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
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
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
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                    "satisfaction": {"GR": -5},
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
        "party": "ES",
        "description": "Španělsko požaduje záruku za vydané státní dluhopisy ve výši 10 000 000 000 EUR",
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
        "party": "IT",
        "description": "Itálie požaduje záruku za vydané státní dluhopisy ve výši 10 000 000 000 EUR",
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "delay": 12,
                "impact": {
                    "satisfaction": {"IT": 5},
                    "guarantee": 10_000_000_000
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
                "delay": 3,
                "impact": {
                    "satisfaction": {"IT": -5},
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
                "delay": 12,
                "impact": {
                    "satisfaction": {"FR": 5},
                    "guarantee": 20_000_000_000
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
                "delay": 3,
                "impact": {
                    "satisfaction": {"FR": -5},
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
                }
            },
        ]
    },
    {
        "party": "DE",
        "description": "Němečtí Zelení chtějí prosadit uzavření všech fosilních elektráren v EU.",
        "options": [
            {
                "key": "p",
                "description": "přijmout rozhodnutí o uzavření fosilních elektráren",
                "delay": 12,
                "impact": {
                    "satisfaction": { "BE": -1, "BG": -1, "CZ": -3, "DK": -1, "EE": -2, "FI": -2, "FR": -2, "HR": -1, "IE": -1, "IT": -2, "CY": -1, "LT": -2, "ES": -2, "SE": -2, "HU": -3, "MT": -1, "DE": +2, "NL": -2, "PL": -3, "PT": -1, "AT": -2, "RO": -3, "GR": -1, "SK": -3, "SI": -2, "LV": -2, "LU": -2,},
                }
            },
            {
                "key": "k",
                "description": "odmítnou rozhodnutí o uzavření fosilních elektráren",
                "delay": 12,
                "impact": {
                    "satisfaction": {"DE": -5,},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                }
            },
        ]
    },
]
