# coding: utf-8

ev_admin_ek = [
    {
        "party": "EK",
        "description": "EK připravila návrh zákona na rozbití monopolu národních producentů a distributorů energií. "
                       "Zákon ukládá národním producentům energií prodat 1/4 produkce 'pod cenou' lokálním konkurenčním "
                       "distributorům a tím má vzniknout konkurenční prostředí s cenami energií.",
        "options": [
            {
                "key": "p",
                "description": "přijmout návrh zákona a nařídit členským státům vytvoření konkurenčních distributorů energií",
                "delay": -1,
                "flag_set": "local_energy_distributors",
                "impact": {
                    "satisfaction": {"LOB": 10},
                }
            },
            {
                "key": "o",
                "description": "odmítnout návrh zákona",
                "delay": 12,
                "impact": {
                    "satisfaction": {"LOB": -5},
                }
            },
            {
                "key": "n",
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
        "description": "Evropská komise připravila Zelenou Dohodu (Green Deal), která představuje soubor "
                       "politických iniciativ, jejichž hlavním cílem je dosáhnout toho, aby Evropa byla v "
                       "roce 2050 klimaticky neutrální. Obsahuje plán s vyhodnocenými dopady, jehož cílem "
                       "je snížit emise skleníkových plynů EU do roku 2030 o 55 % ve srovnání s rokem 1990.",
        "options": [
            {
                "key": "p",
                "description": "přijmout Green Deal",
                "delay": -1,
                "flag_set": "green_deal",
                "impact": {
                    "satisfaction": {
                        "NBM": 2, "WHO": 2, "GDA": 2, "SOR": 2, "BIT": 2, "BE": -2, "BG": -2, "CZ": -2, "DK": -2,
                        "EE": -2, "FI": -1, "FR": -2, "HR": -1, "IE": -1, "IT": -1, "CY": -2, "LT": -2, "ES": -2, "SE": -1,
                        "HU": -2, "MT": -1, "DE": -1, "NL": -1, "PL": -2, "PT": -1, "AT": -1, "RO": -2, "GR": -1, "SK": -2,
                        "SI": -1, "LV": -1, "LU": -1,
                    },
                }
            },
            {
                "key": "o",
                "description": "odmítnout Green Deal",
                "delay": 12,
                "impact": {
                    "satisfaction": {
                        "NBM": -1, "WHO": -1, "GDA": -1, "SOR": -1, "BIT": -1, "BE": 1, "BG": 1, "CZ": 1, "DK": 1,
                        "EE": 1, "FI": 1, "FR": 1, "HR": 1, "IE": 1, "IT": 1, "CY": 1, "LT": 1, "ES": 1, "SE": 1, "HU": 1,
                        "MT": 1, "DE": 1, "NL": 1, "PL": 1, "PT": 1, "AT": 1, "RO": 1, "GR": 1, "SK": 1, "SI": 1, "LV": 1,
                        "LU": 1,
                    },
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {"GDA": -1, "SOR": -1},
                }
            },
        ]
    },
    {
        "party": "EK",
        "description": "EK navrhuje v rámci Green Deal zavedení klimatické daně pro všechny majitele domů a aut.",
        "condition": {
            "flag": ["green_deal"],
        },
        "options": [
            {
                "key": "p",
                "description": "přijmout zavedení klimatické daně pro domácnosti",
                "delay": -1,
                "impact": {
                    "satisfaction": {
                        "WHO": 2, "GDA": 2, "SOR": 2, "BE": -2, "BG": -2, "CZ": -2, "DK": -2,
                        "EE": -2, "FI": -1, "FR": -2, "HR": -1, "IE": -1, "IT": -1, "CY": -2, "LT": -2, "ES": -2, "SE": -1,
                        "HU": -2, "MT": -1, "DE": -1, "NL": -1, "PL": -2, "PT": -1, "AT": -1, "RO": -2, "GR": -1, "SK": -2,
                        "SI": -1, "LV": -1, "LU": -1,
                    },
                }
            },
            {
                "key": "o",
                "description": "odmítnout zavedení klimatické daně pro domácnosti",
                "delay": 6,
                "impact": {
                    "satisfaction": {"WHO": -1, "GDA": -1, "SOR": -1},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 2,
                "impact": {
                    "satisfaction": {},
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
                "key": "s",
                "description": "odsouhlasit podání žaloby na Polsko, Česko, Slovensko a Maďarsko",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": -3, "HU": -3, "PL": -3, "SK": -3, "FR": 1, "IT": 1, "GR": 1, "ES": 1},
                }
            },
            {
                "key": "o",
                "description": "odmítnout podání žaloby na Polsko, Česko, Slovensko a Maďarsko",
                "delay": -1,
                "impact": {
                    "satisfaction": {"CZ": 1, "HU": 1, "PL": 1, "SK": 1, "FR": -3, "IT": -3, "GR": -3, "ES": -3},
                }
            },
            {
                "key": "n",
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
                "key": "s",
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
                "key": "o",
                "description": "odmítnout dokument",
                "delay": -1,
                "impact": {
                    "satisfaction": {"NEZ": -3, "SOR": -3},
                }
            },
            {
                "key": "n",
                "description": "nerozhodnout teď",
                "delay": 6,
                "impact": {
                    "satisfaction": {"SOR": -1},
                }
            },
        ]
    },
]
