from repositories.calculator_repository import (
    calculator_repository as default_calculator_repository
)
from entities.calculation_manager import (
    calculation_manager as default_calculation
)


class CalculatorService:
    """
    Luokka hoitaa laskimen toiminnot

    Attributes:
        entry:
            TKinter-elementti, jonka sisään näkymä alustetaan
    """

    def __init__(self, entry, calculator_repository=default_calculator_repository,
                 calculation=default_calculation):
        """
        Luokan konstruktori, jossa on kaikki tarvittava laskutoimituksien tekemiseen.

        Args:
            entry:
                TKinter-elementti, jonka sisään näkymä alustetaan
        """
        self._entry = entry
        self._calculator_repository = calculator_repository
        self._calculation = calculation
        self._signs = "+*/"
        self._signs_and_symbols = "+*/.("
        self._signs_and_symbols_with_point = "+*/."
        self._error_message = False
        self._left_bracket = 0
        self._right_bracket = 0

    def _check_error_message(self):
        """Tarkistaa näkyykö virheilmoituksesta ja poistaa sen"""
        if self._error_message:
            self._entry.delete(0, 'end')
            self._entry.insert(0, self._calculation.return_input())
            self._error_message = False

    def _handle_two_signs_error(self, sign):
        """Ilmoittaa kahden merkin virheestä"""
        if sign in self._signs_and_symbols:
            self._error_message = True
            self._entry.delete(0, 'end')
            self._entry.insert(
                0, "You cannot enter two signs/symbols in a row")

    def _handle_two_points_error(self):
        """Hoitaa kahden pisteen virheen"""
        self._error_message = True
        self._entry.delete(0, 'end')
        self._entry.insert(0, "You cannot have two points in a number")

    def _handle_left_bracket_error(self):
        """Hoitaa vasemman sulkeen virheen"""
        self._error_message = True
        self._entry.delete(0, 'end')
        self._entry.insert(0, "You have to enter sign before bracket")

    def _handle_number_after_right_bracket_error(self):
        """Hoitaa numeron oikean sulkeen virheen jälkeen"""
        self._error_message = True
        self._entry.delete(0, 'end')
        self._entry.insert(0, "You have to enter sign after bracket")

    def _handle_right_bracket_error(self):
        """Hoitaa oikean sulkeen virheen"""
        self._error_message = True
        self._entry.delete(0, 'end')
        self._entry.insert(0, "You need to enter left bracket first")

    def _handle_equal_error(self):
        """Hoitaa laskutoimituksen virheen"""
        self._error_message = True
        self._entry.delete(0, 'end')
        self._entry.insert(
            0, f"Enter {self._left_bracket-self._right_bracket} more right brackets")

    def _handle_sing_before_equal_error(self):
        """Ilmoittaa virheellisestä merkistä, kun käyttäjä painaa '='-merkkiä"""
        self._error_message = True
        self._entry.delete(0, 'end')
        self._entry.insert(0, "You cannot have sign before pressing equal")

    def _length_zero(self):
        if self._calculation.length() == 0:
            return True

    """Laskutoimitukset"""

    def add_number(self, number):
        """Lisää annetun numeron merkkijonoon"""

        self._check_error_message()

        if self._calculation.length() > 0:
            if self._calculation.return_last() == ")":
                return self._handle_number_after_right_bracket_error()

        self._calculation.add_sign(str(number))
        self._entry.delete(0, 'end')
        self._entry.insert(0, self._calculation.return_input())

    def button_click_add(self):
        """Lisää plusmerkin merkkijonoon"""
        if self._length_zero():
            return

        self._check_error_message()

        if self._calculation.return_last() in self._signs_and_symbols:
            return self._handle_two_signs_error("+")

        self._entry.delete(0, 'end')
        self._calculation.add_sign("+")
        self._entry.insert(0, self._calculation.return_input())

    def button_click_sub(self):
        """Lisää miinusmerkin merkkijonoon"""

        self._check_error_message()

        if self._calculation.length() > 0 and self._calculation.return_last() == "-":
            return self._handle_two_signs_error("/")
        if self._calculation.length() > 0 and self._calculation.return_last() in self._signs:
            return self._handle_right_bracket_error()

        self._entry.delete(0, 'end')
        self._calculation.add_sign("-")
        self._entry.insert(0, self._calculation.return_input())

    def button_click_mul(self):
        """Lisää kertomerkin merkkijonoon"""
        if self._length_zero():
            return

        self._check_error_message()

        if self._calculation.return_last() in self._signs_and_symbols:
            return self._handle_two_signs_error("*")

        self._entry.delete(0, 'end')
        self._calculation.add_sign("*")
        self._entry.insert(0, self._calculation.return_input())

    def button_click_div(self):
        """Lisää jakomerkin merkkijonoon"""
        if self._length_zero():
            return

        self._check_error_message()

        if self._calculation.return_last() in self._signs_and_symbols:
            return self._handle_two_signs_error("/")

        self._entry.delete(0, 'end')
        self._calculation.add_sign("/")
        self._entry.insert(0, self._calculation.return_input())

    def button_click_point(self):
        """Lisää pisteen merkkijonoon"""
        self._check_error_message()

        self._calculation.add_point()
        if self._calculation.check_points():
            return self._handle_two_points_error()

        self._entry.delete(0, 'end')
        self._calculation.add_sign(".")
        self._entry.insert(0, self._calculation.return_input())

    def button_left_bracket(self):
        """Lisää vasemman sulkeen"""
        self._check_error_message()

        if self._calculation.length() == 0:
            self._calculation.add_sign("(")
            self._left_bracket += 1
            self._entry.insert(0, self._calculation.return_input())
            return

        if self._calculation.length() > 0 and self._calculation.return_last() not in self._signs:
            return self._handle_left_bracket_error()

        self._entry.delete(0, 'end')
        self._calculation.add_sign("(")
        self._left_bracket += 1
        self._entry.insert(0, self._calculation.return_input())

    def button_right_bracket(self):
        """Lisää oikean sulkeen"""
        self._check_error_message()
        self._right_bracket += 1

        if self._calculation.length() > 0:
            if self._calculation.return_last() in self._signs_and_symbols_with_point:
                self._handle_two_signs_error("+")
                self._right_bracket -= 1
                return

        if self._right_bracket > self._left_bracket:
            self._handle_right_bracket_error()
            self._right_bracket -= 1
            return

        self._entry.delete(0, 'end')
        self._calculation.add_sign(")")
        self._entry.insert(0, self._calculation.return_input())

    def button_click_clear(self):
        """Poistaa koko syötetyn merkkijonon"""
        self._check_error_message()
        self._entry.delete(0, 'end')
        self._calculation.delete()
        self._left_bracket = 0
        self._right_bracket = 0

    def button_click_clear_entry(self):
        """Poistaa yhden merkin"""
        self._check_error_message()

        self._entry.delete(0, 'end')
        if self._calculation.length() > 0 and self._calculation.return_last() == "(":
            self._left_bracket -= 1
        if self._calculation.length() > 0 and self._calculation.return_last() == ")":
            self._right_bracket -= 1
        self._calculation.delete_last()
        self._entry.insert(0, self._calculation.return_input())

    def button_click_equal(self):
        """Tulostaa vastauksen ja lähettää laskutoimituksen tallennettavaksi tietokantaan"""
        self._check_error_message()
        if self._right_bracket != self._left_bracket:
            return self._handle_equal_error()

        if self._calculation.return_last() in self._signs_and_symbols_with_point or self._calculation.return_last() == "-":
            return self._handle_sing_before_equal_error()

        self._entry.delete(0, 'end')

        result = eval(self._calculation.return_input())

        self._entry.insert(0, result)
        self._calculator_repository.add_calculation(
            f"{self._calculation.return_input()}={result}")
        self._calculation.reset_points()

    def reset(self):
        """Resetoi luokan muuttujat ja tyhjentää entryn"""
        self._error_message = False
        self._left_bracket = 0
        self._right_bracket = 0
        self._calculation.reset_points()
        self._entry.delete(0, 'end')

    def __str__(self):
        """Palauttaa laskimen näytön tämän hetkisen tilan"""
        return self._entry.get()
