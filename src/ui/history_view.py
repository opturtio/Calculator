from tkinter import *
from repositories.calculator_repository import (
    calculator_repository as default_calculator_repository
)

class HistoryView:
    """Historia näkymä"""

    def __init__(self, calculator_repository=default_calculator_repository):
        self._history_window = None
        self._calculator_repository = calculator_repository

    def open_history_window(self):
        self._history_window = Toplevel()
        self._history_window.title("History")


    #TODO luo tähän metodi joka tulostaa listan laskutoimituksista
    def create_history_list(self):
        rows = self._calculator_repository.list_calculations()
        print(rows)

history_view = HistoryView()