import time
from cell import Cell
from point import Point
from cell_border import CellBorder

class Maze: 
    def __init__(
        self, 
        x1, 
        y1, 
        row_count, 
        col_count,
        cell_size_x, 
        cell_size_y, 
        win = None
    ): 
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._row_count = row_count
        self._col_count = col_count
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self): 
        for _ in range(0, self._col_count): 
            col_cells = []
            for _ in range(0, self._row_count): 
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        
        for i in range(self._col_count): 
            for j in range(self._row_count): 
                self._draw_cell(i, j)

    def _draw_cell(self, i, j): 
        if self._win is None: 
            return
        cell = Cell(self._win)
        ul = Point(self._x1 + i * self._cell_size_x, self._y1 + j * self._cell_size_y)
        lr = Point(ul.x + self._cell_size_x, ul.y + self._cell_size_y)
        cell.draw(ul, lr)
        self._animate()

    def _animate(self): 
        if self._win is None: 
            return
        self._win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self): 
        cell : Cell = self._cells[0][0]
        cell.border_type -= CellBorder.HasLeftWall
        i, j = 0, 0
        self._draw_cell(i, j)
        i, j = self._row_count, self._col_count
        cell = self._cells[i][j]
        cell.border_type -= CellBorder.HasRightWall
        self._draw_cell(i, j)