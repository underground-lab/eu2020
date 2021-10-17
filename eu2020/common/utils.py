import os
import eu2020.data.texts as texts
import eu2020.data.colors as colors
from eu2020 import console


def print_text_in_box(text: str, ch="*") -> None:
    boxw = len(text) + 4
    for _ in range(boxw):
        console.print(ch, end="", style=colors.header_style)
    console.print(f"\n{ch} [{colors.header_1}]{text}[/{colors.header_1}] [{colors.header_style}]{ch}[/{colors.header_style}]")
    for _ in range(boxw):
        console.print(ch, end="")
    print("\n")


def input_with_options(question: str, options: dict) -> str:
    a = None
    while a not in options:
        console.print(f"[{colors.header_2}]{question}[/{colors.header_2}]")
        for o in options:
            console.print(f"[{colors.option}]{o}[/{colors.option}] - {options[o]}")
        a = console.input(texts.cursor)
    clear()
    return a


def proceed() -> None:
    console.input(f"[{colors.proceed}]{texts.proceed}[/{colors.proceed}]")
    clear()


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
