from tkinter import *

class AboutView:
    """About näkymä"""

    def __init__(self):
        self._about_window = None

    def show_about_view(self):
        self._about_window = Toplevel()
        self._about_window.title("About")
        self._about_window.geometry('300x300')

    def print_info(self):
        Label(self._about_window, text='Calculator', font=('Helvetica', 18, 'bold')).pack(padx=30, pady=10)
        Label(self._about_window, text='Author: Olli-Pekka Turtio').pack(padx=30, pady=30)


about_view = AboutView()