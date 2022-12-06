from tkinter import ttk, constants
from tkinter import *
from services.calculator_service import CalculatorService
from services.menubar_service import MenubarService
from services.about_service import about_service as default_about_service


class CalculatorView:
    """Laskimen näkymä"""

    def __init__(self, root,
                 about_service=default_about_service):
        """
        Luokan konstruktori. Luo uuden laskin näkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan
        """
        self._root = root
        self._frame = None
        self._calculator = None
        self._menubar = None
        self._about_service = about_service
        self._initialize()

    def pack(self):
        """Näyttää näkymän"""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän"""
        self._frame.destroy()

    def _initialize_buttons(self):
        """Muodostaa käyttöliittymän näppäimet"""

        # Muodostaa näppäimet 0-9
        button_one = ttk.Button(self._frame, text="1",
                                command=lambda: self._calculator.add_number(1))
        button_two = ttk.Button(self._frame, text="2",
                                command=lambda: self._calculator.add_number(2))
        button_three = ttk.Button(self._frame, text="3",
                                  command=lambda: self._calculator.add_number(3))
        button_four = ttk.Button(self._frame, text="4",
                                 command=lambda: self._calculator.add_number(4))
        button_five = ttk.Button(self._frame, text="5",
                                 command=lambda: self._calculator.add_number(5))
        button_six = ttk.Button(self._frame, text="6",
                                command=lambda: self._calculator.add_number(6))
        button_seven = ttk.Button(self._frame, text="7",
                                  command=lambda: self._calculator.add_number(7))
        button_eight = ttk.Button(self._frame, text="8",
                                  command=lambda: self._calculator.add_number(8))
        button_nine = ttk.Button(self._frame, text="9",
                                 command=lambda: self._calculator.add_number(9))
        button_zero = ttk.Button(self._frame, text="0",
                                 command=lambda: self._calculator.add_number(0))

        # Muodostaa laskutoimitus näppäimet
        button_add = ttk.Button(self._frame, text="+",
                                command=self._calculator._button_click_add)
        button_sub = ttk.Button(self._frame, text="-",
                                command=self._calculator._button_click_sub)
        button_mul = ttk.Button(self._frame, text="*",
                                command=self._calculator._button_click_mul)
        button_div = ttk.Button(self._frame, text="/",
                                command=self._calculator._button_click_div)

        # Muodostaa näppäimet: ( ) = CE C ja .
        button_left_bracket = ttk.Button(self._frame, text="(",
                                         command=self._calculator._button_left_bracket)
        button_right_right = ttk.Button(self._frame, text=")",
                                        command=self._calculator._button_right_bracket)
        button_C = ttk.Button(self._frame, text="C",
                              command=self._calculator._button_click_clear)
        button_CE = ttk.Button(self._frame, text="CE",
                               command=self._calculator._button_click_clear_entry)
        button_point = ttk.Button(self._frame, text=".",
                                  command=self._calculator._button_click_point)
        button_equal = ttk.Button(self._frame, text="=",
                                  command=self._calculator._button_click_equal)

        """Button grids"""

        # Rivi 1
        button_left_bracket.grid(row=1, column=0, padx=3, pady=3)
        button_right_right.grid(row=1, column=1, padx=3, pady=3)
        button_C.grid(row=1, column=2, padx=3, pady=3)
        button_CE.grid(row=1, column=3, padx=3, pady=3)

        # Rivi 2
        button_seven.grid(row=2, column=0, padx=3, pady=3)
        button_eight.grid(row=2, column=1, padx=3, pady=3)
        button_nine.grid(row=2, column=2, padx=3, pady=3)
        button_div.grid(row=2, column=3, padx=3, pady=3)

        # Rivi 3
        button_four.grid(row=3, column=0, padx=3, pady=3)
        button_five.grid(row=3, column=1, padx=3, pady=3)
        button_six.grid(row=3, column=2, padx=3, pady=3)
        button_mul.grid(row=3, column=3, padx=3, pady=3)

        # Rivi 4
        button_one.grid(row=4, column=0, padx=3, pady=3)
        button_two.grid(row=4, column=1, padx=3, pady=3)
        button_three.grid(row=4, column=2, padx=3, pady=3)
        button_sub.grid(row=4, column=3, padx=3, pady=3)

        # Rivi 5
        button_zero.grid(row=5, column=0, padx=3, pady=3)
        button_point.grid(row=5, column=1, padx=3, pady=3)
        button_equal.grid(row=5, column=2, padx=3, pady=3)
        button_add.grid(row=5, column=3, padx=3, pady=3)

    def _initialize_menu(self):
        """Muodostaa käyttöliittymän menun"""
        menubar = Menu(self._root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(
            label="New", command=lambda: self._menubar.create_new())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self._root.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        historymenu = Menu(menubar, tearoff=0)
        historymenu.add_command(label="Show history",
                                command=lambda: self._menubar.show_history())
        historymenu.add_command(label="Delete history",
                                command=lambda: self._menubar.delete_history())
        menubar.add_cascade(label="History", menu=historymenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(
            label="About...", command=lambda: self._about_service.initialize_about_view())
        menubar.add_cascade(label="Help", menu=helpmenu)

        self._root.config(menu=menubar)

    def _initialize(self):
        """Alustaa laskimen näkymän"""
        self._frame = ttk.Frame(master=self._root)
        entry = ttk.Entry(self._frame)
        entry.grid(row=0, column=0, ipadx=90, columnspan=5, padx=10, pady=10)
        self._calculator = CalculatorService(entry)
        self._menubar = MenubarService(entry)
        self._initialize_buttons()
        self._initialize_menu()
