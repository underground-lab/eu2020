import re

ch5p = [
        (r"(.*)da$", "do"),
        (r"(.*)a$", "o"),
        (r"(.*)m$", "me"),
        (r"(.*)r$", "ře"),
        (r"(.*)š$", "ši"),
       ]

class Name:

    def __init__(self, name):
        self.name = name

    def get_name1p(self):
        return self.name

    def get_name5p(self):
        for ch in ch5p:
            pattern = re.compile(ch[0])
            if pattern.match(self.name) != None:
                return pattern.sub(r"\1" + ch[1], self.name)
        return self.name
