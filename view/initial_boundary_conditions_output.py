from tkinter import *
from tkinter import ttk

MAX_DEFAULT_VALUE = 7 + 1
COMBOBOX_WIDTH = 3
ENTRY_WIDTH = 10


class initial_boundary_conditions_input:

    def __init__(self, root):
        s = ttk.Style()
        s.configure("TopWhiteBg.TFrame", background="white", borderwidth=5, relief='raised')
        s.configure("WhiteBg.TFrame", background="white")
        s.configure("WhiteBg.TLabel", background="white")

        # Frames
        self.root = ttk.Frame(root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.root.grid()

        self.align_rows_cols(self.root)

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)
