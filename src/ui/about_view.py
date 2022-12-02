from tkinter import *
from PIL import Image, ImageTk

def create_image(path, resize=False):
    image = Image.open(path)
    if resize:
        return image.resize(40,30)
    return image


class AboutView:
    """About näkymä"""

    def __init__(self):
        self._about_window = None
        #self._calculator_image = create_image('./src/assets/calculator2.png')

    def show_about_view(self):
        self._about_window = Toplevel()
        self._about_window.title("About")
        self._about_window.geometry('300x300')

    def print_info(self):
        Label(self._about_window, text='Calculator', font=('Helvetica', 18, 'bold')).pack(padx=30, pady=10)
        Label(self._about_window, text='Calculator for simple calculation', font=('Helvetica', 10)).pack()
        Label(self._about_window, text='Author: Olli-Pekka Turtio').pack()
        Label(self._about_window, text='Published: 2022©').pack()
        #Label(self._about_window, image=self._calculator_image).pack(padx=30, pady=35)

about_view = AboutView()