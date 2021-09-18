import re
import eu2020.data.texts as texts

ch5p = [
        (r"(.*)da$", "do"),
        (r"(.*)a$", "o"),
        (r"(.*)m$", "me"),
        (r"(.*)r$", "ře"),
        (r"(.*)š$", "ši"),
       ]


class Name:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_name1p(self):
        return self.name

    def get_name5p(self):
        if self.gender != "n":
            for ch in ch5p:
                pattern = re.compile(ch[0])
                if pattern.match(self.name) is not None:
                    return pattern.sub(r"\1" + ch[1], self.name)
        return self.name

    def translate(self, word):
        t = texts.gender_dict[word]
        if (t is not None):
            return t[self.gender]
        return word
