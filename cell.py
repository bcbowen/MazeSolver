from line import Line
from point import Point
from window import Window
from cell_border import CellBorder

class Cell: 
    def __init__(self, win: Window): 
        self.border_type = CellBorder.Default
        self._x1 = None 
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, top_left: Point, bottom_right: Point): 
        self._x1 = top_left.x
        self._x2 = bottom_right.x
        self._y1 = top_left.y
        self._y2 = bottom_right.y
        
        if ((self.border_type & CellBorder.HasLeftWall) == CellBorder.HasLeftWall): 
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")
        
        if ((self.border_type & CellBorder.HasRightWall) == CellBorder.HasRightWall):
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if ((self.border_type & CellBorder.HasTopWall) == CellBorder.HasTopWall): 
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if ((self.border_type & CellBorder.HasBottomWall) == CellBorder.HasBottomWall):
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")
        
    def draw_move(self, to_cell: 'Cell', undo: bool = False): 
        x = (self._x2 - self._x1) / 2
        y = (self._y2 - self._y1) / 2
        p1 = Point(x, y) 
        x = (to_cell._x2 - to_cell._x1) / 2
        y = (to_cell._y2 - to_cell._y1) / 2
        p2 = Point(x, y)
        color = "black" if undo else "red" 
        self._win.draw_line(Line(p1, p2), color)
