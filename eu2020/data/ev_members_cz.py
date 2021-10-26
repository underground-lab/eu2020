# coding: utf-8

ev_member_country_cz = [
    {
        "party": "CZ",
        "description": "Některé české strany požadují deklaraci proti střetu zájmů českého premiéra.",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci",
                "delay": 12,
                "impact": {
                    "satisfaction": {"CZ": -5, "HU": -3, "PL": -3, "SK": -1},
                }
            },
            {
                "key": "o",
                "description": "odmítnout deklaraci",
                "delay": 6,
                "impact": {
                    "satisfaction": {"CZ": 5, "HU": 1, "PL": 1, "SK": 1},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 1,
                "impact": {
                }
            },
        ]
    },
]
