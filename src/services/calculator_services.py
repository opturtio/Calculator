

class CalculatorServices:
    """Luokka hoitaa laskimen toiminnot"""
    
    def __init__(self):
        self._current = ""
        self._number = None
        
    def error(self, sign):
        """Informs if error occurs"""
        pass
    
    def _add_number(self, entry, number):
        """Adds plus sign to calculation"""
        self._current = entry.get()
        entry.delete(0, 'end')
        entry.insert(0, str(self._current) + str(number))
        print(self._current)
    
    def _button_click_add(self):
        """Adds plus sign to calculation"""
        pass
    
    def _button_click_sub(self):
        """Adds minus sign to calculation"""
        pass
    
    def _button_click_mul(self):
        """Adds multiplication sign to calculation"""
        pass
    
    def _button_click_div(self):
        """Adds division sign to calculation"""
        pass
    
    def _left_bracket(self):
        """Adds left bracket to calculation"""
        pass
    
    def _right_bracket(self):
        """Adds right bracket to calculation"""
        pass
    
    def _button_click_C(self, entry):
        """Deletes the whole calculation"""
        entry.delete(0, 'end')
    
    def _button_click_CE(self, entry):
        """Cleares one number"""
        entry.delete(0)
    
    def _button_click_point(self):
        """Adds point to calculation"""
        pass
    
    def _button_click_equal(self):
        """Calculates the calculation"""
        pass
