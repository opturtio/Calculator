from repositories.calculator_repository import (
    calculator_repository as default_calculator_repository
)


class MenubarServices:
    def __init__(self, entry, calculator_repository=default_calculator_repository):
        self._entry = entry
        self._calculator_repository = calculator_repository

    def create_new(self): #TODO ainakin delete_calculatios tähän
        self._calculator_repository.delete_calculations()
