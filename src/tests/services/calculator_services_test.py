import unittest
from tkinter import Tk, ttk
from services.calculator_services import CalculatorServices

class TestCalculatorServices(unittest.TestCase):
    def setUp(self):
        self._root = Tk()
        self._frame = ttk.Frame(master=self._root)
        entry = ttk.Entry(self._frame)
        self.calculator = CalculatorServices(entry)

    """Perustestit, testaa kaikkien näppäimien toimivuuden"""    
    
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
        self.assertEqual(str(self.calculator), "1234567890")
        
    def test_addition(self):
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator.add_number(2)
        self.assertEqual(str(self.calculator), "1+2")
        
    def test_substraction(self):
        self.calculator.add_number(9)
        self.calculator._button_click_sub()
        self.calculator.add_number(8)
        self.assertEqual(str(self.calculator), "9-8")
        
    def test_multiplication(self):
        self.calculator.add_number(3)
        self.calculator._button_click_mul()
        self.calculator.add_number(4)
        self.assertEqual(str(self.calculator), "3*4")
        
    def test_division(self):
        self.calculator.add_number(5)
        self.calculator._button_click_div()
        self.calculator.add_number(6)
        self.assertEqual(str(self.calculator), "5/6")
        
    def test_point(self):
        self.calculator.add_number(0)
        self.calculator._button_click_point()
        self.calculator.add_number(7)
        self.assertEqual(str(self.calculator), "0.7")
        
    def test_both_brackets_work(self):
        self.calculator._button_left_bracket()
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator.add_number(2)        
        self.calculator._button_right_bracket()
        self.assertEqual(str(self.calculator), "(1+2)")
        
    def test_button_click_C_wipes_input(self):
        self.calculator.add_number(3)
        self.calculator._button_click_mul()
        self.calculator._button_click_C()
        self.assertEqual(str(self.calculator), "")
        
    def test_button_click_CE_wipes_one(self):
        self.calculator.add_number(3)
        self.calculator._button_click_mul()
        self.calculator._button_click_CE()
        self.assertEqual(str(self.calculator), "3")
        
    def test_button_click_equal(self):
        self.calculator.add_number(1)
        self.calculator._button_click_add()
        self.calculator.add_number(1)
        self.calculator._button_click_equal()
        self.assertEqual(str(self.calculator), "2")
        
    