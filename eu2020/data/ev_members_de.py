# coding: utf-8

ev_member_country_de = [
    {
        "party": "DE",
        "description": "Němečtí Zelení chtějí prosadit uzavření všech fosilních elektráren v EU.",
        "options": [
            {
                "key": "p",
                "description": "přijmout rozhodnutí o uzavření fosilních elektráren",
                "delay": -1,
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
                "description": "odmítnou rozhodnutí o uzavření fosilních elektráren",
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
]
