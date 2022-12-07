
def set_ui_properties(container, width, height, is_resizable):
    # Piece of code to center the window on the screen when it starts up
    screen_width = container.winfo_screenwidth()
    screen_height = container.winfo_screenheight()
    x_coord = int((screen_width / 2) - (width / 2))
    y_coord = int((screen_height / 2) - (height / 2))
    container.geometry("{}x{}+{}+{}".format(width, height, x_coord, y_coord))
    container.resizable(is_resizable, is_resizable)

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)


