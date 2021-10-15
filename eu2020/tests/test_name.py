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
        for name1p, name5p in names.items():
            name = Name(name1p, "m")
            self.assertEqual(name5p, name.get_name5p())


if __name__ == "__main__":
    unittest.main()
