from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Calculator")
    window.minsize(361, 243)
    window.maxsize(361, 243)

    interface = UI(window)

    interface.start()

    window.mainloop()


if __name__ == '__main__':
    main()
