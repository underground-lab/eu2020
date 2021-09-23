ev_deep_state = [
    {
        "party": "SOR",
        "description": "George Soros požaduje rychlejší přísun migrantů z Afriky. Nabízí příspěvek 1 000 000 000 EUR jako podporu pro lidskoprávní organizace.",
        "options": [
            {
                "key": "p",
                "description": "přijmout",
                "delay": 12,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -3, "SK": -3, "AT": -3, "IT": -3, "FR": -2},
                    "budget": 1_000_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout",
                "delay": 3,
                "impact": {
                    "satisfaction": {"SOR": -10, "NEZ": -5, "WHO": -2},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                    "satisfaction": {"SOR": -3,},
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
                "delay": 12,
                "impact": {
                    "satisfaction": {"WHO": 20, "NEZ": 10, "NBM": 10, "SOR": 5, "GDA": 5, "BIP": 10},
                    "budget": -10_000_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout",
                "delay": 3,
                "impact": {
                    "satisfaction": {"WHO": -10, "NEZ": -5, "NBM": -5, "SOR": -5, "GDA": -5, "BIP": -5},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                    "satisfaction": {"WHO": -10},
                }
            },
        ]
    },
    {
        "party": "NEZ",
        "description": "V Bělorusku proběhly volby ve kterých opět vyhrál prezident Lukašenko. Lidskoprávní organizace poukazují na to, že volby byly zmanipulované a požadují odsouzení Běloruska.",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a odsoudit Bělorusko za zmanipulované volby",
                "delay": 12,
                "impact": {
                    "satisfaction": {"NEZ": 5},
                }
            },
            {
                "key": "n",
                "description": "nepřijmout deklaraci odsuzující Bělorusko",
                "delay": 12,
                "impact": {
                    "satisfaction": {"NEZ": -10},
                }
            },
        ]
    },
    {
        "party": "NBM",
        "description": "Bill Gates oznámil otevření nových gigantických výrobních kapacit pro vakcíny, které by měly pomoci při dalších pandemiích. Nyní požaduje aby byly zavedené povinné elektronické očkovací průkazy.",
        "higher_power_cond": "PAN",
        "options": [
            {
                "key": "p",
                "description": "přijmout zavedení povinných elektronických očkovacích průkazů",
                "delay": 12,
                "impact": {
                    "satisfaction": {"NBM": 5, "WHO": 5, "GDA": 2, "SOR": 1, "BIT": 2, "BIP": 5, "BE": -3, "BG": -3, "CZ": -5, "DK": -2, "EE": -3, "FI": -3, "FR": -5, "HR": -2, "IE": -2, "IT": -5, "CY": -2, "LT": -2, "ES": -2, "SE": -4, "HU": -3, "MT": -1, "DE": -2, "NL": -2, "PL": -4, "PT": -2, "AT": -3, "RO": -3, "GR": -2, "SK": -5, "SI": -3, "LV": -2, "LU": -2,},
                }
            },
            {
                "key": "o",
                "description": "odmítnout zavedení povinných elektronických očkovacích průkazů",
                "delay": 5,
                "impact": {
                    "satisfaction": {"NBM": -5, "WHO": -5, "GDA": -2, "SOR": -1, "BIT": -2, "BIP": -5, "BE": 3, "BG": 3, "CZ": 5, "DK": 2, "EE": 3, "FI": 3, "FR": 5, "HR": 2, "IE": 2, "IT": 5, "CY": 2, "LT": 2, "ES": 2, "SE": 4, "HU": 3, "MT": 1, "DE": 2, "NL": 2, "PL": 4, "PT": 2, "AT": 3, "RO": 3, "GR": 2, "SK": 5, "SI": 3, "LV": 2, "LU": 2,},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                    "satisfaction": {"NBM": -1},
                }
            },
        ]
    },
]
