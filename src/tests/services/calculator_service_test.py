import unittest
from tkinter import Tk, ttk
from services.calculator_service import CalculatorService
from entities.calculation_manager import calculation_manager


class TestCalculatorService(unittest.TestCase):
    def setUp(self):
        self._root = Tk()
        self._frame = ttk.Frame(master=self._root)
        entry = ttk.Entry(self._frame)
        self.calculator = CalculatorService(entry)
        self.calculation_manager = calculation_manager
        self.calculation_manager.delete()

    """Testaa CalculationServices-luokan toimivuutta"""

    def test_button_click_equal(self):
        self.calculator.add_number(1)
        self.calculator.button_click_add()
        self.calculator.add_number(1)
        self.calculator.button_click_equal()
        self.assertEqual(str(self.calculator), "2")

    def test_clicking_CE_deletes_left_bracket(self):
        self.calculator.button_left_bracket()
        self.calculator.add_number(1)
        self.calculator.button_click_add()
        self.calculator.button_left_bracket()
        self.calculator.button_click_clear_entry()
        self.assertEqual(self.calculator._left_bracket, 1)

    def test_clicking_CE_deletes_right_bracket(self):
        self.calculator.button_left_bracket()
        self.calculator.add_number(1)
        self.calculator.button_click_add()
        self.calculator.add_number(1)
        self.calculator.button_right_bracket()
        self.calculator.button_click_clear_entry()
        self.assertEqual(self.calculator._right_bracket, 0)

    def test_click_equal_same_amount_brackets(self):
        self.calculator.button_left_bracket()
        self.calculator.add_number(1)
        self.calculator.button_click_add()
        self.calculator.button_left_bracket()
        self.calculator.add_number(1)
        self.calculator.button_click_add()
        self.calculator.add_number(1)
        self.calculator.button_right_bracket()
        self.calculator.button_click_equal()
        self.assertNotEqual(self.calculator._left_bracket,
                            self.calculator._right_bracket)

    def test_too_many_right_brackets(self):
        self.calculator.button_left_bracket()
        self.calculator.add_number(1)
        self.calculator.button_click_add()
        self.calculator.add_number(1)
        self.calculator.button_right_bracket()
        self.calculator.button_right_bracket()
        self.assertEqual(self.calculator._right_bracket, 1)

    def test_reduce_one_right_bracket_after_symbol(self):
        self.calculator.button_left_bracket()
        self.calculator.add_number(1)
        self.calculator.button_click_add()
        self.calculator.button_right_bracket()
        self.assertEqual(self.calculator._right_bracket, 0)

    def test_number_before_left_bracket(self):
        self.calculator.add_number(1)
        self.calculator.button_left_bracket()
        self.assertEqual(str(self.calculator),
                         "You have to enter sign before bracket")

    def test_number_after_right_bracket(self):
        self.calculator.button_left_bracket()
        self.calculator.add_number(1)
        self.calculator.button_right_bracket()
        self.calculator.add_number(1)
        self.assertEqual(str(self.calculator),
                         "You have to enter sign after bracket")

    def test_addition_two_signs_error(self):
        self.calculator.add_number(1)
        self.calculator.button_click_add()
        self.calculator.button_click_add()
        self.assertEqual(str(self.calculator),
                         "You cannot enter two signs/symbols in a row")

    def test_substraction_two_signs_error(self):
        self.calculator.add_number(1)
        self.calculator.button_click_sub()
        self.calculator.button_click_sub()
        self.assertEqual(str(self.calculator),
                         "You cannot enter two signs/symbols in a row")

    def test_multiplication_two_signs_error(self):
        self.calculator.add_number(1)
        self.calculator.button_click_mul()
        self.calculator.button_click_mul()
        self.assertEqual(str(self.calculator),
                         "You cannot enter two signs/symbols in a row")

    def test_division_two_signs_error(self):
        self.calculator.add_number(1)
        self.calculator.button_click_div()
        self.calculator.button_click_div()
        self.assertEqual(str(self.calculator),
                         "You cannot enter two signs/symbols in a row")

    def test_check_error_message_method(self):
        self.calculator._error_message = True
        self.calculator._check_error_message()
        self.assertEqual(self.calculator._error_message, False)

    def test_handle_two_points_error_method(self):
        self.calculator._handle_two_points_error()
        self.assertEqual(str(self.calculator),
                         "You cannot have two points in a number")

    def test_two_sigs_error_method(self):
        self.calculator._error_message = False
        self.calculator._handle_two_signs_error("+")
        self.assertEqual(self.calculator._error_message, True)
        self.assertCountEqual(str(self.calculator),
                              "You cannot enter two signs/symbols in a row")

    def test_sign_before_equal_error(self):
        self.calculator.add_number(1)
        self.calculator.button_click_div()
        self.calculator.button_click_sub()
        self.assertEqual(str(self.calculator),
                         "You need to enter left bracket first")

    def test_two_points_error(self):
        self.calculator.add_number(1)
        self.calculator.button_click_point()
        self.calculator.add_number(1)
        self.calculator.button_click_point()
        self.assertEqual(str(self.calculator),
                         "You cannot have two points in a number")

    def test_sign_before_equal(self):
        self.calculator.add_number(6)
        self.calculator.button_click_div()
        self.calculator.add_number(6)
        self.calculator.button_click_div()
        self.calculator.button_click_equal()
        self.assertEqual(str(self.calculator),
                         "You cannot have sign before pressing equal")

    def test_does_reset_work(self):
        self.calculator.reset()
        self.assertEqual(self.calculator._error_message, False)
        self.assertEqual(self.calculator._left_bracket, 0)
        self.assertEqual(self.calculator._right_bracket, 0)
        self.assertEqual(self.calculation_manager._points, 0)

    def test_entering_right_bracket_to_empty_entry(self):
        self.calculator.button_right_bracket()
        self.assertEqual(str(self.calculator),
                         "You need to enter left bracket first")
