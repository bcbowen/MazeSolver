from cell import Cell

class Maze: 
    def __init__(
        self, 
        x1, 
        y1, 
        num_rows, 
        cell_size_x, 
        cell_size_y, 
        win
    ): 
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self): 
        for row in range(0, self.num_rows): 
            for col in range(0, self.num_rows): 
                


    def _draw_cell(self, i, j): 
        pass

    def _animate(self): 
        pass