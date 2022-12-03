

class Calculations:
    def __init__(self, calculation, timestamp):
        self._calculation = calculation
        self._timestamp = timestamp
        print(self._calculation)
        print(self._timestamp)

    def fetch_calculation(self):
        return self._calculation

    def fetch_timestamp(self):
        return self._timestamp

