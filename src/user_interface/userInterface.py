import os
import sys
import tkinter as tk
import tkinter.ttk as ttk

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.user_interface.frames.loginFrame import LoginFrame
from src.user_interface.frames.mainFrame import MainFrame
from src.user_interface.frames.manageAppointmentFrame import ManageApptFrame

frames_classes = (MainFrame, LoginFrame)


class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title
        self.wm_title("Carpe Diem Massage Company")

        self.__popup = None

        self.frames = {}
        for F in frames_classes:
            self.frames[F.__name__] = F(container=self)

        # self.show_frame(LoginFrame)
        self.show_frame(MainFrame)

    def show_frame(self, page_name):
        frame_name_str = page_name.__name__ if not isinstance(page_name, str) else page_name

        frame = self.frames[frame_name_str]
        frame.grid(row=0, column=0, sticky="nsew")

        if frame_name_str != "LoginFrame":
            self.__popup = tk.Menu(self, tearoff=0)
            self.__popup.add_command(label="Add Appointment", command=self.show_manage_appt_frame)

            if frame_name_str == "MainFrame":
                self.set_ui_properties(width=900, height=600, is_resizable=True)

            self.bind("<Button-3>", self.show_popup_menu)
        elif frame_name_str == "LoginFrame":
            self.set_ui_properties(width=372, height=175, is_resizable=False)

        frame.tkraise()

    def show_popup_menu(self, event):
        try:
            self.__popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.__popup.grab_release()

    def show_manage_appt_frame(self):
        ManageApptFrame(self)

    def set_ui_properties(self, width, height, is_resizable):
        # Piece of code to center the window on the screen when it starts up
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coord = int((screen_width / 2) - (width / 2))
        y_coord = int((screen_height / 2) - (height / 2))
        self.geometry("{}x{}+{}+{}".format(width, height, x_coord, y_coord))
        self.resizable(is_resizable, is_resizable)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
