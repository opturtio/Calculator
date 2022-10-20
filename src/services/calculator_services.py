

class CalculatorServices:
    """Luokka hoitaa laskimen toiminnot"""
    
    def __init__(self):
        """
        Konstruktori
        
        Args:
        
        """
        
        self._calculation = ""
        self._left_brackets = 0
        self._right_brackets = 0
        self._signs = "+-*/."
        self._error_message = False
        self._points = 0
        
    def _check_error_message(self, entry):
        """Tarkistaa näkyykö virheilmoituksesta ja poistaa sen"""
        if self._error_message:
            entry.delete(0, 'end')
            entry.insert(0, self._calculation)
            self._error_message = False
            
    def _handle_two_signs_error(self, entry, sign):
        """Ilmoittaa virheestä"""
        if sign in self._signs:
            self._error_message = True
            entry.delete(0, 'end')
            entry.insert(0, f"You cannot enter two signs in a row")
            
    def _handle_two_points_error(self, entry):
        """Hoitaa kahden pisteen virheen"""
        self._error_message = True
        entry.delete(0, 'end')
        entry.insert(0, f"You cannot have to points in a number")
    
    def _add_number(self, entry, number):
        """Lisää annetun numeron merkkijonoon"""
        self._check_error_message(entry)
        self._calculation = entry.get()
        self._calculation += str(number)
        entry.delete(0, 'end')
        entry.insert(0, self._calculation)
    
    def _button_click_add(self, entry):
        """Lisää plusmerkin merkkijonoon"""
        self._check_error_message(entry)
        if self._calculation[-1] in self._signs:
            self._handle_two_signs_error(entry, "+")
            return
        self._points = 0
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation += "+"
        entry.insert(0, self._calculation)
    
    def _button_click_sub(self, entry):
        """Lisää miinusmerkin merkkijonoon"""
        self._check_error_message(entry)
        if self._calculation[-1] in self._signs:
            self._handle_two_signs_error(entry, "-")
            return
        self._points = 0
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation += "-"
        entry.insert(0, self._calculation)
    
    def _button_click_mul(self, entry):
        """Lisää kertomerkin merkkijonoon"""
        self._check_error_message(entry)
        if self._calculation[-1] in self._signs:
            self._handle_two_signs_error(entry, "*")
            return
        self._points = 0
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation += "*"
        entry.insert(0, self._calculation)
    
    def _button_click_div(self, entry):
        """Lisää jakomerkin merkkijonoon"""
        self._check_error_message(entry)
        if self._calculation[-1] in self._signs:
            self._handle_two_signs_error(entry, "/")
            return
        self._points = 0
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation += "/"
        entry.insert(0, self._calculation)
    
    def _button_click_point(self, entry):
        """Lisää pisteen merkkijonoon"""
        self._check_error_message(entry)
        if self._calculation[-1] in self._signs:
            self._handle_two_signs_error(entry, ".")
            return
        self._points += 1
        if self._points > 1:
            self._handle_two_points_error(entry)
            self._points = 1
            return
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation += "."
        entry.insert(0, self._calculation)
        
    def _left_bracket(self, entry):
        """Lisää vasemman sulkeen"""
        pass
    
    def _right_bracket(self, entry):
        """Lisää oikean sulkeen"""
        pass
    
    def _button_click_C(self, entry):
        """Poistaa koko syötetyn merkkijonon"""
        self._points = 0
        entry.delete(0, 'end')
        self._calculation = ""
    
    def _button_click_CE(self, entry):
        """Poistaa yhden merkin"""
        self._calculation = entry.get()
        entry.delete(0, 'end')
        if self._calculation[-1] == ".":
            self._points = 0
        self._calculation = self._calculation[:-1]
        entry.insert(0, self._calculation)
    
    def _button_click_equal(self, entry):
        """Tulostaa vastauksen ja lähettää laskutoimituksen tallennettavaksi tietokantaan"""

