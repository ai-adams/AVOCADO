import tkinter as tk
from tkinter import ttk
from src.frames import Home
from src.scripts.dpi_awareness import set_dpi_awareness
set_dpi_awareness()

class avocadoBot_GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = ttk.Style(self)
        style.theme_use("clam")
        self.title("avocadoBot")
        self.geometry("800x600")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)
        self.frames = dict()
        home_frame = Home(container, self)
        home_frame.grid(row=0, column=0, sticky="NESW")
        self.frames[Home] = home_frame
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

if __name__ == '__main__':
    app = avocadoBot_GUI()
    app.mainloop()