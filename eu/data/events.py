higher_power_events = [
    {
        "key": "PAN",
        "name": "Pandemie",
        "start": "Propukla pandemie nové neznámé choroby.",
        "end": "Zdá se, že pandemie ustala.",
    },
    {
        "key": "POV",
        "name": "Povodně",
        "start": "Po celé Evropě propukly povodně.",
        "end": "Povodně se podařilo zvládnout.",
    },
    {
        "key": "INF",
        "name": "Inflace",
        "start": "Evropa se potýká s vysokou mírou inflace.",
        "end": "Inflaci se podařilo zvládnout.",
    },
    {
        "key": "HRE",
        "name": "Hospodářská recese",
        "start": "Evropou zmítá hospodářská recese, podniky propouštějí.",
        "end": "Hospodářskou recesi se podařilo zvládnout.",
    },
]


member_country_events = [
    {
        "party": "CZ",
        "description": "Některé strany tlačí na deklaraci proti střetu zájmů českého premiéra.",
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
        "description": "Maďarsko potlačuje práva LBQT menšin. LBQT neziskovka navrhuje odsoudit Maďarsko za porušování práv menšin",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci",
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
]


deep_state_events = [
    {
        "party": "SOR",
        "description": "George Soros požaduje rychlejší přísun migrantů z Afriky. Nabízí příspěvek 1 000 000 000 EUR jako podporu pro lidskoprávní organizace.",
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
]
