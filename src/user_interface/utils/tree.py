import tkinter.ttk as ttk


class Tree(ttk.Treeview):
    def __init__(self, master, columns):
        self.master = master
        super().__init__()

        # Set column properties
        self.configure(columns=columns)

        self.__configure_style()

    def __configure_vertical_scrollbar(self):
        vertical_scrollbar = ttk.Scrollbar(self.master,
                                           orient="vertical",
                                           command=self.yview)

        vertical_scrollbar.grid(column=1, row=0, sticky='NS')
        self.configure(yscrollcommand=vertical_scrollbar.set)

    def __configure_style(self):
        # Alternate row colors
        self.tag_configure("evenrow", background='lightgray')
        self.tag_configure("oddrow", background='white')

        # Add vertical scrollbar
        self.__configure_vertical_scrollbar()

        self['show'] = 'headings'
        self.grid(row=0, column=0, sticky='nsew')

        # Set base style
        style = ttk.Style()
        style.theme_use("alt")
        style.map("Treeview")
