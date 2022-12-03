from database_connection import get_database_connection
from datetime import datetime
from entities.calculations import Calculations

class CalculatorRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_calculation(self, calculation):
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        db = self._connection.cursor()
        db.execute("INSERT INTO Calculations (calculation, timestamp) VALUES (?, ?)", [
                   calculation, timestamp])

    def list_calculations(self):
        db = self._connection.cursor()
        db.execute("SELECT * FROM Calculations")
        rows = db.fetchall()

        return [Calculations(row["calculation"], row["timestamp"]) for row in rows]

    def delete_calculations(self):
        db = self._connection.cursor()
        db.execute("DELETE FROM Calculations")


calculator_repository = CalculatorRepository(get_database_connection())
calculations = calculator_repository.list_calculations()
