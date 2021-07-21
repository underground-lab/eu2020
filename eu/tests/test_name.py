import unittest
from eu.common.name import Name

names = {
    "Adam": "Adame",
    "Eliška": "Eliško",
    "Jana": "Jano",
    "Jarda": "Jardo",
    "Petr": "Petře",
    "Petra": "Petro",
    "Tomáš": "Tomáši",
    
}

class TestName5p(unittest.TestCase):

    def testFilter(self):
        for key in names.keys():
            name = Name(key)
            self.assertEqual(names[key], name.get_name5p())


if __name__ == "__main__":
    unittest.main()
