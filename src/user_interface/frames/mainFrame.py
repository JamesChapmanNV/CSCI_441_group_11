import random
import datetime

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

from src.user_interface.utils.tree import Tree

num_sidepanel_rows = 4

button_panel_width = 200
button_panel_bg = "gray17"

btn_strings = ["Appointments", "Customers", "Masseuses", "Admin"]


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
        btn_panel = tk.Frame(master=self)
        btn_panel.configure(background=button_panel_bg)
        btn_panel.grid_columnconfigure(1, weight=1)
        btn_panel.grid(row=0, column=1, rowspan=len(btn_strings), sticky=tk.NSEW)

        btn_container = tk.Frame(master=btn_panel, bg=button_panel_bg)
        btn_container.grid_columnconfigure(0, weight=1)
        btn_container.grid(row=0, column=0, rowspan=len(btn_strings), padx=20, pady=100)

        for inx, img in enumerate(btn_strings):
            btn = tk.Button(btn_container,
                            text=btn_strings[inx],
                            font="BahnschriftLight 15 bold",
                            borderwidth=0,
                            bg=button_panel_bg,
                            fg="#099FFF",
                            activebackground=button_panel_bg,
                            activeforeground="white")

            btn.grid_columnconfigure(1, weight=1)
            btn.grid_rowconfigure(inx, weight=1)
            btn.grid(row=inx, column=1, padx=15, pady=15, sticky=tk.W)

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
