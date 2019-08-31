#!/c/Users/David/AppData/Local/Programs/Python/Python37-32/python
import string
import tkinter as tk

CELL_SIZE = 30
COLOR="white"


def main():
    main_window = tk.Tk()
    main_window.title("nattsud - a sudoku helper")
    main_window.geometry('300x300')
    main_window.minsize(CELL_SIZE*14, CELL_SIZE*14)

    c = tk.Canvas(main_window, bg=COLOR, height=250, width=100)

    c.place(width=CELL_SIZE*14, height=CELL_SIZE*14)

    start_button = tk.Button(c, text="Set cells\n(1st: givens)", command=set_start)
    calc_button = tk.Button(c, text="Calculate all possible\nvalues (simple)", command=calculate)
    reduce_button = tk.Button(c, text="Reduce all possible\nvalues", command=reduce)
    c.create_window(CELL_SIZE*0.5, CELL_SIZE*11, window=start_button, anchor=tk.NW)
    c.create_window(CELL_SIZE*3, CELL_SIZE*11, window=calc_button, anchor=tk.NW)
    c.create_window(CELL_SIZE*7.1, CELL_SIZE*11, window=reduce_button, anchor=tk.NW)

    _draw_xy_labels_on_canvas(c)

    _draw_lines_on_canvas(c)

    print(main_window.size(), main_window.geometry())

    main_window.mainloop()


def set_start():
    print("START!")


def calculate():
    print("CALC!")


def reduce():
    print("REDUCE!")


def _draw_xy_labels_on_canvas(c):
    grid_x = 0
    grid_y = 0
    for x in list(string.ascii_lowercase[:9]):
        x_label = tk.Label(c, text=x, bg=COLOR)
        grid_x += 1
        c.create_window(CELL_SIZE * grid_x, 0, window=x_label, anchor=tk.NW)
    for y in list(range(1, 10)):
        y_label = tk.Label(c, text=y, bg=COLOR)
        grid_y += 1
        c.create_window(0, CELL_SIZE * grid_y, window=y_label, anchor=tk.NW)


def _draw_lines_on_canvas(c):
    grid_end = CELL_SIZE * 10
    for line_nr in list(range(0, 4)):
        region_end = CELL_SIZE + CELL_SIZE*line_nr*3
        c.create_line(0, region_end, grid_end, region_end)  # horizontal
        c.create_line(region_end, 0, region_end, grid_end)  # vertical
    for line_nr in list(range(0, 3)):
        for region_line_nr in list(range(1, 3)):
            cell_end = CELL_SIZE + CELL_SIZE*line_nr*3 + CELL_SIZE*region_line_nr
            print(cell_end/CELL_SIZE)
            c.create_line(CELL_SIZE, cell_end, grid_end, cell_end, dash=(3,3))  # horizontal
            c.create_line(cell_end, CELL_SIZE, cell_end, grid_end, dash=(3,3))  # vertical


def _idx(y):
    return ord(y) - 96


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


