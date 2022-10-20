

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
        
    def _handle_error(self, entry, sign):
        """Informs if error occurs"""
        if sign in self._signs:
            self._error_message = True
            entry.delete(0, 'end')
            entry.insert(0, f"You cannot enter two {sign} in a row")
    
    def _check_error_message(self, entry):
        if self._error_message:
            entry.delete(0, 'end')
            entry.insert(0, str(self._calculation))
            self._error_message = False
    
    def _add_number(self, entry, number):
        """Adds plus sign to calculation"""
        self._check_error_message(entry)
        self._calculation = entry.get()
        self._calculation += str(number)
        entry.delete(0, 'end')
        entry.insert(0, self._calculation)
    
    def _button_click_add(self, entry):
        """Adds plus sign to calculation"""
        self._check_error_message(entry)
        if self._calculation[-1] in self._signs:
            self._handle_error(entry, "+")
            return
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation += "+"
        entry.insert(0, self._calculation)
    
    def _button_click_sub(self, entry):
        """Adds minus sign to calculation"""
        self._check_error_message(entry)
        if self._calculation[-1] in self._signs:
            self._handle_error(entry, "-")
            return
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation += "-"
        entry.insert(0, self._calculation)
    
    def _button_click_mul(self, entry):
        """Adds multiplication sign to calculation"""
        self._check_error_message(entry)
        if self._calculation[-1] in self._signs:
            self._handle_error(entry, "*")
            return
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation += "*"
        entry.insert(0, self._calculation)
    
    def _button_click_div(self, entry):
        """Adds division sign to calculation"""
        self._check_error_message(entry)
        if self._calculation[-1] in self._signs:
            self._handle_error(entry, "/")
            return
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation += "/"
        entry.insert(0, self._calculation)
    
    def _button_click_point(self, entry):
        """Adds point to calculation"""
        self._check_error_message(entry)
        if self._calculation[-1] in self._signs:
            self._handle_error(entry, ".")
            return
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation += "."
        entry.insert(0, self._calculation)
        
    def _left_bracket(self, entry):
        """Adds left bracket to calculation"""
        pass
    
    def _right_bracket(self, entry):
        """Adds right bracket to calculation"""
        pass
    
    def _button_click_C(self, entry):
        """Deletes the whole calculation"""
        entry.delete(0, 'end')
        self._calculation = ""
    
    def _button_click_CE(self, entry):
        """Cleares one number"""
        self._calculation = entry.get()
        entry.delete(0, 'end')
        self._calculation = self._calculation[:-1]
        entry.insert(0, self._calculation)
    
    def _button_click_equal(self, entry):
        """Calculates the calculation"""

