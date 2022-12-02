from tkinter import *

class AboutView:
    """About näkymä"""

    def __init__(self):
        self._about_window = None

    def show_about_view(self):
        self._about_window = Toplevel()
        self._about_window.title("About")


about_view = AboutView()