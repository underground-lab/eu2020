# coding: utf-8

import re
import eu2020.data.texts as texts

ch5p = [
    (r"(.*)a$", "o"),
    (r"(.*)el$", "le"),
    (r"(.*)l$", "le"),
    (r"(.*)m$", "me"),
    (r"(.*)n$", "ne"),
    (r"(.*)or$", "ore"),
    (r"(.*)r$", "ře"),
    (r"(.*)š$", "ši"),
    (r"(.*)v$", "ve"),
]


class Name:

    def __init__(self, name: str, gender: str):
        self.name = name
        self.gender = gender

    def get_name1p(self) -> str:
        return self.name

    def get_name5p(self) -> str:
        if self.gender != "n":
            for regex, suffix in ch5p:
                pattern = re.compile(regex)
                if pattern.match(self.name) is not None:
                    return pattern.sub(r"\1" + suffix, self.name)
        return self.name

    def translate(self, word: str) -> str:
        t = texts.gender_dict.get(word)
        if t is not None:
            return t[self.gender]
        return word
