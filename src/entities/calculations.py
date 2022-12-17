class Calculations:
    """
    Tietokannasta noudettaessa laskutoimitusta,
    muodostetaan Calculations-olio, jota voidaan käyttää
    palauttamaan laskutoimitus tai kellon aika jolloin
    se on tallennettu tietokantaan.

    Attributes:
        calculation: Tietokannasta poimittu laskutoimitus.
        timestamp: Tietokannasta poimitun laskutoimituksen aikaleima.
    """
    def __init__(self, calculation, timestamp):
        """
        Luokan konstruktori, joka luo uuden laskutoimituksen ja
        aikaleiman tietokannasta poimituille laskutoimituksille.

        Args:
            calculation (String): Muodostaa calculation muuttujan,
            johon on tallennettu tietokannasta poimittu laskutoimitus
            timestamp (String): Muodostaa timestamp muuttujan,
            johon on tallennettu tietokannasta poimitun laskutoimituksen aikaleima.
        """
        self._calculation = calculation
        self._timestamp = timestamp

    def fetch_calculation(self):
        """
        Palauttaa calculation muuttujan.

        Returns:
            String: Tietokannasta poimittu laskutoimitus.
        """
        return self._calculation

    def fetch_timestamp(self):
        """
        Palauttaa timestamp muuttujan.

        Returns:
            String: Tietokannasta poimitun laskutoimituksen aikaleima.
        """
        return self._timestamp
