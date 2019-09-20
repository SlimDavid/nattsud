#!/c/Users/David/AppData/Local/Programs/Python/Python37-32/python
import string
import tkinter as tk
from tkinter.font import Font

from nattsud.solver import Solver

CELL_SIZE = 30
POSSIBLES_SIZE = 50
X_STARTING_POINT_OF_POSSIBLES = 14 * CELL_SIZE
COLOR = "white"
INFO_FIELD_CHAR_SIZE=50

CANVAS_SIZE_X = X_STARTING_POINT_OF_POSSIBLES + POSSIBLES_SIZE * 10
CANVAS_SIZE_Y = CELL_SIZE * 19

cells = dict()
tk_cells = dict()
possibles = dict()
info_field = dict()
solver = Solver()


def main():
    main_window = create_main_window()

    c = tk.Canvas(main_window, bg=COLOR)
    c.place(width=CANVAS_SIZE_X, height=CANVAS_SIZE_Y)

    global start_button
    start_button = tk.Button(c, text="Set cells\n(1st: givens)", command=set_start)
    calc_button = tk.Button(c, text="Calculate all possible\nvalues (simple)", command=calculate_possible_numbers)
    reduce_button = tk.Button(c, text="Reduce all possible\nvalues", command=reduce_possible_numbers)
    c.create_window(CELL_SIZE*0.5, CELL_SIZE*11, window=start_button, anchor=tk.NW)
    c.create_window(CELL_SIZE*3, CELL_SIZE*11, window=calc_button, anchor=tk.NW)
    c.create_window(CELL_SIZE*7.1, CELL_SIZE*11, window=reduce_button, anchor=tk.NW)

    draw_xy_labels_for_possibles(c)
    put_possible_numbers_fields(c)
    draw_lines_for_possibles(c)

    draw_xy_labels_for_cells(c)
    draw_lines_for_cells(c)
    put_input_fields(c)

    info_field[0] = put_info_field(c)

    main_window.mainloop()


def create_main_window():
    main_window = tk.Tk()
    main_window.title("nattsud - a sudoku helper")
    main_window.geometry('700x500')
    main_window.minsize(CANVAS_SIZE_X, CANVAS_SIZE_Y)
    return main_window


def set_start():
    for tk_cell in tk_cells:
        tk_cells[tk_cell].insert(1, 3)
        cells[tk_cell] = _get_val(tk_cell)
    given_cells = solver.set_givens(cells)
    info_text = "given cells:\n"
    cells_text = ""
    for cell in given_cells:
        info_text += (" " + str(cell) + ":" + _get_val(cell))
        cells_text += (str(cell) + ":" + _get_val(cell) + ", ")
        _disable(tk_cells[cell])
        # _set_possible(cell[0], cell[1], int(_get_val(cell)))
        _set_possible_definite(cell)
    if given_cells:
        start_button['state'] = tk.DISABLED
        cells_text = cells_text[0:-2]  # Remove last ", "
        _show_info_strings("given cells:", cells_text)


def calculate_possible_numbers():
    print("CALC!")


def reduce_possible_numbers():
    print("REDUCE!")


def draw_xy_labels_for_cells(c):
    grid_x = 0
    for x in list(string.ascii_lowercase[:9]):
        x_label = tk.Label(c, text=x, bg=COLOR)
        grid_x += 1
        c.create_window(CELL_SIZE*(grid_x+0.5), 0, window=x_label, anchor=tk.N)

    grid_y = 0
    for y in list(range(1, 10)):
        y_label = tk.Label(c, text=y, bg=COLOR)
        grid_y += 1
        c.create_window(CELL_SIZE/2, CELL_SIZE*(grid_y+0.5), window=y_label, anchor=tk.E)


def draw_xy_labels_for_possibles(c):
    grid_x = X_STARTING_POINT_OF_POSSIBLES - POSSIBLES_SIZE/2
    for x in list(string.ascii_lowercase[:9]):
        x_label = tk.Label(c, text=x, bg=COLOR)
        grid_x += POSSIBLES_SIZE
        c.create_window(grid_x, 0, window=x_label, anchor=tk.N)

    grid_x = X_STARTING_POINT_OF_POSSIBLES - POSSIBLES_SIZE/2
    grid_y = POSSIBLES_SIZE/2
    for y in list(range(1, 10)):
        y_label = tk.Label(c, text=y, bg=COLOR)
        grid_y += POSSIBLES_SIZE
        c.create_window(grid_x, grid_y, window=y_label, anchor=tk.E)


def draw_lines_for_cells(c):
    grid_end = CELL_SIZE * 10
    for line_nr in list(range(0, 4)):
        region_end_x = CELL_SIZE + CELL_SIZE*line_nr*3
        region_end_y = CELL_SIZE + CELL_SIZE*line_nr*3
        c.create_line(CELL_SIZE, region_end_y, grid_end, region_end_y)  # horizontal
        c.create_line(region_end_x, CELL_SIZE, region_end_x, grid_end)  # vertical
    for line_nr in list(range(0, 3)):
        for region_line_nr in list(range(1, 3)):
            cell_end_x = CELL_SIZE + CELL_SIZE*line_nr*3 + CELL_SIZE*region_line_nr
            cell_end_y = CELL_SIZE + CELL_SIZE*line_nr*3 + CELL_SIZE*region_line_nr
            c.create_line(CELL_SIZE, cell_end_y, grid_end, cell_end_y, dash=(3,3))  # horizontal
            c.create_line(cell_end_x, CELL_SIZE, cell_end_x, grid_end, dash=(3,3))  # vertical


def draw_lines_for_possibles(c):
    grid_start_x = X_STARTING_POINT_OF_POSSIBLES
    grid_start_y = 0
    grid_end_x = grid_start_x + POSSIBLES_SIZE * 9
    grid_end_y = POSSIBLES_SIZE + POSSIBLES_SIZE * 9
    for line_nr in list(range(0, 4)):
        region_end_x = X_STARTING_POINT_OF_POSSIBLES + POSSIBLES_SIZE*line_nr*3
        region_end_y = POSSIBLES_SIZE + POSSIBLES_SIZE*line_nr*3
        c.create_line(grid_start_x, region_end_y, grid_end_x, region_end_y)  # horizontal
        c.create_line(region_end_x, POSSIBLES_SIZE, region_end_x, grid_end_y)  # vertical
    for line_nr in list(range(0, 3)):
        for region_line_nr in list(range(1, 3)):
            cell_end_x = grid_start_x + POSSIBLES_SIZE*line_nr*3 + POSSIBLES_SIZE*region_line_nr
            cell_end_y = POSSIBLES_SIZE + POSSIBLES_SIZE*line_nr*3 + POSSIBLES_SIZE*region_line_nr
            c.create_line(grid_start_x, cell_end_y, grid_end_x, cell_end_y, dash=(3,3))  # horizontal
            c.create_line(cell_end_x, POSSIBLES_SIZE, cell_end_x, grid_end_y, dash=(3,3))  # vertical


def put_input_fields(c):
    adjust_to_lines_x = 2
    adjust_to_lines_y = 4
    for x in list(string.ascii_lowercase[:9]):
        for y in list(range(1, 10)):
            tk_cells[x, y] = create_tk_spinbox(c)
            c.create_window(_idx(x)*CELL_SIZE + adjust_to_lines_x,
                            y*CELL_SIZE + adjust_to_lines_y,
                            window=tk_cells[x, y],
                            anchor=tk.NW)


def put_possible_numbers_fields(c):
    x_offset = X_STARTING_POINT_OF_POSSIBLES - POSSIBLES_SIZE
    adjust_to_lines_x = 2
    for x in list(string.ascii_lowercase[:9]):
        for y in list(range(1, 10)):
            i = 0
            for yy in [0, 1, 2]:
                for xx in [0, 1, 2]:
                    i += 1
                    possibles[x, y, i] = tk.Label(c, height=1, width=1, font=Font(size=POSSIBLES_SIZE//6), bg=COLOR)
                    _set_possible(x, y, i, i)
                    c.create_window(_idx(x)*POSSIBLES_SIZE + x_offset + (xx*POSSIBLES_SIZE/3) + adjust_to_lines_x,
                                    y*POSSIBLES_SIZE + (yy*(POSSIBLES_SIZE*0.85)/3) + 1,
                                    window=possibles[x, y, i],
                                    anchor=tk.NW)


def create_tk_spinbox(c):
    return tk.Spinbox(c,
                      width=1,
                      font=Font(size=(CELL_SIZE//2 - 2)),
                      values=("", 1, 2, 3, 4, 5, 6, 7, 8, 9),
                      wrap=True,
                      state='readonly',
                      readonlybackground=COLOR,
                      disabledbackground="light grey")


def put_info_field(c):
    label = tk.Label(c, height=10, width=INFO_FIELD_CHAR_SIZE)
    label['text'] = "Welcome to nattsud!"
    c.create_window(0.5*CELL_SIZE, 13*CELL_SIZE, window=label, anchor=tk.NW)
    return label


def _set_possible(x, y, i, val):
    possibles[x, y, i]['text'] = val


def _set_possible_definite(cell):
    x = cell[0]
    y = cell[1]
    val = int(_get_val(cell))
    for i in range(1, 10):
        _set_possible(x, y, i, "")
    _set_possible(x, y, val, val)


def _show_info_strings(*texts):
    aggregated_info = ""
    for text in texts:
        size = INFO_FIELD_CHAR_SIZE
        nr_of_substrings = len(text)//size + 1
        for i in range(nr_of_substrings):
            aggregated_info += (text[i*size:(i+1)*size] + "\n")

    aggregated_info = aggregated_info[0:-1]  # Strip last "\n"
    info_field[0]['text'] = aggregated_info


def _disable(o):
    o['state'] = tk.DISABLED


def _idx(y):
    return ord(y) - 96


def _get_val(cell):
    return tk_cells[cell].get()


if __name__ == '__main__':
    main()







# def _draw_xy_labels_on_window(main_window):
#     grid_x = 0
#     grid_y = 0
#     for x in list(string.ascii_lowercase[:9]):
#         x_label = tk.Label(main_window, text=x)
#         grid_x += 1
#         x_label.grid(column=grid_x, row=0)
#         y_label_created = False
#         for y in list(range(1, 10)):
#             if not y_label_created:
#                 y_label = tk.Label(main_window, text=_idx(x))
#                 grid_y += 1
#                 y_label.grid(column=0, row=grid_y)
#                 y_label_created = True
#             input_cell = tk.Entry(main_window, width=2)
#             input_cell.grid(column=_idx(x), row=y)


