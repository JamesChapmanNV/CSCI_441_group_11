import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkfont

from src.user_interface.utils.tree import Tree
from src import appointmentManager
from src import masseuseManager
from src import customerManager
from src.user_interface.frames.manageAppointmentFrame import ManageApptFrame

# Frame background color
color_dark_gray = "gray17"
# Text font color
color_light_blue = "#099FFF"

btn_strings = ["Appointments", "Customers", "Masseuses", "Admin"]


class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button_panel_hidden = False
        self.__show_buttons()

        # Show appointments by default on UI construct
        self.__show_appointment_container()

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
                             text="Add Appointment",
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
        ManageApptFrame(container=self.container)

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
        self.__make_appointment_scheduler()

    def __make_appointment_scheduler(self):
        columns = ('appt_num', 'date', 'time', 'room_num', "assigned_to", "customer")
        tree = Tree(master=self.__sched_container, columns=columns)

        for column in columns:
            tree.heading(column,
                         text=column.replace("_", " ").replace("num", "#").title(),
                         anchor="w")
            tree.column(column,
                        width=tkfont.Font().measure(column.title()),
                        stretch=True if column == columns[-1] else False,
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
            tree.insert('', tk.END, values=tree_entry, tags=(style_tag,))

            # Dynamically set column width if a value entered extends the bounds of current width
            for entry_index, val in enumerate(tree_entry):
                col_w = tkfont.Font().measure(val)
                if tree.column(columns[entry_index], width=None) < col_w:
                    tree.column(columns[entry_index], width=col_w)

    def __toggle_menu_panel(self):
        if not self.button_panel_hidden:
            self.__btn_panel.grid_remove()
            self.button_panel_hidden = True
        else:
            self.__btn_panel.grid()
            self.button_panel_hidden = False
