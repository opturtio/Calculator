import unittest
from tkinter import *
from repositories.calculator_repository import (
    calculator_repository as default_calculation_repository
)
from entities.calculation_manager import (
    calculation_manager as default_calculation_manager
)


class TestHistoryService(unittest.TestCase):
    def setUp(self, calculation_repository=default_calculation_repository, calculation_manager=default_calculation_manager):
        self._calculation_repository = calculation_repository
        self._calculation_manager = calculation_manager
