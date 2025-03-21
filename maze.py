import time
from cell import Cell
from point import Point

class Maze: 
    def __init__(
        self, 
        x1, 
        y1, 
        row_count, 
        col_count,
        cell_size_x, 
        cell_size_y, 
        win
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

    def _create_cells(self): 
        for _ in range(0, self._row_count): 
            cell_row = []
            for _ in range(0, self._col_count): 
                cell_row.append(Cell(self._win))
            self._cells.append(cell_row)
        
        for i in range(self._col_count): 
            for j in range(self._row_count): 
                self._draw_cell(i, j)

    def _draw_cell(self, i, j): 
        cell = Cell(self._win)
        ul = Point(self._x1 + i * self._cell_size_x, self._y1 + j * self._cell_size_y)
        lr = Point(ul.x + self._cell_size_x, ul.y + self._cell_size_y)
        cell.draw(ul, lr)
        self._animate()

    def _animate(self): 
        self._win.redraw()
        time.sleep(.05)