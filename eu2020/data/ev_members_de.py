# coding: utf-8

ev_member_country_de = [
    {
        "party": "DE",
        "description": "Němečtí Zelení chtějí prosadit uzavření všech fosilních elektráren v EU.",
        "condition": {
            "flag": ["local_energy_distributors"]
        },
        "options": [
            {
                "key": "p",
                "description": "přijmout rozhodnutí o uzavření fosilních elektráren",
                "delay": -1,
                "flag_set": "coal_power_stations_closure",
                "impact": {
                    "satisfaction": {
                        "BE": -1, "BG": -1, "CZ": -3, "DK": -1, "EE": -2, "FI": -2, "FR": -2, "HR": -1, "IE": -1, "IT": -2,
                        "CY": -1, "LT": -2, "ES": -2, "SE": -2, "HU": -3, "MT": -1, "DE": +2, "NL": -2, "PL": -3, "PT": -1,
                        "AT": -2, "RO": -3, "GR": -1, "SK": -3, "SI": -2, "LV": -2, "LU": -2,
                    },
                }
            },
            {
                "key": "o",
                "description": "odmítnout rozhodnutí o uzavření fosilních elektráren",
                "delay": 12,
                "impact": {
                    "satisfaction": {"DE": -5, },
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
        "party": "DE",
        "description": "Německo požaduje mimořádnou pomoc ve výši 500 000 000 EUR na zvládnutí povodní.",
        "condition": {
            "flag": ["floods_de"],
        },
        "options": [
            {
                "key": "p",
                "description": "poskytnout pomoc",
                "delay": 12,
                "impact": {
                    "satisfaction": {"GR": 2},
                    "budget": -500_000_000,
                }
            },
            {
                "key": "n",
                "description": "neposkytnout pomoc",
                "delay": 3,
                "impact": {
                    "satisfaction": {"GR": -5},
                }
            },
        ]
    },
]
