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
    {
        "party": "HU",
        "description": "Maďarsko postavilo plot proti uprchlíkům přicházejícím ze Srbska a Chorvatska. "
                       "Lidskoprávní organizace požadují okamžité odstranění plotu.",
        "flag": "turkey_refugee_agreement",
        "options": [
            {
                "key": "o",
                "description": "nařídit Maďarsku odstranění plotu",
                "delay": -1,
                "flag_set": "fence_hu",
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -8, "PL": -3, "SK": -1, "NEZ": 3, "SOR": 3},
                }
            },
            {
                "key": "s",
                "description": "odsouhlasit plot jako zlepšení ochrany vnějších hranic EU",
                "delay": -1,
                "flag_set": "fence_hu",
                "impact": {
                    "satisfaction": {"CZ": 3, "HU": 8, "PL": 3, "SK": 1, "NEZ": -5, "SOR": -5},
                    "budget": 200_000_000,
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
