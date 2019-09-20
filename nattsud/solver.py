#!/c/Users/David/AppData/Local/Programs/Python/Python37-32/python


class Solver:

    def __init__(self):
        self.given_cells = {}
        self.set_cells = {}

    def set_givens(self, cells):
        for cell, value in cells.items():
            if value is not "":
                self.given_cells[cell] = value

        return self.given_cells
