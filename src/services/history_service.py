from tkinter import *
from repositories.calculator_repository import (
    calculator_repository as default_calculation_repository
)

class HistoryService:
    """
    Hoitaa HistoryViewiin liittyvän sovelluslogiikan
    """
    def __init__(self, calculation_repository=default_calculation_repository):
        self._calculation_repository = calculation_repository

    def replace_current_calculation_with_selected(self, listbox):
        selected = listbox.get(ACTIVE)
        print(selected)

    def delete_calculation_from_history_view(self, listbox):
        selected = listbox.get(ACTIVE)
        listbox.delete(ACTIVE)
        print(selected)


history_service = HistoryService()
