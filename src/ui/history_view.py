from tkinter import *
from repositories.calculator_repository import (
    calculator_repository as default_calculation_repository
)


class HistoryView:
    """Muodostaa historia näkymän"""

    def __init__(self, calculation_repository=default_calculation_repository):
        self._history_window = None
        self._calculation_repository = calculation_repository

    def open_history_window(self):
        self._history_window = Toplevel()
        self._history_window.title("History")
        self._history_window.geometry("400x400")


    def create_history_list(self):
        scrollbar = Scrollbar(self._history_window, orient="vertical")
        listbox = Listbox(self._history_window, width=70, height=40, yscrollcommand=scrollbar.set, selectmode=SINGLE)

        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        listbox.pack(side="left",fill="both", expand=True)


        for calc in self._calculation_repository.list_calculations():
            listbox.insert("end", f"{calc.fetch_timestamp()}: {calc.fetch_calculation()}")



history_view = HistoryView()
