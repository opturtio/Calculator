from repositories.calculator_repository import (
    calculator_repository as default_calculation_repository
)

class HistoryService:
    """
    Hoitaa HistoryViewiin liittyvän sovelluslogiikan
    """
    def __init__(self, calculation_repository=default_calculation_repository):
        self._calculation_repository = calculation_repository

    def delete_calculation_from_history_view(self):
        pass

    def replace_current_calculation_with_selected(self):
        pass


history_service = HistoryService()
