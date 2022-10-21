from tkinter import ttk, constants
from services.calculator_services import CalculatorServices

class CalculatorView:
    """Laskimen näkymä"""
    
    def __init__(self, root):
        """
        Luokan konstruktori. Luo uuden laskin näkymän.
        
        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan
        """
        self._root = root
        self._frame = None
        self._calculator = CalculatorServices()
        
        self._initialize()
        
    def pack(self):
        """Näyttää näkymän"""
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()
    
    def _initialize_buttons(self, entry):
        """Muodostaa käyttöliittymän näppäimet"""
        
        """Muodostaa näppäimet 0-9"""
        button_one = ttk.Button(self._frame, text="1", command=lambda: self._calculator._add_number(entry, 1))
        button_two = ttk.Button(self._frame, text="2", command=lambda: self._calculator._add_number(entry, 2))
        button_three = ttk.Button(self._frame, text="3", command=lambda: self._calculator._add_number(entry, 3))
        button_four = ttk.Button(self._frame, text="4", command=lambda: self._calculator._add_number(entry, 4))
        button_five = ttk.Button(self._frame, text="5", command=lambda: self._calculator._add_number(entry, 5))
        button_six = ttk.Button(self._frame, text="6", command=lambda: self._calculator._add_number(entry, 6))
        button_seven = ttk.Button(self._frame, text="7", command=lambda: self._calculator._add_number(entry, 7))
        button_eight = ttk.Button(self._frame, text="8", command=lambda: self._calculator._add_number(entry, 8))
        button_nine = ttk.Button(self._frame, text="9", command=lambda: self._calculator._add_number(entry, 9))
        button_zero = ttk.Button(self._frame, text="0", command=lambda: self._calculator._add_number(entry, 0))

        """Muodostaa laskutoimitus näppäimet"""
        button_add = ttk.Button(self._frame, text="+", command=lambda: self._calculator._button_click_add(entry))
        button_sub = ttk.Button(self._frame, text="-", command=lambda: self._calculator._button_click_sub(entry))
        button_mul = ttk.Button(self._frame, text="*", command=lambda: self._calculator._button_click_mul(entry))
        button_div = ttk.Button(self._frame, text="/", command=lambda: self._calculator._button_click_div(entry))

        """Muodostaa näppäimet: ( ) = CE C ."""
        button_left_bracket = ttk.Button(self._frame, text="(", command=lambda: self._calculator._button_left_bracket(entry))
        button_right_right = ttk.Button(self._frame, text=")", command=lambda: self._calculator._button_right_bracket(entry))
        button_C = ttk.Button(self._frame, text="C", command=lambda: self._calculator._button_click_C(entry))
        button_CE = ttk.Button(self._frame, text="CE", command=lambda: self._calculator._button_click_CE(entry))
        button_point = ttk.Button(self._frame, text=".", command=lambda: self._calculator._button_click_point(entry))
        button_equal = ttk.Button(self._frame, text="=", command=lambda: self._calculator._button_click_equal(entry))
        
        """Button grids"""
        
        """Rivi 1"""
        button_left_bracket.grid(row=1, column=0 ,padx=3, pady=3)
        button_right_right.grid(row=1, column=1 ,padx=3, pady=3)
        button_C.grid(row=1, column=2 ,padx=3, pady=3)
        button_CE.grid(row=1, column=3 ,padx=3, pady=3)
        
        """Rivi 2"""
        button_seven.grid(row=2, column=0 ,padx=3, pady=3)
        button_eight.grid(row=2, column=1 ,padx=3, pady=3)
        button_nine.grid(row=2, column=2 ,padx=3, pady=3)
        button_div.grid(row=2, column=3 ,padx=3, pady=3)
        
        """Rivi 3"""
        button_four.grid(row=3, column=0 ,padx=3, pady=3)
        button_five.grid(row=3, column=1 ,padx=3, pady=3)
        button_six.grid(row=3, column=2 ,padx=3, pady=3)
        button_mul.grid(row=3, column=3 ,padx=3, pady=3)
        
        """Rivi 4"""
        button_one.grid(row=4, column=0 ,padx=3, pady=3)
        button_two.grid(row=4, column=1 ,padx=3, pady=3)
        button_three.grid(row=4, column=2 ,padx=3, pady=3)
        button_sub.grid(row=4, column=3 ,padx=3, pady=3)
        
        """Rivi 5"""
        button_zero.grid(row=5, column=0 ,padx=3, pady=3)
        button_point.grid(row=5, column=1 ,padx=3, pady=3)
        button_equal.grid(row=5, column=2 ,padx=3, pady=3)
        button_add.grid(row=5, column=3 ,padx=3, pady=3)
        
    def _initialize(self):
        """Alustaa laskimen näkymän"""
        self._frame = ttk.Frame(master=self._root)
        entry = ttk.Entry(self._frame)
        entry.grid(row=0, column=0, ipadx=90, columnspan=5, padx=10, pady=10)
        
        self._initialize_buttons(entry)
