import unittest
from tkinter import Tk, ttk
from services.calculator_service import CalculatorService
from entities.calculation_manager import calculation_manager


class TestCalculationManager(unittest.TestCase):
    def setUp(self):
        self._root = Tk()
        self._frame = ttk.Frame(master=self._root)
        entry = ttk.Entry(self._frame)
        self.calculator = CalculatorService(entry)
        self._calculation_manager = calculation_manager
        self._calculation_manager.delete()

    """Testaa CalculationManager-luokan, mutta samalla myös CalculationServices-luokan toimivuutta"""

    def test_input_of_numbers(self):
        self.calculator.add_number(1)
        self.calculator.add_number(2)
        self.calculator.add_number(3)
        self.calculator.add_number(4)
        self.calculator.add_number(5)
        self.calculator.add_number(6)
        self.calculator.add_number(7)
        self.calculator.add_number(8)
        self.calculator.add_number(9)
        self.calculator.add_number(0)
        self.assertEqual(
            str(self._calculation_manager.return_calculation()), "1234567890")

    def test_addition(self):
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator.add_number(2)
        self.assertEqual(
            str(self._calculation_manager.return_calculation()), "1+2")

    def test_substraction(self):
        self.calculator.add_number(9)
        self.calculator._button_click_sub()
        self.calculator.add_number(8)
        self.assertEqual(
            str(self._calculation_manager.return_calculation()), "9-8")

    def test_multiplication(self):
        self.calculator.add_number(3)
        self.calculator._button_click_mul()
        self.calculator.add_number(4)
        self.assertEqual(
            str(self._calculation_manager.return_calculation()), "3*4")

    def test_division(self):
        self.calculator.add_number(5)
        self.calculator._button_click_div()
        self.calculator.add_number(6)
        self.assertEqual(
            str(self._calculation_manager.return_calculation()), "5/6")

    def test_point(self):
        self.calculator.add_number(0)
        self.calculator._button_click_point()
        self.calculator.add_number(7)
        self.assertEqual(
            str(self._calculation_manager.return_calculation()), "0.7")

    def test_both_brackets_work(self):
        self.calculator._button_left_bracket()
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator.add_number(2)
        self.calculator._button_right_bracket()
        self.assertEqual(
            str(self._calculation_manager.return_calculation()), "(1+2)")

    def test_button_click_C_wipes_input(self):
        self.calculator.add_number(3)
        self.calculator._button_click_mul()
        self.calculator._button_click_clear()
        self.assertEqual(
            str(self._calculation_manager.return_calculation()), "")

    def test_button_click_clear_entry_wipes_one(self):
        self.calculator.add_number(3)
        self.calculator._button_click_mul()
        self.calculator._button_click_clear_entry()
        self.assertEqual(
            str(self._calculation_manager.return_calculation()), "3")

    def test_calculation_return_rigth_calculation(self):
        self.calculator.add_number(3)
        self.assertEqual(
            str(self._calculation_manager.return_calculation()), "3")

    def test_return_input_works_rigth(self):
        for i in range(10):
            for j in range(9):
                self.calculator.add_number(j)
        self.assertEqual(str(self.calculator),
                         self._calculation_manager.return_input())
