import tkinter as tk

from src import customerManager
from src.user_interface.utils import appointments
from src import appointmentManager
from src import masseuseManager
from datetime import datetime, timedelta
import random


class ManageMasseuseFrame(tk.Toplevel):
    def __init__(self, container, main_frame):
        super().__init__()
        self.container = container
        self.main_frame = main_frame

        self.__show_inner_frame()
        self.wm_title("Add masseuse")

    def __show_inner_frame(self):
        f = ('Times', 14)
        self.__inner_frame = tk.Frame(self, bd=2, bg='#CCCCCC', relief=tk.SOLID, padx=10, pady=10)

        tk.Label(self.__inner_frame,
                 text="Name",
                 bg='#CCCCCC',
                 font=f).grid(row=0, column=0, sticky=tk.W, pady=10)
        tk.Label(self.__inner_frame,
                 text="Email",
                 bg='#CCCCCC',
                 font=f).grid(row=1, column=0, pady=10)
        tk.Label(self.__inner_frame,
                 text="Address",
                 bg='#CCCCCC',
                 font=f).grid(row=2, column=0, pady=10)
        tk.Label(self.__inner_frame,
                 text="Phone",
                 bg='#CCCCCC',
                 font=f).grid(row=3, column=0, pady=10)

        self.name_input = tk.Text(self.__inner_frame, height=2, width=20)
        self.address_input = tk.Text(self.__inner_frame, height=2, width=20)
        self.email_input = tk.Text(self.__inner_frame, height=2, width=20)
        self.phone_input = tk.Text(self.__inner_frame, height=2, width=20)

        save_button = tk.Button(self.__inner_frame,
                                width=15,
                                text='Save',
                                font=f,
                                relief=tk.SOLID,
                                cursor='hand2',
                                command=self.__save_masseuse)

        self.name_input.grid(row=0, column=1, pady=10, padx=20)
        self.address_input.grid(row=1, column=1, pady=10, padx=20)
        self.email_input.grid(row=2, column=1, pady=10, padx=20)
        self.phone_input.grid(row=3, column=1, pady=10, padx=20)
        save_button.grid(row=4, column=1, pady=10, padx=20)

        self.__inner_frame.pack()

    def __save_masseuse(self):
        masseuseManager.insert_masseuse(random.randint(10000, 99999), self.name_input.get("1.0", 'end-1c'),
                                        self.address_input.get("1.0", 'end-1c'),
                                        self.email_input.get("1.0", 'end-1c'),
                                        self.phone_input.get("1.0", 'end-1c'))
        self.destroy()
        self.main_frame.make_appointment_scheduler()
