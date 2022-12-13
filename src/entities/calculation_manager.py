class CalculationManager:
    def __init__(self, calculation):
        self._calculation = calculation

    def add_sign(self, sign):
        self._calculation += sign

    def length(self):
        return len(self._calculation)

    def return_calculation(self):
        return self._calculation

    def return_input(self):
        if len(self._calculation) >= 42:
            return self._calculation[len(self._calculation)-42:]
        return self._calculation

    def return_last(self):
        return self._calculation[-1]

    def delete(self):
        self._calculation = ""
        return self._calculation

    def delete_last(self):
        self._calculation = self._calculation[:-1]


calculation_manager = CalculationManager("")  # pylint: disable=invalid-name
