import tkinter.ttk as ttk
from tkcalendar import DateEntry, Calendar


class Appointments(ttk.Frame):
    def __init__(self, container, textvariable):
        super().__init__(container)
        self.container = container

        # Add Calendar
        cal = DateEntry(self, selectmode='day', textvariable=textvariable)
        cal.grid()
