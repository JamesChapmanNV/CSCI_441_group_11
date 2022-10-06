import datetime
import tkinter as tk
import tkinter.font as tkfont
import random

from src.user_interface.utils import toolbar
from src.user_interface.utils.tree import Tree
from src import appointmentManager
from src import masseuseManager
from src import customerManager

width = 800
height = 500


class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title
        self.wm_title("Carpe Diem Massage Company")

        # Declare expected class attributes
        self.tree = None

        # Set width, height, and frame grid properties
        self.__set_ui_properties(width=width, height=height)

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
            

        tree_entries = []
        appointments = appointmentManager.get_future_booked_appointments()
        # return to an array of all booked appointments
        # each appointment includes [appointmentId, start_time, room, status, masseuseId, customerId]
        for appointment in appointments:
            appt_num = appointment[0]
            dt = appointment[1]
            date = dt.strftime('%Y-%m-%d')
            time = dt.strftime('%H:%M')
            room_num = appointment[2]
            assigned_to = masseuseManager.get_masseuse_name(appointment[4])
            customer = customerManager.get_customer_name(appointment[5])
            entry = (f'{appt_num}', f'{date}', f'{time}', f'{room_num}', f'{assigned_to}', f'{customer}')
            tree_entries.append(entry)
        
        # ####### Using this block for testing
        # test_num_of_appointments = 50
        # tree_entries = []
        # for appointment in range(test_num_of_appointments):
        #     # Making a bunch of random rows to test the treeview
        #     appt_num = random.randint(10000, 99999)
        #     now = datetime.datetime.now()
        #     date = now.strftime('%Y-%m-%d')
        #     time = now.strftime('%H:%M')
        #     room_num = random.randint(1, 3)
        #     assigned_to = f"Masseuse {random.randint(1, 3)}"
        #     customer = "Firstname, Lastname"
        #     entry = (f'{appt_num}', f'{date}', f'{time}', f'{room_num}', f'{assigned_to}', f'{customer}')
        #     tree_entries.append(entry)
        # #######

        for tree_index, tree_entry in enumerate(tree_entries):

            # Apply style tag based on whether the index of the entry is even or odd
            style_tag = 'evenrow' if tree_index % 2 == 0 else 'oddrow'
            self.tree.insert('', tk.END, values=tree_entry, tags=(style_tag,))

            # Dynamically set column width if a value entered extends the bounds of current width
            for entry_index, val in enumerate(tree_entry):
                col_w = tkfont.Font().measure(val)
                if self.tree.column(columns[entry_index], width=None) < col_w:
                    self.tree.column(columns[entry_index], width=col_w)

    def __set_ui_properties(self, width, height):

        # Piece of code to center the window on the screen when it starts up
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coord = int((screen_width / 2) - (width / 2))
        y_coord = int((screen_height / 2) - (height / 2))
        self.geometry("{}x{}+{}+{}".format(width, height, x_coord, y_coord))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
