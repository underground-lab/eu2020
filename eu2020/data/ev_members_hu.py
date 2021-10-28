# coding: utf-8

ev_member_country_hu = [
    {
        "party": "HU",
        "description": "Maďarsko zakázalo propagaci LGBT ve školách. LGBT aktivisté požadují odsoudit Maďarsko za porušování."
                       " práv menšin",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a odsoudit Maďarsko za porušování práv menšin LGBT",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -8, "PL": -3, "SK": -1},
                }
            },
            {
                "key": "k",
                "description": "udělit pokutu 200 000 000 EUR",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -8, "PL": -3, "SK": -1},
                    "budget": 200_000_000,
                }
            },
            {
                "key": "o",
                "description": "odmítnout deklaraci",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": 3, "HU": 8, "PL": 3, "SK": 1},
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
