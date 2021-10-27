# coding: utf-8

import eu2020.data.colors as colors

app_name = "EU Diktátor 2020"

what_is_your_name = "Jak se jmenuješ? "
what_is_your_gender = "Jakého seš pohlaví? "

cursor = f"[{colors.cursor}]>[/{colors.cursor}] "

proceed = "Pokračovat..."

period = "Období: {} {}"
# budget = "Rozpočet {}: {:,} EUR, rozdíl příjmů a výdajů: {:,} EUR, dluh: {:,} EUR"
membership_satisfaction = "Spokojenost členských států: [{}]{:.2f} %[/{}]"
membership_satisfaction_header = "Spokojenost členských států"
deep_state_satisfaction_header = "Spokojenost deep state"

intro = """
Ahoj {},
gratuluji - právě si se {} šéfem Evropské komise. Tvá síla a možnosti jsou prakticky neomezené.
Vládneš {} členským zemím a tvým úkolem je udržet země co nejdéle v EU.
"""

gender_dict = {
    "stal": {
        "m": "stal",
        "f": "stala",
        "n": "stalo"
    }
}

options = "Možnosti:"
higher_power_event = "Mimořádná událost"
higher_power_events = "Mimořádné události: [{}]{}[/{}]"

budget_income =        "Příjmy:                 "
budget_outcome =       "Výdaje:                 "
budget_balance =       "Bilance:                "
budget_extra_income =  "Mimořádné příjmy:       "
budget_extra_outcome = "Mimořádné výdaje:       "
budget_dept =          "Dluh z minulých období: "
budget_guarantee =     "Poskytnuté garance:     "
