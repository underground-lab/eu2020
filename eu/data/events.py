
current_random_events = []


random_events = [
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
                    "budget": 200000000,
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
