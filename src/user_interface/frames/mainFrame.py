import random
import datetime

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

from src.user_interface.utils import toolbar
from src.user_interface.utils.tree import Tree


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # Declare expected class attributes
        self.tree = None

        # Show toolbar
        self.__show_toolbar()

        # Show appointments by default on UI construct
        self.__show_appointments()

    def __show_toolbar(self):
        return toolbar.Toolbar(self)

    def __show_appointments(self):
        columns = ('appt_num', 'date', 'time', 'room_num', "assigned_to", "customer")
        self.tree = Tree(master=self, columns=columns)

        for column in columns:
            stretch = True if column == columns[-1] else False

            self.tree.heading(column,
                              text=column.replace("_", " ").replace("num", "#").title(),
                              anchor="w")
            self.tree.column(column,
                             width=tkfont.Font().measure(column.title()),
                             stretch=stretch,
                             minwidth=50,
                             anchor="w")

        ####### Using this block for testing
        test_num_of_appointments = 50
        tree_entries = []
        for appointment in range(test_num_of_appointments):
            # Making a bunch of random rows to test the treeview
            appt_num = random.randint(10000, 99999)
            now = datetime.datetime.now()
            date = now.strftime('%Y-%m-%d')
            time = now.strftime('%H:%M')
            room_num = random.randint(1, 3)
            assigned_to = f"Masseuse {random.randint(1, 3)}"
            customer = "Firstname, Lastname"
            entry = (f'{appt_num}', f'{date}', f'{time}', f'{room_num}', f'{assigned_to}', f'{customer}')
            tree_entries.append(entry)
        #######

        for tree_index, tree_entry in enumerate(tree_entries):

            # Apply style tag based on whether the index of the entry is even or odd
            style_tag = 'evenrow' if tree_index % 2 == 0 else 'oddrow'
            self.tree.insert('', tk.END, values=tree_entry, tags=(style_tag,))

            # Dynamically set column width if a value entered extends the bounds of current width
            for entry_index, val in enumerate(tree_entry):
                col_w = tkfont.Font().measure(val)
                if self.tree.column(columns[entry_index], width=None) < col_w:
                    self.tree.column(columns[entry_index], width=col_w)