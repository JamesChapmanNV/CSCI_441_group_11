import tkinter
import tkinter.ttk as ttk


class Tree(ttk.Treeview):
    def __init__(self, master, columns):
        self.master = master
        super().__init__(self.master, columns=columns)

        # Set column properties
        self.__configure_style()

    def __configure_vertical_scrollbar(self):
        vertical_scrollbar = ttk.Scrollbar(self,
                                           orient="vertical",
                                           command=self.yview)
        self.configure(yscrollcommand=vertical_scrollbar.set)

        vertical_scrollbar.pack(expand=False, side=tkinter.RIGHT, fill=tkinter.Y)

    def __configure_style(self):
        # Alternate row colors
        self.tag_configure("evenrow", background='lightgray')
        self.tag_configure("oddrow", background='white')

        self['show'] = 'headings'

        self.grid_columnconfigure(0, weight=1)
        self.grid(row=1, column=0, sticky='nsew')

        # Add vertical scrollbar
        self.__configure_vertical_scrollbar()

        # Set base style
        style = ttk.Style()
        style.theme_use("winnative")
        style.map("Treeview")
