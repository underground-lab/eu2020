import unittest
from eu2020.common.period import Period


class TestPeriod(unittest.TestCase):

    def testFilter(self):
        period = Period(2020, 0)
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Leden", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Únor", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Březen", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Duben", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Květen", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Červen", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Červenec", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Srpen", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Září", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Říjen", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Listopad", period.get_month())
        period.next()
        self.assertEqual(2020, period.get_year())
        self.assertEqual("Prosinec", period.get_month())
        period.next()
        self.assertEqual(2021, period.get_year())
        self.assertEqual("Leden", period.get_month())
        period.next()


if __name__ == "__main__":
    unittest.main()
