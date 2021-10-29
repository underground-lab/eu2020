# coding: utf-8

ev_deep_state_nez = [
    {
        "party": "NEZ",
        "description": "V Bělorusku proběhly volby ve kterých opět vyhrál prezident Lukašenko. Lidskoprávní organizace "
                       "poukazují na to, že volby byly zmanipulované a požadují odsouzení Běloruska.",
        "options": [
            {
                "key": "p",
                "description": "přijmout deklaraci a odsoudit Bělorusko za zmanipulované volby",
                "delay": -1,
                "flag_set": "belarus_border_conflict",
                "impact": {
                    "satisfaction": {"NEZ": 5},
                }
            },
            {
                "key": "n",
                "description": "nepřijmout deklaraci odsuzující Bělorusko",
                "delay": -1,
                "impact": {
                    "satisfaction": {"NEZ": -10},
                }
            },
        ]
    },
    {
        "party": "NEZ",
        "description": "Běloruský prezident Lukašenko v rámci odvetné hybridní války začal posílat Afghánské "
                       "a Irácké uprchlíky přes hranici s Polskem a Litvou. Obě země následně začaly své hranice "
                       "s Běloruskem opevňovat a stavět proti-imigrační plot. Neziskové lidskoprávní organizace "
                       "požadují okamžité odstranění plotu a volný průchod pro uprchlíky.",
        "flag": "belarus_border_conflict",
        "options": [
            {
                "key": "o",
                "description": "přikázat Polsku a Litvě odstranění plotu",
                "delay": -1,
                "impact": {
                    "satisfaction": {"PL": -5, "LT": -5, "NEZ": 3},
                }
            },
            {
                "key": "s",
                "description": "schválit ochranu vnějších hranic s Běloruskem",
                "delay": -1,
                "impact": {
                    "satisfaction": {"PL": 3, "LT": 3, "NEZ": -5},
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
