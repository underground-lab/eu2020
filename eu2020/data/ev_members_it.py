# coding: utf-8

ev_member_country_it = [
    {
        "party": "IT",
        "description": "Itálie požaduje záruku za vydané státní dluhopisy ve výši 10 000 000 000 EUR.",
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "delay": 12,
                "impact": {
                    "satisfaction": {"IT": 5},
                    "guarantee": 10_000_000_000
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
                "delay": 3,
                "impact": {
                    "satisfaction": {"IT": -5},
                }
            },
        ]
    },
    {
        "party": "IT",
        "description": "V Itálii hrozí bankrot některých významných bank. Pokud by se tak stalo, znamenalo by to "
                       "nebezpečnou destabilizaci, která by mohla vyústit v odchod zěmě z EU. Itálie proto požaduje "
                       "mimořádnou dotaci na sanaci bank ve výši 12 000 000 000 EUR.",
        "options": [
            {
                "key": "p",
                "description": "poskytnout mimořádnou dotaci ve výši 12 000 000 000 EUR",
                "delay": 24,
                "impact": {
                    "satisfaction": {"IT": 5},
                    "budget": -12_000_000_000
                }
            },
            {
                "key": "o",
                "description": "odmítnout poskytnutí dotace na sanaci italských bank",
                "delay": 3,
                "impact": {
                    "satisfaction": {"IT": -5},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"IT": -1},
                }
            },
        ]
    },
]
