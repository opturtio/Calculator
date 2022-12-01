from services.calculator_service import CalculatorService

from repositories.calculator_repository import (
    calculator_repository as default_calculator_repository
)
from entities.calculation import (
    calculation as default_calculation
)
from ui.history_view import (
    history_view as default_history_view
)


class MenubarService:
    def __init__(self, entry,
                 calculation = default_calculation,
                 calculator_repository=default_calculator_repository,
                 history_view=default_history_view):

        self._entry = entry
        self._calculation = calculation
        self._calculator_service = CalculatorService(entry)
        self._calculator_repository = calculator_repository
        self._history_view = history_view

    def create_new(self):
        self._calculator_repository.delete_calculations()
        self._calculator_service.reset()
        self._calculation.delete()

    def delete_history(self):
        self._calculator_repository.delete_calculations()
        
    def show_history(self):
        self._history_view.open_history_window()