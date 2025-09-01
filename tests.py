import unittest
from cell import Cell
from maze import Maze
from cell_border import CellBorder

class Tests(unittest.TestCase): 
    def _helper_test_maze_create_cells(self, row_count, col_count): 
        m1 = Maze(0, 0, row_count, col_count, 10, 10)
        self.assertEqual(len(m1._cells), col_count)
        self.assertEqual(len(m1._cells[0]), row_count)
        print(f"{row_count} rows; {col_count} cols")

    def test_maze_create_cell_cases(self): 
        test_cases = [
            (10, 12), 
            (15, 20), 
            (5, 5)
        ]

        for rows, cols in test_cases: 
            with self.subTest(row_count=rows, col_count=cols): 
                self._helper_test_maze_create_cells(rows,cols)

    def test_break_entrance_and_exit(self): 
        row_count = 10
        col_count = 12
        m1 = Maze(0, 0, row_count, col_count, 10, 10)
        i, j = 0, 0
        cell : Cell = m1._cells[i][j]
        self.assertEqual((cell.border_type & CellBorder.HasLeftWall), 0)

        i, j = m1._row_count - 1, m1._col_count - 1
        cell = m1._cells[i][j]
        self.assertEqual((cell.border_type * CellBorder.HasRightWall), 0)


if __name__ == "__main__":
    unittest.main()