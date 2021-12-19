# coding: utf-8

ev_story_covid19 = [
    {
        "party": "WHO",
        "description": "Světová Zdravotnická Organizace ohlásila, že se znepokojením sleduje vývoj pandemie v Číně "
                       "a ve spolupráci s Čínskými úřady zkoumá potenciální podobnost viru s dřívějšími kmeny SARS a MERS.",
        "condition": {
            "flag": ["pandemic"],
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
                "flag_set": "pandemic_1",
            },
        ]
    },
    {
        "party": "WHO",
        "description": "Světová Zdravotnická Organizace ohlásila, že vir který se v Číně velice rychle šíří je zcela nový "
                       "kmen který byl pojmenován SARS COVID 19. Vir má velký potenciál šířit se i do dalších regionů.",
        "condition": {
            "flag": ["pandemic_1"],
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
                "flag_set": "pandemic_2",
            },
        ]
    },
    {
        "party": "IT",
        "description": "Itálie hlásí první případ nakaženého virem SARS COVID 19.",
        "condition": {
            "flag": ["pandemic_2"],
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
                "flag_set": "pandemic_3",
            },
        ]
    },
    {
        "party": "IT",
        "description": "V Itálii se onemocnění velmi rychle šíří a zasahuje hlavně starší obyvatele. "
                       "Nemocnice nestíhají a převážejí nemocné do méně zasažených regionů",
        "condition": {
            "flag": ["pandemic_3"],
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
                "flag_set": "pandemic_4",
            },
        ]
    },
    {
        "party": "ES",
        "description": "Španělsko hlásí první nakažené SARS COVID 19.",
        "condition": {
            "flag": ["pandemic_3"],
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
            },
        ]
    },
    {
        "party": "FR",
        "description": "Francie hlásí první nakažené SARS COVID 19.",
        "condition": {
            "flag": ["pandemic_3"],
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
            },
        ]
    },
    {
        "party": "DE",
        "description": "Německo hlásí první nakažené SARS COVID 19.",
        "condition": {
            "flag": ["pandemic_3"],
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
            },
        ]
    },
    {
        "party": "US",
        "description": "New York hlásí první nakažené SARS COVID 19. Politici kritizují postup vlády, která uzavřela všechny "
                       "lety z Číny, ale ponechala otevřené cesty z Evropy. Vir se tedy do USA nedostal primárně z Číny ale "
                       "z Evropy.",
        "condition": {
            "flag": ["pandemic_3"],
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
            },
        ]
    },
    {
        "party": "WHO",
        "description": "Světová Zdravotnická organizace vyhlásila celosvětovou pandemii SARS COVID 19.",
        "condition": {
            "flag": ["pandemic_4"],
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
                "flag_set": "pandemic_5",
            },
        ]
    },
    {
        "party": "WHO",
        "description": "Světová Zdravotnická organizace oznámila program vývoje vakcíny proti SARS COVID 19 do "
                       "kterého se už zapojilo přes 100 firem po celém světě. Dále WHO založila nadační fond COVAX, "
                       "který má financovat vývoj, nákup a distiribuci vakcín po celém světě. WHO žádá "
                       "Evropskou unii o příspěvek 10 000 000 000 EUR.",
        "condition": {
            "flag": ["pandemic_5"],
        },
        "options": [
            {
                "key": "p",
                "description": "přijmout",
                "delay": -1,
                "flag_set": "pandemic_6",
                "impact": {
                    "satisfaction": {"WHO": 20, "NEZ": 10, "NBM": 10, "SOR": 5, "WEF": 5, "BIP": 10},
                    "budget": -10_000_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout",
                "delay": 6,
                "impact": {
                    "satisfaction": {"WHO": -10, "NEZ": -5, "NBM": -5, "SOR": -5, "WEF": -5, "BIP": -5},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"WHO": -2},
                }
            },
        ]
    },
    {
        "party": "NBM",
        "description": "Bill Gates oznámil otevření nových gigantických výrobních kapacit pro vakcíny, které by měly pomoci"
                       " při dalších pandemiích. Nyní požaduje aby byly zavedené povinné elektronické očkovací průkazy.",
        "condition": {
            "flag": ["pandemic_6"],
        },
        "options": [
            {
                "key": "v",
                "description": "vzít na vědomí",
                "delay": -1,
                "flag_set": "pandemic_7",
            },
        ]
    },
    {
        "party": "EK",
        "description": "Evropská komise navrhuje zavedení takzvaných Green Pasů pro cestování mezi zeměmi EU.",
        "condition": {
            "flag": ["pandemic_7"],
        },
        "options": [
            {
                "key": "p",
                "description": "přijmout zavedení Green Pasů",
                "delay": -1,
                "impact": {
                    "satisfaction": {
                        "NBM": 5, "WHO": 5, "WEF": 2, "SOR": 1, "BIT": 2, "BIP": 5, "BE": -3, "BG": -3, "CZ": -5, "DK": -2,
                        "EE": -3, "FI": -3, "FR": -5, "HR": -2, "IE": -2, "IT": -5, "CY": -2, "LT": -2, "ES": -2, "SE": -4,
                        "HU": -3, "MT": -1, "DE": -2, "NL": -2, "PL": -4, "PT": -2, "AT": -3, "RO": -3, "GR": -2, "SK": -5,
                        "SI": -3, "LV": -2, "LU": -2,
                    },
                }
            },
            {
                "key": "o",
                "description": "odmítnout zavedení Green Pasů",
                "delay": 12,
                "impact": {
                    "satisfaction": {
                        "NBM": -5, "WHO": -5, "WEF": -2, "SOR": -1, "BIT": -2, "BIP": -5, "BE": 3, "BG": 3, "CZ": 5, "DK": 2,
                        "EE": 3, "FI": 3, "FR": 5, "HR": 2, "IE": 2, "IT": 5, "CY": 2, "LT": 2, "ES": 2, "SE": 4, "HU": 3,
                        "MT": 1, "DE": 2, "NL": 2, "PL": 4, "PT": 2, "AT": 3, "RO": 3, "GR": 2, "SK": 5, "SI": 3, "LV": 2,
                        "LU": 2,
                    },
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"NBM": -1},
                }
            },
        ]
    },
]
