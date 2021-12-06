# coding: utf-8

import eu2020.data.colors as colors

app_name = "EU Diktátor 2020"

what_is_your_name = "Jak se jmenuješ? "
what_is_your_gender = "Jakého seš pohlaví? "

cursor = f"[{colors.cursor}]>[/{colors.cursor}] "

proceed = "Pokračovat..."

period = "Období: {} {}"
# budget = "Rozpočet {}: {:,} EUR, rozdíl příjmů a výdajů: {:,} EUR, dluh: {:,} EUR"
membership_satisfaction = "Spokojenost členských států: [{0}]{1:.2f} %[/{0}]"
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
higher_power_events = "Mimořádné události: [{0}]{1}[/{0}]"

budget_report_template = """
Příjmy:                  [$number_color]$income EUR[/$number_color]
Výdaje:                  [$number_color]$outcome EUR[/$number_color]
Mimořádné příjmy:        [$number_color]$extra_income EUR[/$number_color]
Mimořádné výdaje:        [$number_color]$extra_outcome EUR[/$number_color]
Dluh z minulých období:  [$number_color]$dept EUR[/$number_color]
Bilance:                 [$balance_color]$balance EUR[/$balance_color]
Poskytnuté garance:      [$number_color]$guarantee EUR[/$number_color]
""".lstrip()
