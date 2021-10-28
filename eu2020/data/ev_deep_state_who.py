# coding: utf-8

ev_deep_state_who = [
    {
        "party": "WHO",
        "description": "V souvislosti s probíhající pandemií WHO založila nadační fond COVAX, který má financovat nákup"
                       " a distiribuci vakcín po celém světe. WHO žádá Evropskou unii o příspěvek 10 000 000 000 EUR",
        "flag": "pandemic",
        "options": [
            {
                "key": "p",
                "description": "přijmout",
                "delay": -1,
                "impact": {
                    "satisfaction": {"WHO": 20, "NEZ": 10, "NBM": 10, "SOR": 5, "GDA": 5, "BIP": 10},
                    "budget": -10_000_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout",
                "delay": 6,
                "impact": {
                    "satisfaction": {"WHO": -10, "NEZ": -5, "NBM": -5, "SOR": -5, "GDA": -5, "BIP": -5},
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
]
