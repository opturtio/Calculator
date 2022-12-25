from tkinter import *
from PIL import ImageTk
import PIL.Image


def create_image(path):
    image = PIL.Image.open(path)
    tk_image = ImageTk.PhotoImage(image)
    return tk_image


class AboutView:
    """Muodostaa about-näkymän"""

    def __init__(self):
        """
        Luokan konstruktori.
        Luokassa yksi muuttuja johon alustetaan about-näkymä.
        """
        self._about_window = None

    def show_about_view(self):
        """Muodostaa about-ikkunan"""
        self._about_window = Toplevel()
        self._about_window.title("About")
        self._about_window.geometry('400x400')
        self._about_window.minsize(400, 400)
        self._about_window.maxsize(400, 400)

    def create_image(self):
        """Luo kuva muuttujan"""
        self._calculator_image = create_image('./src/assets/calculator2.gif')

    def print_info(self):
        """Tulostaa tiedot about-ikkunaan"""

        Label(self._about_window, text='Calculator', font=(
            'Helvetica', 18, 'bold')).pack(padx=30, pady=10)

        Label(self._about_window, text='Calculator for simple calculation',
              font=('Helvetica', 10)).pack()

        Label(self._about_window, image=self._calculator_image).pack(side=TOP)
        Label(self._about_window, text='Author: Olli-Pekka Turtio').pack()
        Label(self._about_window, text='Published: 2022©').pack()


about_view = AboutView()
