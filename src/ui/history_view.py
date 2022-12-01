from tkinter import *

class HistoryView:
    """Historia näkymä"""

    def __init__(self):
        self._history_window = None

    def open_history_window(self):
        self._history_window = Toplevel()
        self._history_window.title("History")



history_view = HistoryView()