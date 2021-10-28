# coding: utf-8

ev_member_country_pl = [
    {
        "party": "PL",
        "description": "Polsko zavádí zóny bez LGBT. Aktivisté požadují přísné potrestání Polska.",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a odsoudit Polsko",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -10, "SK": -1},
                }
            },
            {
                "key": "k",
                "description": "udělit pokutu 200 000 000 EUR",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -10, "SK": -1},
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
    {
        "party": "PL",
        "description": "Polsko udělalo krok k odchodu z Evropské unie. Ústavní soud rozhodl, že polské právo "
                       "je nadřazené unijnímu. Postavení ústav a jejich ustanoveních jsou předmětem vášnivé debaty "
                       "v právnické komunitě v celé Evropské unii.",
        "options": [
            {
                "key": "k",
                "description": "udělit pokutu 200 000 000 EUR a zahájit kroky k vyloučení Polska z EU",
                "delay": -1,
                "impact": {
                    "satisfaction": {"PL": -5},
                    "budget": 200_000_000,
                }
            },
            {
                "key": "p",
                "description": "přijmout deklaraci proti Polsku a udělit pokutu  200 000 000 EUR",
                "delay": -1,
                "impact": {
                    "satisfaction": {"PL": -5},
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
