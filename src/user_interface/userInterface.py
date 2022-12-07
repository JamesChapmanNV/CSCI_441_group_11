import os
import sys
import tkinter as tk

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.user_interface.frames.loginFrame import LoginFrame
from src.user_interface.frames.mainFrame import MainFrame
from user_interface.frames.management_frames.manageAppointmentFrame import ManageApptFrame
from src.user_interface.utils.frameUtils import set_ui_properties

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

        self.show_frame(LoginFrame)

    def show_frame(self, page_name):
        frame_name_str = page_name.__name__ if not isinstance(page_name, str) else page_name

        frame = self.frames[frame_name_str]
        frame.grid(row=0, column=0, sticky="nsew")

        if frame_name_str != "LoginFrame":
            self.__popup = tk.Menu(self, tearoff=0)
            self.__popup.add_command(label="Add Appointment", command=self.show_manage_appt_frame)

            if frame_name_str == "MainFrame":
                set_ui_properties(self, width=900, height=600, is_resizable=True)

            self.bind("<Button-3>", self.show_popup_menu)
        elif frame_name_str == "LoginFrame":
            set_ui_properties(self, width=372, height=175, is_resizable=False)

        frame.tkraise()

    def show_popup_menu(self, event):
        try:
            self.__popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.__popup.grab_release()

    def show_manage_appt_frame(self):
        ManageApptFrame(self, self.frames["MainFrame"])


if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
