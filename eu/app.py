import eu.data.texts as texts
import eu.data.data as data
from eu.common.name import Name
from eu.common.period import Period


def main():
    print(f"\n{texts.app_name}\n")

    n = input(f"{texts.what_is_your_name}\n> ")
    print()
    g = input_with_options(texts.what_is_your_gender, data.gender)
    print()
    name = Name(n, g)

    print(texts.intro.format(name.get_name5p(), name.translate("stal"), len(data.member_countries)))
    proceed()

    period = Period(2020, 0)
    print(texts.period.format(period.get_month(), period.get_year()))
    print(texts.budget.format(data.budget))


def input_with_options(question, options):
    a = None
    while a not in options.keys():
        print(question)
        for o in options.keys():
            print(f"{o} - {options[o]}")
        a = input("> ")
    return a


def proceed():
    input(texts.proceed)
    print()


if __name__ == "__main__":
    main()
