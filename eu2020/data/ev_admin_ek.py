# coding: utf-8

ev_admin_ek = [
    {
        "party": "EK",
        "description": "Evropská komise připravila Zelenou Dohodu (Green Deal), která představuje soubor "
                       "politických iniciativ, jejichž hlavním cílem je dosáhnout toho, aby Evropa byla v "
                       "roce 2050 klimaticky neutrální. Obsahuje plán s vyhodnocenými dopady, jejíž cílem "
                       "je snížit emise skleníkových plynů EU do roku 2030 o 55 % ve srovnání s rokem 1990.",
        "options": [
            {
                "key": "p",
                "description": "přijmout Green Deal",
                "delay": -1,
                "impact": {
                    "satisfaction": {
                        "NBM": 2, "WHO": 2, "GDA": 2, "SOR": 2, "BIT": 2, "BE": -2, "BG": -2, "CZ": -2, "DK": -2,
                        "EE": -2, "FI": -1, "FR": -2, "HR": -1, "IE": -1, "IT": -1, "CY": -2, "LT": -2, "ES": -2, "SE": -1,
                        "HU": -2, "MT": -1, "DE": -1, "NL": -1, "PL": -2, "PT": -1, "AT": -1, "RO": -2, "GR": -1, "SK": -2,
                        "SI": -1, "LV": -1, "LU": -1,
                    },
                }
            },
            {
                "key": "o",
                "description": "odmítnout Green Deal",
                "delay": 6,
                "impact": {
                    "satisfaction": {
                        "NBM": -1, "WHO": -1, "GDA": -1, "SOR": -1, "BIT": -1, "BE": 1, "BG": 1, "CZ": 1, "DK": 1,
                        "EE": 1, "FI": 1, "FR": 1, "HR": 1, "IE": 1, "IT": 1, "CY": 1, "LT": 1, "ES": 1, "SE": 1, "HU": 1,
                        "MT": 1, "DE": 1, "NL": 1, "PL": 1, "PT": 1, "AT": 1, "RO": 1, "GR": 1, "SK": 1, "SI": 1, "LV": 1,
                        "LU": 1,
                    },
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"GDA": -1, "SOR": -1},
                }
            },
        ]
    },
]
