import unittest
from tkinter import Tk, ttk
from services.calculator_services import CalculatorServices
from entities.calculation import calculation


class TestCalculatorServices(unittest.TestCase):
    def setUp(self):
        self._root = Tk()
        self._frame = ttk.Frame(master=self._root)
        entry = ttk.Entry(self._frame)
        self.calculator = CalculatorServices(entry)
        self.calculation = calculation
        self.calculation.delete()

    """Testaa CalculationServices-luokan toimivuutta"""

    def test_button_click_equal(self):
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator.add_number(1)
        self.calculator._button_click_equal()
        self.assertEqual(str(self.calculator), "2")

    def test_clicking_CE_deletes_left_bracket(self):
        self.calculator._button_left_bracket()
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator._button_left_bracket()
        self.calculator._button_click_clear_entry()
        self.assertEqual(self.calculator._left_bracket, 1)

    def test_clicking_CE_deletes_right_bracket(self):
        self.calculator._button_left_bracket()
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator.add_number(1)
        self.calculator._button_right_bracket()
        self.calculator._button_click_clear_entry()
        self.assertEqual(self.calculator._right_bracket, 0)

    def test_click_equal_same_amount_brackets(self):
        self.calculator._button_left_bracket()
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator._button_left_bracket()
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator.add_number(1)
        self.calculator._button_right_bracket()
        self.calculator._button_click_equal()
        self.assertNotEqual(self.calculator._left_bracket,
                            self.calculator._right_bracket)

    def test_too_many_right_brackets(self):
        self.calculator._button_left_bracket()
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator.add_number(1)
        self.calculator._button_right_bracket()
        self.calculator._button_right_bracket()
        self.assertEqual(self.calculator._right_bracket, 1)

    def test_reduce_one_right_bracket_after_symbol(self):
        self.calculator._button_left_bracket()
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator._button_right_bracket()
        self.assertEqual(self.calculator._right_bracket, 0)

    def test_number_before_left_bracket(self):
        self.calculator.add_number(1)
        self.calculator._button_left_bracket()
        self.assertEqual(str(self.calculator),
                         "You have to enter sign before bracket")

    def test_number_after_right_bracket(self):
        self.calculator._button_left_bracket()
        self.calculator.add_number(1)
        self.calculator._button_right_bracket()
        self.calculator.add_number(1)
        self.assertEqual(str(self.calculator),
                         "You have to enter sign after bracket")

    def test_addition_two_signs_error(self):
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator._button_click_add()
        self.assertEqual(str(self.calculator),
                         "You cannot enter two signs/symbols in a row")

    def test_substraction_two_signs_error(self):
        self.calculator.add_number(1)
        self.calculator._button_click_sub()
        self.calculator._button_click_sub()
        self.assertEqual(str(self.calculator),
                         "You cannot enter two signs/symbols in a row")

    def test_multiplication_two_signs_error(self):
        self.calculator.add_number(1)
        self.calculator._button_click_mul()
        self.calculator._button_click_mul()
        self.assertEqual(str(self.calculator),
                         "You cannot enter two signs/symbols in a row")

    def test_division_two_signs_error(self):
        self.calculator.add_number(1)
        self.calculator._button_click_div()
        self.calculator._button_click_div()
        self.assertEqual(str(self.calculator),
                         "You cannot enter two signs/symbols in a row")

    def test_check_error_message_method(self):
        self.calculator._error_message = True
        self.calculator._check_error_message()
        self.assertEqual(self.calculator._error_message, False)

    def test_handle_two_points_error_method(self):
        self.calculator._handle_two_points_error()
        self.assertEqual(str(self.calculator),
                         "You cannot have to points in a number")

    def test_two_sigs_error_method(self):  # TODO check this out
        self.calculator._error_message = False
        self.calculator._handle_two_signs_error("+")
        self.assertEqual(self.calculator._error_message, True)
        self.assertCountEqual(str(self.calculator),
                              "You cannot enter two signs/symbols in a row")
