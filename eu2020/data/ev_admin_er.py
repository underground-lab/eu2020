# coding: utf-8

ev_admin_er = [
    {
        "party": "ER",
        "description": "Rada ministrů všech členských zemí je znepokojená strmým růstem cen energií "
                       "po schválení uzavření všech uhelných elektráren. "
                       "Většina členských zemí dokonce zažívá krachy lokálních distributorů energií a "
                       "lidé se dostávají do obtížných situací. Rada v reakci na aktuální situaci navrhuje "
                       "snížení DPH z energií.",
        "condition": {
            "flag": ["coal_power_stations_closure"]
        },
        "options": [
            {
                "key": "s",
                "description": "schválit návrh na snížení DPH z energií",
                "delay": -1,
                "impact": {
                    "satisfaction": {
                        "GDA": -3, "BE": 1, "BG": 1, "CZ": 1, "DK": 1,
                        "EE": 1, "FI": 1, "FR": 1, "HR": 1, "IE": 1, "IT": 1, "CY": 1, "LT": 1, "ES": 1, "SE": 1, "HU": 1,
                        "MT": 1, "DE": 1, "NL": 1, "PL": 1, "PT": 1, "AT": 1, "RO": 1, "GR": 1, "SK": 1, "SI": 1, "LV": 1,
                        "LU": 1,
                    },
                }
            },
            {
                "key": "z",
                "description": "zamítnout návrh na snížení DPH z energií",
                "delay": -1,
                "impact": {
                    "satisfaction": {
                        "GDA": 3, "BE": -2, "BG": -2, "CZ": -2, "DK": -2, "EE": -2, "FI": -2,
                        "FR": -3, "HR": -2, "IE": -2, "IT": -2, "CY": -2, "LT": -2, "ES": -2,
                        "SE": -2, "HU": -2, "MT": -2, "DE": -1, "NL": -1, "PL": -3, "PT": -2,
                        "AT": -1, "RO": -2, "GR": -3, "SK": -2, "SI": -2, "LV": -2,
                        "LU": -2,
                    },
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {},
                }
            },
        ]
    },
]
