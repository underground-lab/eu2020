# coding: utf-8

ev_member_country_cz = [
    {
        "party": "CZ",
        "description": "České opoziční strany požadují deklaraci proti střetu zájmů českého premiéra.",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -3, "SK": -1},
                }
            },
            {
                "key": "o",
                "description": "odmítnout deklaraci",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": 1, "HU": 1, "PL": 1, "SK": 1},
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
                "description": "odsoudit Rusko a přijmou sankce",
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
]
