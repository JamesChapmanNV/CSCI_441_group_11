import tkinter as tk


class Toolbar(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        menubar = tk.Menu(self.master)
        self.master.master.config(menu=menubar)

        appointment_menu = tk.Menu(menubar, tearoff=0)
        appointment_menu.add_command(label="Show Appointments")

        customers_menu = tk.Menu(menubar, tearoff=0)
        customers_menu.add_command(label="Show Customers")

        masseuses_menu = tk.Menu(menubar, tearoff=0)
        masseuses_menu.add_command(label="Show Masseuses")

        menubar.add_cascade(label="Appointments", menu=appointment_menu)
        menubar.add_cascade(label="Customers", menu=customers_menu)
        menubar.add_cascade(label="Masseuses", menu=masseuses_menu)
