# coding: utf-8

ev_member_country_lu = [
    {
        "party": "LU",
        "description": "Lucemburský šéf diplomacie požaduje vyloučení Maďarska z EU kvůli přístupu k uprchlíkům.",
        "flag": "fence_hu",
        "options": [
            {
                "key": "z",
                "description": "zahájit kroky k vyloučení Maďarska z EU",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -10, "PL": -3, "SK": -1, "LU": 3},
                }
            },
            {
                "key": "k",
                "description": "udělit Maďarsku pokutu 200 000 000 EUR",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -10, "PL": -3, "SK": -1, "LU": 3},
                    "budget": 200_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout požadavek",
                "delay": -1,
                "impact": {
                    "satisfaction": {"HU": 3, "LU": -3, },
                    "budget": 200_000_000,
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"LU": -1},
                }
            },
        ]
    },
]
