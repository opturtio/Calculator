from services.calculator_service import CalculatorService

from repositories.calculator_repository import (
    calculator_repository as default_calculator_repository
)  # pylint: disable=duplicate-code
from entities.calculation_manager import (
    calculation_manager as default_calculation
)  # pylint: disable=duplicate-code
from ui.history_view import (
    history_view as default_history_view
)


class MenubarService:
    """
    Hoitaa menubar-valikkoon liittyvän logiikan

    Attributes:
        entry: Ottaa vastaan käyttäjän antamat syötteet
        calculation: Ottaa vastaan, tulostaa ja tallentaa käyttäjän syötteet
        calculator_repository: Vastaa tietokannan käsittelystä
        history_view: Muodostaa historia näkymän
    """

    def __init__(self, entry,
                 calculation=default_calculation,
                 calculator_repository=default_calculator_repository,
                 history_view=default_history_view):

        self._entry = entry
        self._calculation = calculation
        self._calculator_service = CalculatorService(entry)
        self._calculator_repository = calculator_repository
        self._history_view = history_view

    def create_new(self):
        """Nollaa laskimen"""
        self._calculator_repository.delete_calculations()
        self._calculator_service.reset()
        self._calculation.delete()

    def delete_history(self):
        """Tyhjentää tietokannan"""
        self._calculator_repository.delete_calculations()

    def show_history(self):
        """Muodostaa historia näkymän"""
        self._history_view.open_history_window()
        self._history_view.create_history_list()
