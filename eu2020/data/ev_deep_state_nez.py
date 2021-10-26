# coding: utf-8

ev_deep_state_nez = [
    {
        "party": "NEZ",
        "description": "V Bělorusku proběhly volby ve kterých opět vyhrál prezident Lukašenko. Lidskoprávní organizace"
                       " poukazují na to, že volby byly zmanipulované a požadují odsouzení Běloruska.",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a odsoudit Bělorusko za zmanipulované volby",
                "delay": 12,
                "impact": {
                    "satisfaction": {"NEZ": 5},
                }
            },
            {
                "key": "n",
                "description": "nepřijmout deklaraci odsuzující Bělorusko",
                "delay": 12,
                "impact": {
                    "satisfaction": {"NEZ": -10},
                }
            },
        ]
    },
]
