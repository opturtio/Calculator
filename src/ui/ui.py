from ui.calculator_view import CalculatorView


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka"""

    def __init__(self, root):
        """
        Käyttöliittymäluokka joka vastaa näkymästä ja sen vaihtamisesta.

        Args:
            root:
                Tkinter-elementti: Alustaa käyttöliittymän.
        """

        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää sovelluksen käyttöliittymän"""
        self._show_calculator_view()

    def _hide_current_view(self):
        """Poistaa vanhan näkymän"""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_calculator_view(self):
        """Näyttää kirjautumisnäkymän."""
        self._hide_current_view()

        self._current_view = CalculatorView(
            self._root
        )
        self._current_view.pack()
