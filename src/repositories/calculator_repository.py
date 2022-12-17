from datetime import datetime
from database_connection import get_database_connection
from entities.calculations import Calculations


class CalculatorRepository:
    """
    Laskimen tietokantaa käsittelevä luokka

    Attributes:
        connection: attribuutti muodostaa yhteyden Sqlite3-tietokantaan
    """

    def __init__(self, connection):
        self._connection = connection

    def add_calculation(self, calculation):
        """Lisää laskutoimituksen tietokantaan

        Args:
            calculation (str): CalculationServicessa ja
                CalculationManagerissa käyttäjän muodostama laskutoimitus
        """
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO Calculations (calculation, timestamp) VALUES (?, ?)", (
            calculation, timestamp))
        self._connection.commit()

    def list_calculations(self):
        """
        Muodostaa Calculations-olion ja palauttaa sen
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Calculations")
        rows = cursor.fetchall()
        self._connection.commit()

        return [Calculations(row["calculation"], row["timestamp"]) for row in rows]

    def delete_calculations(self):
        """
        Poistaa kaikki laskutoimituksen tietokannasta
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM Calculations")
        self._connection.commit()


calculator_repository = CalculatorRepository(
    get_database_connection())  # pylint: disable=invalid-name
