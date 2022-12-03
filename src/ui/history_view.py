from tkinter import *
from repositories.calculator_repository import (
    calculations as default_calculations
)

class HistoryView:
    """Historia näkymä"""

    def __init__(self, calculations=default_calculations):
        self._history_window = None
        self._calculations = calculations

    def open_history_window(self):
        self._history_window = Toplevel()
        self._history_window.title("History")


    #TODO luo tähän metodi joka tulostaa listan laskutoimituksista
    def create_history_list(self):
        for calc in self._calculations:
            print(f"{calc.fetch_timestamp()}: {calc.fetch_calculation()}")

history_view = HistoryView()