# coding: utf-8

ev_deep_state_wef = [
    {
        "party": "WEF",
        "description": "Světové Ekonomické Fórum požaduje snížení zemědělské produkce v EU a zvýšení dovozu "
                       "zemědělských produktů z rozvojových zemí.",
        "options": [
            {
                "key": "p",
                "description": "přijmout",
                "delay": -1,
                "impact": {
                    "satisfaction": {
                        "WHO": 2, "WEF": 5, "OSN": 5, "NEZ": 4, "SOR": 2, "BE": -2, "BG": -2, "CZ": -2, "DK": -2,
                        "EE": -2, "FI": -1, "FR": -2, "HR": -1, "IE": -1, "IT": -1, "CY": -2, "LT": -2, "ES": -2, "SE": -1,
                        "HU": -2, "MT": -1, "DE": -1, "NL": -1, "PL": -2, "PT": -1, "AT": -1, "RO": -2, "GR": -1, "SK": -2,
                        "SI": -1, "LV": -1, "LU": -1,
                    },
                }
            },
            {
                "key": "o",
                "description": "odmítnout",
                "delay": 12,
                "impact": {
                    "satisfaction": {"WHO": -3, "NEZ": -4, "NBM": -1, "SOR": -1, "WEF": -5, "OSN": -5},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 6,
                "impact": {
                    "satisfaction": {"WEF": -2},
                }
            },
        ]
    },
]
