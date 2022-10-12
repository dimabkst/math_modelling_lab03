from tkinter import *
from tkinter import ttk


class results_output:

    def __init__(self, root):

        s = ttk.Style()
        s.configure("TopWhiteBg.TFrame", background="white", borderwidth=5, relief='raised')
        s.configure("VectorWhiteBg.TFrame", background="white", borderwidth=5, relief="solid")
        s.configure("WhiteBg.TFrame", background="white")
        s.configure("WhiteBg.TLabel", background="white")

        # Frames
        self.root = ttk.Frame(root, style="TopWhiteBg.TFrame", padding="3 3 12 12")
        self.root.grid(column=0, row=0, sticky=(N, W, E, S))
        #

        # Align
        self.align_rows_cols(self.root)
        #

    def align_rows_cols(self, frame):
        cols_num, rows_num = frame.grid_size()
        for i in range(rows_num):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(cols_num):
            frame.grid_columnconfigure(j, weight=1)
