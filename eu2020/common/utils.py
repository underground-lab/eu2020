import os
import eu2020.data.texts as texts


def print_text_in_box(text: str, ch="*") -> None:
    boxw = len(text) + 4
    for _ in range(boxw):
        print(ch, end = "")
    print("\n{} {} {}".format(ch, text, ch))
    for _ in range(boxw):
        print(ch, end = "")
    print("\n")


def input_with_options(question: str, options: dict) -> str:
    a = None
    while a not in options.keys():
        print(question)
        for o in options.keys():
            print(f"{o} - {options[o]}")
        a = input("> ")
    clear()
    return a


def proceed() -> None:
    input(texts.proceed)
    clear()


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
