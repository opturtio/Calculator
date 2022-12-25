class CalculationManager:
    """
    Laskutoimituksista vastaava luokka

    Attributes:
        calculation: Sen hetkinen laskutoimitus
    """

    def __init__(self, calculation):
        """
        Luokan konstruktori, joka luo uuden laskutoimituksen.

        Args:
            calculation: Sen hetkinen laskutoimitus.
        """
        self._calculation = calculation
        self._signs = "+-*/()"
        self._points = 0

    def add_sign(self, sign):
        """
        Lisää merkin laskutoimitukseen.

        Args:
            sign (str): Lisättävä merkki
        """
        if sign in self._signs:
            self.reset_points()
        self._calculation += sign

    def insert_calculation(self, calculation):
        """
        Poistaa vanhan ja lisää uuden laskutoimituksen.

        Args:
            calculation (str): Lisää uuden laskutoimituksen.
        """
        self._calculation = ""
        self._calculation = calculation

    def length(self):
        """
        Palauttaa laskutoimituksen pituuden.

        Returns:
            Integer: laskutoimuksen pituus
        """
        return len(self._calculation)

    def return_calculation(self):
        """
        Palauttaa laskutoimituksen.

        Returns:
            String: Tämän hetkinen laskutoimitus.
        """
        return self._calculation

    def return_input(self):
        """
        Palauttaa laskutoimituksen maksimissaan 42 merkkiä pitkänä.

        Returns:
            String: Palauttaa maksimissaan 42 merkkiä pitkän laskutoimituksen.
        """
        if len(self._calculation) >= 42:
            return self._calculation[len(self._calculation)-42:]
        return self._calculation

    def return_last(self):
        """
        Palauttaa laskutoimituksen viimeisen arvon.

        Returns:
            String: Laskutoimituksen viimeinen arvo.
        """
        return self._calculation[-1]

    def delete(self):
        """
        Nollaa laskutoimituksen.

        Returns:
            String: Palauttaa nollatun laskutoimituksen.
        """
        self._calculation = ""
        return self._calculation

    def delete_last(self):
        """
        Poistaa viimeisen merkin laskutoimituksesta.
        """
        self._calculation = self._calculation[:-1]

    def add_point(self):
        """
        Lisää yhden pistelaskuriin
        """
        self._points += 1

    def check_points(self):
        """
        Tarkistaa onko pistelaskuri ylittynyt sallitun määrän

        Returns:
            Palauttaa True, jos pistelaskuri ylittynyt
        """
        if self._points > 1:
            return True

    def reset_points(self):
        """
        Nollaa pistelaskurin
        """
        self._points = 0


calculation_manager = CalculationManager("")  # pylint: disable=invalid-name
