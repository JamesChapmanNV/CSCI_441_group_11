import tkinter as tk
import tkinter.font as tkfont
from datetime import datetime

from src.user_interface.utils.tree import Tree
from src import appointmentManager
from src import masseuseManager
from src import customerManager
from src.user_interface.frames.management_frames.manageCustomerFrame import ManageCustomerFrame
from src.user_interface.utils.frameUtils import set_ui_properties

# Frame background color
color_dark_gray = "gray17"
# Text font color
color_light_blue = "#099FFF"

btn_strings = ["Appointments", "Customers", "Masseuses", "Admin"]


class CustomersFrame(tk.Toplevel):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button_panel_hidden = False
        if not self.button_panel_hidden:
            self.__show_buttons()

        # Show appointments by default on UI construct
        self.__show_appointment_container()

        set_ui_properties(self, width=900, height=600, is_resizable=True)

    def __show_buttons(self):

        # Split button column vertically in half
        self.__btn_panel = tk.Frame(master=self, bg=color_dark_gray)
        self.__btn_panel.grid_rowconfigure(0, weight=1)
        self.__btn_panel.grid_columnconfigure(1, weight=1)
        self.__btn_panel.grid(row=0, column=1, sticky=tk.NSEW)

        btn_container = tk.Frame(master=self.__btn_panel, bg=color_dark_gray)
        btn_container.grid(row=0, column=0, padx=20, pady=100)

        for inx, img in enumerate(btn_strings):
            btn = tk.Button(btn_container,
                            text=btn_strings[inx],
                            font="BahnschriftLight 15 bold",
                            borderwidth=0,
                            bg=color_dark_gray,
                            fg=color_light_blue,
                            activebackground=color_dark_gray,
                            activeforeground="white")

            btn.grid_columnconfigure(1, weight=1)
            btn.grid_rowconfigure(inx, weight=1)
            btn.grid(row=inx, column=1, padx=15, pady=15, sticky=tk.W)

        '''
            Add appointment button
        '''
        action_btn_container = tk.Frame(master=self.__btn_panel, bg=color_dark_gray)
        action_btn_container.grid(row=1, column=0, padx=20, pady=20)
        add_appt = tk.Button(action_btn_container,
                             text="Add Customer",
                             font="BahnschriftLight 15 bold",
                             borderwidth=0,
                             bg=color_dark_gray,
                             fg="white",
                             activebackground=color_dark_gray,
                             activeforeground="white",
                             command=self.__show_manage_appt_frame)

        add_appt.grid_columnconfigure(1, weight=1)
        add_appt.grid_rowconfigure(0, weight=1)
        add_appt.grid(row=0, column=1, padx=15, pady=15, sticky=tk.W)

    def __show_manage_appt_frame(self):
        ManageCustomerFrame(container=self.container, main_frame=self)

    def __show_appointment_container(self):

        self.__sched_container = tk.Frame(master=self)
        self.__sched_container.grid_rowconfigure(0, weight=1)
        self.__sched_container.grid_rowconfigure(1, weight=50)
        self.__sched_container.grid_columnconfigure(0, weight=1)
        self.__sched_container.grid(row=0, column=0, sticky=tk.NSEW)

        '''
        Horizontal bar
        '''
        nav_btn_container = tk.Frame(master=self.__sched_container, bg=color_dark_gray)
        nav_btn_container.grid_rowconfigure(0, weight=1)
        nav_btn_container.grid_columnconfigure(0, weight=1)
        nav_btn_container.grid(row=0, column=0, sticky=tk.NSEW)
        nav_btn = tk.Button(nav_btn_container,
                            text="MENU",
                            font="BahnschriftLight 15 bold",
                            fg=color_light_blue,
                            bg=color_dark_gray,
                            activebackground=color_dark_gray,
                            activeforeground="white",
                            bd=0,
                            padx=20,
                            command=self.__toggle_menu_panel)
        nav_btn.grid(row=0, column=0, sticky=tk.E)

        '''
        Appointment scheduler
        '''
        self.make_appointment_scheduler()

    def make_appointment_scheduler(self):
        columns = ('customerId', 'name', 'address', 'email', "phone")
        self.tree_view = Tree(master=self.__sched_container, columns=columns)

        for column in columns:
            self.tree_view.heading(column,
                                   text=column.replace("_", " ").replace("num", "#").title(),
                                   anchor="w")
            self.tree_view.column(column,
                                  width=tkfont.Font().measure(column.title()),
                                  stretch=True if column == columns[-1] else False,
                                  minwidth=50,
                                  anchor="w")

        tree_entries = []
        customers = customerManager.get_customers()
        # appointments = appointmentManager.get_future_booked_appointments()
        # return to an array of all booked appointments
        # each appointment includes [appointmentId, start_time, room, status, masseuseId, customerId]
        for customer in customers:
            customerId = customer[0]
            name = customer[1]
            address = customer[2]
            email = customer[3]
            phone = customer[4]
            entry = (f'{customerId}', f'{name}', f'{address}', f'{email}', f'{phone}')
            tree_entries.append(entry)

        for tree_index, tree_entry in enumerate(tree_entries):

            # Apply style tag based on whether the index of the entry is even or odd
            style_tag = 'evenrow' if tree_index % 2 == 0 else 'oddrow'
            self.tree_view.insert('', tk.END, values=tree_entry, tags=(style_tag,))

            # Dynamically set column width if a value entered extends the bounds of current width
            for entry_index, val in enumerate(tree_entry):
                col_w = tkfont.Font().measure(val)
                if self.tree_view.column(columns[entry_index], width=None) < col_w:
                    self.tree_view.column(columns[entry_index], width=col_w)

        self.tree_view.bind('<Double-1>', self.__on_tree_double_click)

    def __on_tree_double_click(self, event):
        selected_values = list(self.tree_view.item(self.tree_view.selection()[0]).values())[2]
        update_appt_frame = ManageCustomerFrame(container=self.container, main_frame=self)
        update_appt_frame.update_appointment(date=datetime.strptime(selected_values[1], '%Y-%m-%d').strftime('%m/%d/%y'),
                                             time=selected_values[2],
                                             masseuse=selected_values[4],
                                             customer=selected_values[5])

    def __toggle_menu_panel(self):
        if not self.button_panel_hidden:
            self.__btn_panel.grid_remove()
            self.button_panel_hidden = True
        else:
            self.__btn_panel.grid()
            self.button_panel_hidden = False

