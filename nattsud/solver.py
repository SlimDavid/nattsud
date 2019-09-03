#!/c/Users/David/AppData/Local/Programs/Python/Python37-32/python

import tkinter as tk

class Solver:

    def __init__(self):
        self.given_cells = {}
        self.set_cells = {}

    def set_givens(self, cells):
        print("GIVENS")
        for cell in cells:
            print(cell, ":", cells[cell].get())
            if cells[cell].get() is not "":
                self.given_cells[cell] = cells[cell].get()
                cells[cell]['state'] = tk.DISABLED
                # cells[cell].configure(bg = "blue")
                print("value:", cells[cell].get())
        print("Given cells:")
        for given_cell in self.given_cells:
            print(given_cell, "", self.given_cells[cell])
            # given_cell['state'] = tk.DISABLED
