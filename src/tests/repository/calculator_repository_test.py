import unittest
from datetime import datetime
from repositories.calculator_repository import (
    calculator_repository as default_calculator_repository
)
from entities.calculations import Calculations

class TestCalculatorRepository(unittest.TestCase):
    def setUp(self, calculator_repository=default_calculator_repository):
        self.calculator_repository = calculator_repository
        self.calculator_repository.delete_calculations()
        self.calculator_repository.add_calculation("2+3+4=9")

        self.current_time = datetime.now()
        timestamp = self.current_time.strftime("%Y-%m-%d %H:%M:%S")

        self.calculations = Calculations("2+3+4=9", timestamp)

    def test_listing_calculations_works(self):
        list_of_calculations = self.calculator_repository.list_calculations()
        calculation = list_of_calculations[0].fetch_calculation()
        timestamp = list_of_calculations[0].fetch_timestamp()

        self.assertEqual(calculation, self.calculations.fetch_calculation())
        self.assertAlmostEqual(timestamp, self.calculations.fetch_timestamp())

    def test_deleting_by_timestamp(self):
        self.calculator_repository.delete_by_timestamp(self.current_time)
        list_of_calculations = self.calculator_repository.list_calculations()
        timestamp = list_of_calculations[0].fetch_timestamp()

        self.assertAlmostEqual(timestamp, self.calculations.fetch_timestamp())

