import unittest
from entities.calculations import Calculations


class TestCalculations(unittest.TestCase):
    def setUp(self):
        self.calculations = Calculations("1+2+3", "2022-12-17 23:26:10")

    def test_returning_calculation_works(self):
        self.assertEqual(self.calculations.fetch_calculation(), "1+2+3")

    def test_returning_timestamp_works(self):
        self.assertEqual(self.calculations.fetch_timestamp(),
                         "2022-12-17 23:26:10")
