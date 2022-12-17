from tkinter import *
from services.calculator_service import CalculatorService
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

    def __init__(self, calculation_repository=default_calculation_repository, calculation_manager=default_calculation_manager):
        self._calculation_repository = calculation_repository
        self._calculation_manager = calculation_manager
        self._calculator_service = CalculatorService

    def replace_current_calculation_with_selected(self, listbox):
        selected = listbox.get(ACTIVE)
        selected = selected.split(": ")[1]
        selected = selected.split("=")[0]
        print(selected)
        self._calculation_manager.insert_calculation(selected)
        #self._calculator_service.insertt()


    def delete_calculation_from_history_view(self, listbox):
        selected = listbox.get(ACTIVE)
        listbox.delete(ACTIVE)
        print(selected)


history_service = HistoryService()
