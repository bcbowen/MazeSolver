from window import Window
from line import Line
from point import Point
from cell import Cell
from cell_border import CellBorder
from maze import Maze

def main(): 
    row_count = 12
    col_count = 16
    margin = 50 
    screen_x = 800 
    screen_y = 600 
    cell_size_x = (screen_x - 2 * margin) / col_count
    cell_size_y = (screen_y - 2 * margin) / row_count
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, row_count, col_count, cell_size_x, cell_size_y, win)
    win.wait_for_close()


main()