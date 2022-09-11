import tkinter as tk
import toolbar as tb


class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()

        self.wm_title("Carpe Diem Massage Company")
        self.set_ui_properties(width=600, height=400)

        toolbar = tb.Toolbar(self)

    def set_ui_properties(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coord = int((screen_width / 2) - (width / 2))
        y_coord = int((screen_height / 2) - (height / 2))

        self.geometry("{}x{}+{}+{}".format(width, height, x_coord, y_coord))


if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
