from tkinter import ACTIVE
from repositories.calculator_repository import (
    calculator_repository as default_calculation_repository
)
from entities.calculation_manager import (
    calculation_manager as default_calculation_manager
)


class HistoryService:
    """
    Hoitaa HistoryViewiin liittyvän sovelluslogiikan
    """

    def __init__(self, calculation_repository=default_calculation_repository,
                 calculation_manager=default_calculation_manager):

        self._calculation_repository = calculation_repository
        self._calculation_manager = calculation_manager

    def replace_current_calculation_with_selected(self, listbox):
        """
        Korvaa nykyisen laskun listboxista valitulla laskulla

        Args:
            listbox (tkinter-objekti): tkinterin listbox-objekti
        """
        selected = listbox.get(ACTIVE)
        selected = selected.split(": ")[1]
        selected = selected.split("=")[0]

        self._calculation_manager.insert_calculation(selected)

    def delete_calculation_from_history_view(self, listbox):
        """
        Poistaa valitun laskutoimituksen listboxista ja tietokannasta

        Args:
            listbox (tkinter-objekti): tkinterin listbox-objekti
        """
        selected = listbox.get(ACTIVE)
        selected = selected.split(": ")[0]
        listbox.delete(ACTIVE)
        self._calculation_repository.delete_by_timestamp(selected)


history_service = HistoryService()
