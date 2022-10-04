import random
import datetime

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

from src.user_interface.utils import toolbar
from src.user_interface.utils.tree import Tree

num_sidepanel_rows = 4


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        # Add rows for the side panel given a total number of rows
        for rownum in range(num_sidepanel_rows):
            self.grid_rowconfigure(rownum, weight=1)

        # Add column 0 for appointment scheduler
        self.grid_columnconfigure(0, weight=1)

        # Show appointments by default on UI construct
        self.__show_appointments()
        self.__show_buttons()

    def __show_buttons(self):

        # Split button column vertically in half
        button_panel_1 = tk.Frame(master=self)
        button_panel_1.configure(background="#0e487d")
        button_panel_1.grid_columnconfigure(1, weight=1)
        button_panel_1.grid(row=0, column=1, sticky=tk.NSEW)

        for inx, img in enumerate(self.__get_button_resources()):
            img_button = tk.Button(button_panel_1, image=img, borderwidth=0)
            img_button.grid_columnconfigure(1, weight=1)
            img_button.grid_rowconfigure(inx, weight=1)
            img_button.grid(row=inx, column=1, padx=15, pady=15, sticky=tk.NS)

        blank_frames = []
        for blank_inx in range(3):
            blank_frame = tk.Frame(master=self)
            blank_frame.configure(background="#0e487d")
            blank_frame.grid_columnconfigure(1, weight=1)
            blank_frame.grid_rowconfigure(1, weight=1)
            blank_frame.grid(row=blank_inx + 1, column=1, sticky=tk.NSEW)
            blank_frames.append(blank_frame)

    def __show_appointments(self):
        columns = ('appt_num', 'date', 'time', 'room_num', "assigned_to", "customer")
        self.tree = Tree(master=self, columns=columns)

        for column in columns:
            self.tree.heading(column,
                              text=column.replace("_", " ").replace("num", "#").title(),
                              anchor="w")
            self.tree.column(column,
                             width=tkfont.Font().measure(column.title()),
                             stretch=True if column == columns[-1] else False,
                             minwidth=50,
                             anchor="w")

        # Using this block for testing
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
        #

        for tree_index, tree_entry in enumerate(tree_entries):

            # Apply style tag based on whether the index of the entry is even or odd
            style_tag = 'evenrow' if tree_index % 2 == 0 else 'oddrow'
            self.tree.insert('', tk.END, values=tree_entry, tags=(style_tag,))

            # Dynamically set column width if a value entered extends the bounds of current width
            for entry_index, val in enumerate(tree_entry):
                col_w = tkfont.Font().measure(val)
                if self.tree.column(columns[entry_index], width=None) < col_w:
                    self.tree.column(columns[entry_index], width=col_w)

    def __get_button_resources(self):
        self.__img_appointments = tk.PhotoImage(file="./resources/button_appointments.png")
        self.__img_customers = tk.PhotoImage(file="./resources/button_customers.png")
        self.__img_masseuses = tk.PhotoImage(file="./resources/button_masseuses.png")
        self.__img_admin = tk.PhotoImage(file="./resources/button_admin.png")
        return [self.__img_appointments, self.__img_customers, self.__img_masseuses, self.__img_admin]
