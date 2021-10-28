# coding: utf-8

ev_member_country_fr = [
    {
        "party": "FR",
        "description": "Francie požaduje záruku za vydané státní dluhopisy ve výši 20 000 000 000 EUR.",
        "options": [
            {
                "key": "p",
                "description": "přijmout záruku",
                "delay": 12,
                "impact": {
                    "satisfaction": {"FR": 5},
                    "guarantee": 20_000_000_000
                }
            },
            {
                "key": "n",
                "description": "nepřijmout záruku",
                "delay": 3,
                "impact": {
                    "satisfaction": {"FR": -5},
                }
            },
        ]
    },
]
