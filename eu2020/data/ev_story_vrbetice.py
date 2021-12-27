# coding: utf-8

ev_story_vrbetice = [
    {
        "party": "CZ",
        "description": "České tajné služby přinesly informaci, že za výbuchy muničních skladů ve Vrběticích stojí "
                       "ruští agenti. Česká vláda žádá společnou reakci na úrovni EU.",
        "options": [
            {
                "key": "d",
                "description": "přijmout deklaraci a odsoudit Rusko za operace na území svrchovaného státu",
                "delay": -1,
                "flag_set": "vrbetice",
                "impact": {
                    "satisfaction": {"CZ": 5, "RU": -5},
                }
            },
            {
                "key": "s",
                "description": "odsoudit Rusko a přijmout sankce",
                "delay": -1,
                "flag_set": "vrbetice",
                "impact": {
                    "satisfaction": {"CZ": 5, "RU": -10},
                }
            },
            {
                "key": "o",
                "description": "odmítnout společnou reakci na úrovni EU",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -5, "RU": 5},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                }
            },
        ]
    },
    {
        "party": "RU",
        "description": "Rusko prohlásilo obvinění týkající se výbuchu skladů ve Vrběticích za "
                       "vykonstruované a pohrozilo odvetnými kroky.",
        "condition": {
            "flag": ["vrbetice"],
        },
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
