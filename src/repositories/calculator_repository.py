from database_connection import get_database_connection
from datetime import datetime


class CalculatorRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_calculation(self, calculation):
        current_time = datetime.now()
        current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        db = self._connection.cursor()
        db.execute("INSERT INTO Calculations (calculation, timestamp) VALUES (?,?)", [
                   calculation, current_time])

    def list_calculations(self):
        db = self._connection.cursor()
        db.execute("SELECT * FROM Calculations")
        rows = db.fetchall()
        return rows

    def delete_calculations(self):
        db = self._connection.cursor()
        db.execute("DELETE FROM Calculations")


calculator_repository = CalculatorRepository(get_database_connection())
