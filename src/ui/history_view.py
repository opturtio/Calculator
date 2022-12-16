from tkinter import *
from repositories.calculator_repository import (
    calculator_repository as default_calculation_repository
)
from services.history_service import (
    history_service as default_history_service
)


class HistoryView:
    """Muodostaa historia näkymän"""

    def __init__(self, calculation_repository=default_calculation_repository, history_service=default_history_service):
        self._history_window = None
        self._calculation_repository = calculation_repository
        self._history_service = history_service


    def open_history_window(self):
        """
        Alustaa Historia-ikkunan näkymän
        """
        self._history_window = Toplevel()
        self._history_window.title("History")
        self._history_window.geometry("600x600")
        self._label_one = Label(self._history_window, text="The history of the Calculations").pack()


    def create_scrollbar_and_listbox(self):
        """
        Alustaa listboxin ja luo scrollauksen
        """
        self._height_scrollbar = Scrollbar(self._history_window, orient="vertical")
        self._width_scrollbar = Scrollbar(self._history_window, orient="horizontal")
        self._listbox = Listbox(self._history_window, bg="white", width=70, height=25, yscrollcommand=self._height_scrollbar.set, xscrollcommand=self._width_scrollbar.set, selectmode="SINGLE")

        self._height_scrollbar.config(command=self._listbox.yview)
        self._height_scrollbar.pack(side=RIGHT, fill=Y)

        self._width_scrollbar.config(command=self._listbox.xview)
        self._width_scrollbar.pack(side=BOTTOM, fill=X)

        self._listbox.pack()


    def create_buttons(self):
        """
        Tulostaa napit select ja delete.
        Select-nappi: Valitsee valitun laskutoimituksen ja korvaa sillä nykyisen
        Delete-nappi: Poistaa laskutoimituksen
        """
        self._select_button = Button(self._history_window, text="Select", command=print("select_nappi toimii")).pack(side=BOTTOM, pady=5)
        self._delete_button = Button(self._history_window, text="Delete", command=print("delete_button toimii")).pack(side=BOTTOM, pady=10)


    def create_history_list(self):
        """
        Tulostaa listan aikaisemmista laskutoimituksista
        """
        for calc in self._calculation_repository.list_calculations():
            self._listbox.insert("end", f"{calc.fetch_timestamp()}: {calc.fetch_calculation()}")



history_view = HistoryView()
