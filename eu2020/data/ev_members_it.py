# coding: utf-8

ev_member_country_it = [
    {
        "party": "IT",
        "description": "Itálie požaduje záruku za vydané státní dluhopisy ve výši 10 000 000 000 EUR",
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
]
