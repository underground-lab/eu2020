higher_power_events = [
    {
        "key": "PAN",
        "name": "Pandemie",
        "start": "Propukla pandemie nové neznámé choroby.",
        "end": "Zdá se, že pandemie ustala.",
        "period": 2,
    },
    {
        "key": "POV",
        "name": "Povodně",
        "start": "Po celé Evropě propukly povodně.",
        "end": "Povodně se podařilo zvládnout.",
        "period": 2,
    },
    {
        "key": "INF",
        "name": "Inflace",
        "start": "Evropa se potýká s vysokou mírou inflace. Lidé se bojí o své úspory.",
        "end": "Inflaci se podařilo zvládnout.",
        "period": 2,
    },
    {
        "key": "HRE",
        "name": "Hospodářská recese",
        "start": "Evropou zmítá hospodářská recese, podniky propouštějí.",
        "end": "Hospodářskou recesi se podařilo zvládnout.",
        "period": 2,
    },
]


member_country_events = [
    {
        "party": "CZ",
        "description": "Některé české strany tlačí na deklaraci proti střetu zájmů českého premiéra.",
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
]


deep_state_events = [
    {
        "party": "SOR",
        "description": "George Soros požaduje rychlejší přísun migrantů z Afriky. Nabízí příspěvek 1 000 000 000 EUR jako podporu pro lidskoprávní organizace.",
        "period": 12,
        "options": [
            {
                "key": "p",
                "description": "přijmout",
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -3, "SK": -3, "AT": -3, "IT": -3, "FR": -2},
                    "budget": 1_000_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout",
                "impact": {
                    "satisfaction": {"SOR": -10, "NEZ": -5, "WHO": -2},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "impact": {
                    "satisfaction": {"SOR": -3,},
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "WHO",
        "description": "V souvislosti s probíhající pandemií WHO založila nadační fond COVAX, který má financovat nákup a distiribuci vakcín po celém světe. WHO žádá Evropskou unii o příspěvek 10 000 000 000 EUR",
        "higher_power_cond": "PAN",
        "period": 12,
        "options": [
            {
                "key": "p",
                "description": "přijmout",
                "impact": {
                    "satisfaction": {"WHO": 20, "NEZ": 10, "NBM": 10, "SOR": 5, "GDA": 5, "BIP": 10},
                    "budget": -10_000_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout",
                "impact": {
                    "satisfaction": {"WHO": -10, "NEZ": -5, "NBM": -5, "SOR": -5, "GDA": -5, "BIP": -5},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "impact": {
                    "satisfaction": {"WHO": -10},
                    "budget": 0,
                }
            },
        ]
    },
    {
        "party": "NEZ",
        "description": "V Bělorusku proběhly volby ve kterých opět vyhrál prezident Lukašenko. Lidskoprávní organizace poukazují na to, že volby byly zmanipulované a požadují odsouzení Běloruska.",
        "period": 12,
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a odsoudit Bělorusko za zmanipulované volby",
                "impact": {
                    "satisfaction": {"NEZ": 5},
                    "budget": 0,
                }
            },
            {
                "key": "n",
                "description": "nepřijmout deklaraci odsuzující Bělorusko",
                "impact": {
                    "satisfaction": {"NEZ": -10},
                    "budget": 0,
                }
            }
        ]
    },
]
