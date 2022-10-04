import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox


class LoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        self.__show_inner_frame()

    def __validate_login(self):
        uname = self.user_input.get()
        password = self.pass_input.get()

        if uname == "" and password == "":
            tk.messagebox.showinfo("", "Blank Not allowed")
        elif uname == "Admin" and password == "123":
            self.destroy()
            self.container.show_frame("MainFrame")
        else:
            messagebox.showinfo("", "Incorrent Username and Password")

    def __show_inner_frame(self):
        f = ('Times', 14)
        self.__inner_frame = tk.Frame(self, bd=2, bg='#CCCCCC', relief=tk.SOLID, padx=10, pady=10)

        tk.Label(self.__inner_frame,
                 text="Enter Username",
                 bg='#CCCCCC',
                 font=f).grid(row=0, column=0, sticky=tk.W, pady=10)
        tk.Label(self.__inner_frame,
                 text="Enter Password",
                 bg='#CCCCCC',
                 font=f).grid(row=1, column=0, pady=10)

        self.user_input = tk.Entry(self.__inner_frame, font=f)
        self.pass_input = tk.Entry(self.__inner_frame, font=f, show='*')
        login_button = tk.Button(self.__inner_frame,
                                 width=15,
                                 text='Login',
                                 font=f,
                                 relief=tk.SOLID,
                                 cursor='hand2',
                                 command=self.__validate_login)

        self.user_input.grid(row=0, column=1, pady=10, padx=20)
        self.pass_input.grid(row=1, column=1, pady=10, padx=20)
        login_button.grid(row=2, column=1, pady=10, padx=20)

        self.__inner_frame.pack()
