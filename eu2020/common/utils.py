import os

import eu2020.data.texts as texts
import eu2020.data.colors as colors
from eu2020 import console


def safe_input(prompt, suppress=False):
    while True:
        try:
            return console.input(prompt)
        except (EOFError, KeyboardInterrupt):
            if suppress:
                continue
            if safe_input(
                    "\n[{0}]{1}[/{0}] ".format(colors.warning, texts.confirm_quit),
                    suppress=True
            ) in ("A", "a"):
                console.print(texts.goodbye)
                raise SystemExit


def print_text_in_box(text: str, ch="*") -> None:
    edge = ch * (len(text) + 4)
    console.print(edge, style=colors.header_style)
    console.print(f"{ch} [{colors.header_1}]{text}[/{colors.header_1}] [{colors.header_style}]{ch}[/{colors.header_style}]")
    console.print(f"{edge}\n")


def input_with_options(question: str, options: dict) -> str:
    a = None
    while a not in options:
        console.print(f"[{colors.header_2}]{question}[/{colors.header_2}]")
        for o in options:
            console.print(f"[{colors.option}]{o}[/{colors.option}] - {options[o]}")
        a = safe_input(texts.cursor)
    clear()
    return a


def proceed() -> None:
    safe_input(f"[{colors.proceed}]{texts.proceed}[/{colors.proceed}]")
    clear()


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def auto_set_option_keys(event) -> None:
    keys_used = []

    for option in event.get("options", []):
        if "key" in option:
            keys_used.append(option["key"])

    for option in reversed(event.get("options", [])):
        if "key" not in option:
            for k in option["description"]:
                if k != ' ' and k not in keys_used:
                    option["key"] = k
                    keys_used.append(k)
                    break
