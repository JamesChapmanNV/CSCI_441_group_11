import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont
from tkcalendar import DateEntry, Calendar

from src.user_interface.utils.tree import Tree
from src import appointmentManager
from src import masseuseManager
from src import customerManager


class Appointments(ttk.Frame):
    def __init__(self, container, textvariable):
        super().__init__(container)
        self.container = container

        # Add Calendar
        cal = DateEntry(self, selectmode='day', textvariable=textvariable)

        cal.grid()
        # cal.pack(pady=20)