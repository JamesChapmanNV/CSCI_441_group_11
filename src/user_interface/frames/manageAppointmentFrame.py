import tkinter as tk


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

        self.date_input = tk.Entry(self.__inner_frame, font=f)
        self.time_input = tk.Entry(self.__inner_frame, font=f)

        choices = {"Landon", "Dan", "James"}
        default_choice = tk.StringVar(self, value="Landon")
        self.masseuse_input = tk.OptionMenu(self.__inner_frame, default_choice, *choices)
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

        self.__inner_frame.pack()
