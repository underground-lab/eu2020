# coding: utf-8

ev_others_ru = [
    {
        "party": "RU",
        "description": "Ruský prezident Vladimir Putin ostře pokáral transgender ideologii "
                       "a označil ji za 'zločin proti lidskosti', když tvrdí, že děti mohou změnit pohlaví.",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a ostře odsoudit Rusko za porušování práv menšin LGBT",
                "delay": -1,
                "impact": {
                    "satisfaction": {"NEZ": 10, "HU": -1, "PL": -1},
                }
            },
            {
                "key": "i",
                "description": "ignorovat",
                "delay": -1,
                "impact": {
                    "satisfaction": {"NEZ": -8},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"NEZ": -1},
                }
            },
        ]
    },
    {
        "party": "RU",
        "description": "Rusko prohlásilo obvinění týkající se výbuchu skladů ve Vrběticích za "
                       "vykonstruované a pohrozilo odvetnými kroky.",
        "flag": "vrbetice",
        "options": [
            {
                "key": "p",
                "description": "podniknout diplomatické kroky ke zmírnění napětí",
                "delay": -1,
                "impact": {
                    "satisfaction": {"RU": 3},
                }
            },
            {
                "key": "i",
                "description": "ignorovat",
                "delay": -1,
                "impact": {
                }
            },
        ]
    },
]
