import datetime
import tkinter as tk
from src.user_interface.frames.mainFrame import MainFrame

width = 800
height = 500


class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title
        self.wm_title("Carpe Diem Massage Company")

        # Set width, height, and frame grid properties
        self.__set_ui_properties(width=width, height=height)

    def __set_ui_properties(self, width, height):
        # Piece of code to center the window on the screen when it starts up
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coord = int((screen_width / 2) - (width / 2))
        y_coord = int((screen_height / 2) - (height / 2))
        self.geometry("{}x{}+{}+{}".format(width, height, x_coord, y_coord))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = UserInterface()
    main_frame = MainFrame(app)
    app.mainloop()
