ev_deep_state = [
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
