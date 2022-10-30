import tkinter as tk
from user_interface.utils import Appointments


class ManageApptFrame(tk.Toplevel):
    def __init__(self, container):
        super().__init__()
        self.container = container

        self.__show_inner_frame()
        self.wm_title("Manage Appointment")

    def __show_inner_frame(self):
        f = ('Times', 14)
        self.__inner_frame = tk.Frame(self, bd=2, bg='#CCCCCC', relief=tk.SOLID, padx=10, pady=10)

        tk.Label(self.__inner_frame,
                 text="Date",
                 bg='#CCCCCC',
                 font=f).grid(row=0, column=0, sticky=tk.W, pady=10)
        tk.Label(self.__inner_frame,
                 text="Time",
                 bg='#CCCCCC',
                 font=f).grid(row=1, column=0, pady=10)
        tk.Label(self.__inner_frame,
                 text="Masseuse",
                 bg='#CCCCCC',
                 font=f).grid(row=2, column=0, pady=10)

        # Input values
        self.__date_var = tk.StringVar()
        self.__time_var = tk.StringVar(self, value="9")
        self.__masseuse_var = tk.StringVar(self, value="Landon")

        # Set callback
        self.__date_var.trace_add('write', callback=self.my_callback)

        # self.date_input = tk.Entry(self.__inner_frame, textvariable=self.__date_var, font=f)
        self.date_input = Appointments.Appointments(self.__inner_frame, self.__date_var)

        # self.time_input = tk.Entry(self.__inner_frame, font=f)

        # current_time = tk.StringVar()
        self.time_input = tk.OptionMenu(self.__inner_frame, self.__time_var, *self.get_times())

        choices = {"Landon", "Dan", "James"}

        self.masseuse_input = tk.OptionMenu(self.__inner_frame, self.__masseuse_var, *choices)
        save_button = tk.Button(self.__inner_frame,
                                width=15,
                                text='Save',
                                font=f,
                                relief=tk.SOLID,
                                cursor='hand2')

        self.date_input.grid(row=0, column=1, pady=10, padx=20)
        self.time_input.grid(row=1, column=1, pady=10, padx=20)
        self.masseuse_input.grid(row=2, column=1, pady=10, padx=20)
        save_button.grid(row=3, column=1, pady=10, padx=20)

        # self.date_input.bind("<<CalendarSelected>>", lambda: print(self.date_input.selection_get()))

        self.__inner_frame.pack()

    def my_callback(self, var, index, mode):
        print("Traced variable {}".format(self.__date_var.get()))
        if self.__date_var.get() != "10/30/22":
            self.__time_var.set("Test")

    def get_times(self):
        times = []
        for i in range(8):
            times.append(i + 9)
        return times
