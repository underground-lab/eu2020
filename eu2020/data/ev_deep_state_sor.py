# coding: utf-8

ev_deep_state_sor = [
    {
        "party": "SOR",
        "description": "George Soros požaduje rychlejší přísun migrantů z Afriky. Nabízí příspěvek 1 000 000 000 EUR "
                       "jako podporu pro lidskoprávní organizace.",
        "options": [
            {
                "key": "p",
                "description": "přijmout",
                "delay": 12,
                "impact": {
                    "satisfaction": {"SOR": 8, "CZ": -3, "HU": -3, "PL": -3, "SK": -3, "AT": -3, "IT": -3, "FR": -2},
                    "budget": 1_000_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout",
                "delay": 6,
                "impact": {
                    "satisfaction": {"SOR": -10, "NEZ": -5, "WHO": -2},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"SOR": -3, },
                }
            },
        ]
    },
]
