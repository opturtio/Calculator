from tkinter import *
from repositories.calculator_repository import (
    calculator_repository as default_calculator_repository
)

class HistoryView:
    """Historia näkymä"""

    def __init__(self):
        self._history_window = None

    def open_history_window(self):
        self._history_window = Toplevel()
        self._history_window.title("History")

    #TODO luo tähän metodi joka tulostaa listan laskutoimituksista

history_view = HistoryView()