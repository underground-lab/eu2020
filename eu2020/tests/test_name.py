import unittest
from eu2020.common.name import Name

names = {
    "Adam": "Adame",
    "Eliška": "Eliško",
    "Jana": "Jano",
    "Jarda": "Jardo",
    "Petr": "Petře",
    "Petra": "Petro",
    "Tomáš": "Tomáši",
}


class TestName(unittest.TestCase):

    def testName5p(self):
        for key in names.keys():
            name = Name(key, "m")
            self.assertEqual(names[key], name.get_name5p())


if __name__ == "__main__":
    unittest.main()
