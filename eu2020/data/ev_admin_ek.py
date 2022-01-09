# coding: utf-8

ev_admin_ek = [
    {
        "party": "EK",
        "description": "EK připravila návrh zákona na rozbití monopolu národních producentů a distributorů energií. "
                       "Zákon ukládá národním producentům energií prodat 1/4 produkce 'pod cenou' lokálním konkurenčním "
                       "distributorům a tím má vzniknout konkurenční prostředí s cenami energií.",
        "options": [
            {
                "description": "přijmout návrh zákona a nařídit členským státům vytvoření konkurenčních distributorů energií",
                "delay": -1,
                "flag_set": "local_energy_distributors",
                "impact": {
                    "satisfaction": {"LOB": 10},
                }
            },
            {
                "description": "odmítnout návrh zákona",
                "delay": 12,
                "impact": {
                    "satisfaction": {"LOB": -5},
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"LOB": -1},
                }
            },
        ]
    },
    {
        "party": "EK",
        "description": "Polsko, Česko, Slovensko a Maďarsko odmítly plán na přerozdělování uprchlíků. "
                       "EK proto navrhuje podání žaloby na tyto země k Evropskému soudu.",
        "condition": {
            "flag": ["refugee_distribution"],
        },
        "options": [
            {
                "description": "odsouhlasit podání žaloby na Polsko, Česko, Slovensko a Maďarsko",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -3, "SK": -3, "FR": 1, "IT": 1, "GR": 1, "ES": 1},
                }
            },
            {
                "description": "odmítnout podání žaloby na Polsko, Česko, Slovensko a Maďarsko",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": 1, "HU": 1, "PL": 1, "SK": 1, "FR": -3, "IT": -3, "GR": -3, "ES": -3},
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"FR": -1, "IT": -1, "GR": -1, "ES": -1},
                }
            },
        ]
    },
    {
        "party": "EK",
        "description": "Evropská komise vypracovala dokument 'Inkluzivní komunikace' ve kterém navrhuje "
                       "zakázat některá slova jako například Vánoce, vánoční svátky, oslovení dámy a pánové "
                       "a mají se přestat používat křesťanská jména jako Marie a Jan. Důvodem je fakt, že Evropa "
                       "už není křesťanská a vánoční oslavy nejsou dostatečně inkluzivní.",
        "options": [
            {
                "description": "odsouhlasit dokument",
                "delay": -1,
                "impact": {
                    "satisfaction": {
                        "NEZ": 3, "SOR": 3, "BE": -3, "BG": -3, "CZ": -4, "DK": -3,
                        "EE": -3, "FI": -3, "FR": -3, "HR": -3, "IE": -3, "IT": -5, "CY": -3, "LT": -3, "ES": -3, "SE": -3,
                        "HU": -3, "MT": -2, "DE": -3, "NL": -3, "PL": -5, "PT": -3, "AT": -3, "RO": -3, "GR": -3, "SK": -5,
                        "SI": -3, "LV": -3, "LU": -3,
                    },
                }
            },
            {
                "description": "odmítnout dokument",
                "delay": -1,
                "impact": {
                    "satisfaction": {"NEZ": -3, "SOR": -3},
                }
            },
            {
                "description": "nerozhodnout teď",
                "delay": 6,
                "impact": {
                    "satisfaction": {"SOR": -1},
                }
            },
        ]
    },
]
