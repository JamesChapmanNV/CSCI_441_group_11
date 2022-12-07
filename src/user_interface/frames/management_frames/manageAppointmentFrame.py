import tkinter as tk

import customerManager
from src.user_interface.utils import appointments
from src import appointmentManager
from src import masseuseManager
from datetime import datetime, timedelta


class ManageApptFrame(tk.Toplevel):
    def __init__(self, container, main_frame):
        super().__init__()
        self.container = container
        self.main_frame = main_frame

        self.__show_inner_frame()
        self.wm_title("Manage Appointment")

    def __show_inner_frame(self):
        f = ('Times', 14)
        self.__inner_frame = tk.Frame(self, bd=2, bg='#CCCCCC', relief=tk.SOLID, padx=10, pady=10)

        tk.Label(self.__inner_frame,
                 text="Appointment ID",
                 bg='#CCCCCC',
                 font=f).grid(row=0, column=0, pady=10)
        tk.Label(self.__inner_frame,
                 text="123",
                 bg='#CCCCCC',
                 font=f).grid(row=0, column=1, pady=10)
        tk.Label(self.__inner_frame,
                 text="Date",
                 bg='#CCCCCC',
                 font=f).grid(row=1, column=0, pady=10)
        tk.Label(self.__inner_frame,
                 text="Time",
                 bg='#CCCCCC',
                 font=f).grid(row=2, column=0, pady=10)
        tk.Label(self.__inner_frame,
                 text="Masseuse",
                 bg='#CCCCCC',
                 font=f).grid(row=3, column=0, pady=10)
        tk.Label(self.__inner_frame,
                 text="Customer",
                 bg='#CCCCCC',
                 font=f).grid(row=4, column=0, pady=10)
        tk.Label(self.__inner_frame,
                 text="Room #",
                 bg='#CCCCCC',
                 font=f).grid(row=5, column=0, pady=10)

        # Get appointmentID if available


        # Input values
        self.__date_var = tk.StringVar()
        self.__time_var = tk.StringVar(self, value="Time")
        self.__masseuse_var = tk.StringVar(self, value="Masseuse")
        self.__customer_var = tk.StringVar(self, value="Customer")

        # Set callback
        self.__date_var.trace_add('write', callback=self.my_callback)

        # self.date_input = tk.Entry(self.__inner_frame, textvariable=self.__date_var, font=f)
        self.date_input = appointments.Appointments(self.__inner_frame, self.__date_var)
        '''
        self.show_id = tk.StringVar(self, value="123")
        This is probably not necessary. Trying to figure out how to update appointmentID correctly.
        '''

        rooms = ["1", "2", "3", "4", ]
        room_select = tk.StringVar()
        room_select.set(rooms[0])

        # self.time_input = tk.Entry(self.__inner_frame, font=f)

        # current_time = tk.StringVar()
        # self.time_input = tk.OptionMenu(self.__inner_frame, self.__time_var, *self.get_times())

        masseuse_choices = masseuseManager.get_all_masseuse_names()
        self.masseuse_input = tk.OptionMenu(self.__inner_frame, self.__masseuse_var, *masseuse_choices)

        customer_choices = customerManager.get_all_customer_names()
        self.customer_input = tk.OptionMenu(self.__inner_frame, self.__customer_var, *customer_choices)
        self.room_num = tk.OptionMenu(self.__inner_frame, room_select, *rooms)
        save_button = tk.Button(self.__inner_frame,
                                width=15,
                                text='Save',
                                font=f,
                                relief=tk.SOLID,
                                cursor='hand2',
                                command=self.__save_appointment)

        delete_button = tk.Button(self.__inner_frame,
                                  width=15,
                                  text='Delete',
                                  font=f,
                                  relief=tk.SOLID,
                                  cursor='hand2',
                                  command=self.__delete_appointment)
        '''
        self.show_id.grid(row=0, column=1, pady=10, padx=20)
        Trying to get appointmentID to display correctly
        '''
        self.date_input.grid(row=1, column=1, pady=10, padx=20)
        self.time_input.grid(row=2, column=1, pady=10, padx=20)
        self.masseuse_input.grid(row=3, column=1, pady=10, padx=20)
        self.customer_input.grid(row=4, column=1, pady=10, padx=20)
        self.room_num.grid(row=5, column=1, pady=10, padx=20)
        save_button.grid(row=6, column=0, pady=10, padx=15)
        delete_button.grid(row=6, column=1, pady=10, padx=15)
        # self.date_input.bind("<<CalendarSelected>>", lambda: print(self.date_input.selection_get()))

        self.__inner_frame.pack()

    def update_appointment(self, date, time, masseuse, customer):
        self.__date_var.set(date)
        self.__time_var.set(time)
        self.__masseuse_var.set(masseuse)
        self.__customer_var.set(customer)

    def __save_appointment(self):
        print(self.__date_var.get(), self.__time_var.get(), self.__masseuse_var.get())
        time1 = datetime.strptime(self.__time_var.get(), '%I:%M %p').strftime('%H')
        dt = datetime.strptime(self.__date_var.get(), '%m/%d/%y') + timedelta(hours=int(time1))
        appointmentManager.insert_appointment(f'{dt}', 1, 'BOOKED', 61789, 10325)
        self.main_frame.make_appointment_scheduler()

    def __delete_appointment(self):
        appointmentManager.delete_appointment(902)
        self.main_frame.make_appointment_scheduler()


    def my_callback(self, var, index, mode):
        print("Traced variable {}".format(self.__date_var.get()))
        self.time_input = tk.OptionMenu(self.__inner_frame, self.__time_var, *self.get_times())

        '''if self.__date_var.get() != "10/30/22":
            self.__time_var.set("Test")'''

    def get_times(self):
        seletedDate = self.__date_var.get()
        if (seletedDate == '11/6/22'):
            return [1, 2, 3]
        if (seletedDate == ''):
            return [
                '9:00 AM',
                '10:00 AM',
                '11:00 AM',
                '12:00 PM',
                '1:00 PM',
                '2:00 PM',
                '3:00 PM',
                '4:00 PM']

        times = []
        times_dict = {
            '9:00 AM': 0,
            '10:00 AM': 0,
            '11:00 AM': 0,
            '12:00 PM': 0,
            '1:00 PM': 0,
            '2:00 PM': 0,
            '3:00 PM': 0,
            '4:00 PM': 0}

        appointments = appointmentManager.get_appointments(
            datetime.strptime(seletedDate, '%m/%d/%y').strftime("%Y-%m-%d"))
        # each appointment includes [appointmentId, start_time, room, status, masseuseId, customerId]

        for appointment in appointments:
            dt = appointment[1]
            time = dt.strftime("%#I:%M %p")
            times_dict[time] = times_dict[time] + 1

        # count number of appointments at that time scheduled
        # because there are 3 rooms, if <3, there is an appointment available
        for time in times_dict:
            if (times_dict[time] < 3):
                times.append(time)

        print(times)
        return times
