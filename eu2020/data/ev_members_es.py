# coding: utf-8

ev_member_country_es = [
    {
        "party": "ES",
        "description": "Španělsko požaduje záruku za vydané státní dluhopisy ve výši 10 000 000 000 EUR.",
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "delay": 12,
                "impact": {
                    "satisfaction": {"ES": 5},
                    "guarantee": 10_000_000_000
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
                "delay": 2,
                "impact": {
                    "satisfaction": {"ES": -5},
                }
            },
        ]
    },
]
