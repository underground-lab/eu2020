import os
import eu2020.data.texts as texts
from eu2020 import console


def print_text_in_box(text: str, ch="*") -> None:
    style = "cyan"
    boxw = len(text) + 4
    for _ in range(boxw):
        console.print(ch, end="", style=style)
    console.print("\n{} [yellow]{}[/yellow] [{}]{}[/{}]".format(ch, text, style, ch, style))
    for _ in range(boxw):
        console.print(ch, end="")
    print("\n")


def input_with_options(question: str, options: dict) -> str:
    a = None
    while a not in options:
        console.print(f"[cyan]{question}[/cyan]")
        for o in options:
            console.print(f"[magenta]{o}[/magenta] - {options[o]}")
        a = console.input("[cyan]>[/cyan] ")
    clear()
    return a


def proceed() -> None:
    console.input(f"[cyan]{texts.proceed}[/cyan]")
    clear()


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
