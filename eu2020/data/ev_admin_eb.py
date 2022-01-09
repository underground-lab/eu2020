# coding: utf-8

ev_admin_eb = [
    {
        "party": "EB",
        "description": "Evropská centrální banka navrhuje řešit vysokou míru inflace zvednutím úrokových "
                       "sazeb (tj. zdražením úvěrů). Toto opatření ale může vážně ohrozit státy s vysokým "
                       "zadlužením jako je Itálie, Francie a Španělsko a plánované opatření by je mohlo dovést "
                       "k bankrotu.",
        "condition": {
            "flag": ["inflation"],
        },
        "options": [
            {
                "description": "podpořit opatření proti inflaci zvednutím úrokových sazeb",
                "delay": 12,
                "impact": {
                    "satisfaction": {"FR": -3, "IT": -5, "ES": -3, "GR": -2},
                }
            },
            {
                "description": "odmítnout opatření proti inflaci zvednutím úrokových sazeb",
                "delay": 12,
                "impact": {
                    "satisfaction": {"FR": 1, "IT": 1, "ES": 1, "GR": 1},
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {},
                }
            },
        ]
    },
    {
        "party": "EB",
        "description": "Evropská centrální banka navrhuje řešit probíhající hospodářskou recesi takzvaným "
                       "kvantitativním uvolňováním (pumpováním peněz do ekonomiky). Důsledkem tohoto opatření "
                       "je ale růst inflace.",
        "condition": {
            "flag": ["economic_recession"],
        },
        "options": [
            {
                "description": "podpořit kvantitativní uvolňování tiskem nových peněz",
                "delay": 12,
                "impact": {
                    "satisfaction": {"FR": 2, "IT": 2, "ES": 2, "GR": 2},
                }
            },
            {
                "description": "podpořit kvantitativní uvolňování zavedením záporných úrokových sazeb",
                "delay": 12,
                "impact": {
                    "satisfaction": {"FR": 2, "IT": 2, "ES": 2, "GR": 2},
                }
            },
            {
                "description": "odmítnout zavedení kvantitativního uvolňování",
                "delay": 12,
                "impact": {
                    "satisfaction": {},
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {},
                }
            },
        ]
    },
]
