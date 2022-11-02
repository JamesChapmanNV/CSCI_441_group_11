import tkinter as tk
from src.user_interface.utils import Appointments
from src import appointmentManager
from src import masseuseManager
from datetime import datetime

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
        self.__time_var = tk.StringVar(self, value="Time")
        self.__masseuse_var = tk.StringVar(self, value="Masseuse")

        # Set callback
        self.__date_var.trace_add('write', callback=self.my_callback)

        # self.date_input = tk.Entry(self.__inner_frame, textvariable=self.__date_var, font=f)
        self.date_input = Appointments.Appointments(self.__inner_frame, self.__date_var)

        # self.time_input = tk.Entry(self.__inner_frame, font=f)

        # current_time = tk.StringVar()
        #self.time_input = tk.OptionMenu(self.__inner_frame, self.__time_var, *self.get_times())

        choices = masseuseManager.get_all_masseuse_names()

        self.masseuse_input = tk.OptionMenu(self.__inner_frame, self.__masseuse_var, *choices)
        save_button = tk.Button(self.__inner_frame,
                                width=15,
                                text='Save',
                                font=f,
                                relief=tk.SOLID,
                                cursor='hand2',
                                command=self.__save_appointment)

        self.date_input.grid(row=0, column=1, pady=10, padx=20)
        self.time_input.grid(row=1, column=1, pady=10, padx=20)
        self.masseuse_input.grid(row=2, column=1, pady=10, padx=20)
        save_button.grid(row=3, column=1, pady=10, padx=20)

        # self.date_input.bind("<<CalendarSelected>>", lambda: print(self.date_input.selection_get()))

        self.__inner_frame.pack()

    def __save_appointment(self):
        print(self.__date_var.get(), self.__time_var.get(), self.__masseuse_var.get())

    def my_callback(self, var, index, mode):
        print("Traced variable {}".format(self.__date_var.get()))
        self.time_input = tk.OptionMenu(self.__inner_frame, self.__time_var, *self.get_times())

        '''if self.__date_var.get() != "10/30/22":
            self.__time_var.set("Test")'''

    def get_times(self):
        seletedDate = self.__date_var.get()
        if(seletedDate == '11/6/22'):
            return [1,2,3]
        if(seletedDate == ''):
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
            '9:00 AM' : 0, 
            '10:00 AM' : 0, 
            '11:00 AM' : 0, 
            '12:00 PM' : 0, 
            '1:00 PM' : 0, 
            '2:00 PM' : 0, 
            '3:00 PM' : 0, 
            '4:00 PM' : 0 } 
        
        appointments = appointmentManager.get_appointments(datetime.strptime(seletedDate,'%m/%d/%y').strftime("%Y-%m-%d"))
        # each appointment includes [appointmentId, start_time, room, status, masseuseId, customerId]
        
        for appointment in appointments:
            dt = appointment[1]
            time = dt.strftime("%#I:%M %p")
            times_dict[time] = times_dict[time]+1
            
        # count number of appointments at that time scheduled
        # because there are 3 rooms, if <3, there is an appointment available
        for time in times_dict:
            if(times_dict[time] < 3):
                times.append(time)
        
        print(times)
        return times
        
       