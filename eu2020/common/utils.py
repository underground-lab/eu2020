import os
import eu2020.data.texts as texts


def print_text_in_box(text, ch="*"):
    boxw = len(text) + 4
    for _ in range(boxw):
        print(ch, end = "")
    print("\n{} {} {}".format(ch, text, ch))
    for _ in range(boxw):
        print(ch, end = "")
    print("\n")


def input_with_options(question, options):
    a = None
    while a not in options.keys():
        print(question)
        for o in options.keys():
            print(f"{o} - {options[o]}")
        a = input("> ")
    clear()
    return a


def proceed():
    input(texts.proceed)
    clear()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
