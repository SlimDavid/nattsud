#!/c/Users/David/AppData/Local/Programs/Python/Python37-32/python


class Solver:

    def __init__(self):
        self.given_cells = {}
        self.set_cells = {}

    def set_givens(self, cells):
        print("GIVENS")

        for cell, value in cells.items():
            print(cell, ":", value)
            if value is not "":
                self.given_cells[cell] = value
                print("value:", value)

        return self.given_cells
