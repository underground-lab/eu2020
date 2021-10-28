# coding: utf-8

ev_deep_state_nbm = [
    {
        "party": "NBM",
        "description": "Bill Gates oznámil otevření nových gigantických výrobních kapacit pro vakcíny, které by měly pomoci"
                       " při dalších pandemiích. Nyní požaduje aby byly zavedené povinné elektronické očkovací průkazy.",
        "flag": "pandemic",
        "options": [
            {
                "key": "p",
                "description": "přijmout zavedení povinných elektronických očkovacích průkazů",
                "delay": -1,
                "impact": {
                    "satisfaction": {
                        "NBM": 5, "WHO": 5, "GDA": 2, "SOR": 1, "BIT": 2, "BIP": 5, "BE": -3, "BG": -3, "CZ": -5, "DK": -2,
                        "EE": -3, "FI": -3, "FR": -5, "HR": -2, "IE": -2, "IT": -5, "CY": -2, "LT": -2, "ES": -2, "SE": -4,
                        "HU": -3, "MT": -1, "DE": -2, "NL": -2, "PL": -4, "PT": -2, "AT": -3, "RO": -3, "GR": -2, "SK": -5,
                        "SI": -3, "LV": -2, "LU": -2,
                    },
                }
            },
            {
                "key": "o",
                "description": "odmítnout zavedení povinných elektronických očkovacích průkazů",
                "delay": 12,
                "impact": {
                    "satisfaction": {
                        "NBM": -5, "WHO": -5, "GDA": -2, "SOR": -1, "BIT": -2, "BIP": -5, "BE": 3, "BG": 3, "CZ": 5, "DK": 2,
                        "EE": 3, "FI": 3, "FR": 5, "HR": 2, "IE": 2, "IT": 5, "CY": 2, "LT": 2, "ES": 2, "SE": 4, "HU": 3,
                        "MT": 1, "DE": 2, "NL": 2, "PL": 4, "PT": 2, "AT": 3, "RO": 3, "GR": 2, "SK": 5, "SI": 3, "LV": 2,
                        "LU": 2,
                    },
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"NBM": -1},
                }
            },
        ]
    },
]
