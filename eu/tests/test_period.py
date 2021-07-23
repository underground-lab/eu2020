import unittest
from eu.common.period import Period


class TestPeriod(unittest.TestCase):

    def testFilter(self):
        period = Period(2020, 0)
        self.assertEqual(2020, period.get_year())


if __name__ == "__main__":
    unittest.main()
