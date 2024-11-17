from line import Line
from point import Point
from window import Window

class Cell: 
    def __init__(self, win:Window, has_left: bool, has_right : bool, has_top: bool, has_bottom: bool, top_left: Point, bottom_right: Point): 
        self.has_left_wall = has_left
        self.has_right_wall = has_right
        self.has_top_wall = has_top
        self.has_bottom_wall = has_bottom
        self._x1 = top_left.x 
        self._x2 = bottom_right.x
        self._y1 = top_left.y
        self._y2 = bottom_right.y
        self._win = win

    def draw(self): 
        if (self.has_left_wall): 
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")
        
        if (self.has_right_wall): 
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if (self.has_top_wall): 
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")

        if (self.has_bottom_wall): 
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2, self._y2)
            line = Line(p1, p2)
            self._win.draw_line(line, "black")
        
        
        
