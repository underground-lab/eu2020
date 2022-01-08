# coding: utf-8

ev_empires_ru = [
    {
        "party": "RU",
        "description": "Ruský prezident Vladimir Putin ostře pokáral transgender ideologii "
                       "a označil ji za 'zločin proti lidskosti', když tvrdí, že děti mohou změnit pohlaví.",
        "options": [
            {
                "description": "přijmout deklaraci a ostře odsoudit Rusko za porušování práv menšin LGBT",
                "delay": -1,
                "impact": {
                    "satisfaction": {"NEZ": 10, "HU": -1, "PL": -1},
                }
            },
            {
                "description": "ignorovat",
                "delay": -1,
                "impact": {
                    "satisfaction": {"NEZ": -8},
                }
            },
            {
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
        "description": "Rusko prohlásilo, že by EU měla Bělorusku za zastavení migrace zaplatit "
                       "stejné peníze jako zaplatila Turecku.",
        "condition": {
            "flag": ["turkey_refugee_agreement", "fence_pl"],
        },
        "options": [
            {
                "description": "zaplatit Bělorusku 6 mld EUR aby zadržovalo uprchlíky",
                "delay": -1,
                "impact": {
                    "satisfaction": {"RU": 3, "PL": 5, "LT": 5},
                    "budget": -6_000_000_000,
                },
            },
            {
                "description": "odmítnout zaplatit Bělorusku aby zadržovalo uprchlíky",
                "delay": -1,
                "impact": {
                    "satisfaction": {"RU": -1, "PL": -3, "LT": -3},
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                }
            },
        ]
    },
]
