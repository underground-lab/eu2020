# coding: utf-8

ev_admin_es = [
    {
        "party": "ES",
        "description": "Lichtenštejnsko se obrátito na Evropský soud pro lidská práva ve věci "
                       "navrácení zabaveného majetku. Po válce byly totiž na majetek Lichtenštejnů "
                       "uplatněny dekrety prezidenta Beneše. Knížecí rodina tvrdí, že jí český stát "
                       "zabavil majetek nezákonně, protože vládnoucí kníže se za Němce neprohlásil "
                       "a byl hlavou suverénního státu, který za války zachovával neutralitu.",
        "options": [
            {
                "key": "p",
                "description": "podpořit Lichtenštejnsko u Evropského soudu",
                "delay": -1,
                "impact": {
                    "satisfaction": {
                        "CZ": -5
                    },
                }
            },
            {
                "key": "e",
                "description": "nepodpořit Lichtenštejnsko u Evropského soudu",
                "delay": -1,
                "impact": {
                    "satisfaction": {
                        "CZ": 2
                    },
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
        "party": "ES",
        "description": "V Polsku začala platit sporná novela o trestání soudců (takzvaný náhubkový zákon). "
                       "Polská opozice a další kritici novinek varují, že upravené předpisy umožní trestat a "
                       "odvolat z funkce neposlušné soudce, kteří se staví proti změnám v justici prosazovaným "
                       "současnou národně-konzervativní vládou. Evropský soud navrhuje pro Polsko pokutu "
                       "1 000 000 EUR za každý den platnosti sporného zákona. Nicméně existuje riziko "
                       "že Polsko bude následně vetovat Unijní rozpočet.",
        "options": [
            {
                "key": "p",
                "description": "podpořit pokutu 1 000 000 EUR za každý den platnosti sporného zákona",
                "delay": -1,
                "impact": {
                    "satisfaction": {"PL": -10},
                    "budget": 365_000_000,
                }
            },
            {
                "key": "o",
                "description": "nepodpořit pokutu",
                "delay": -1,
                "impact": {
                    "satisfaction": {"PL": 2},
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
