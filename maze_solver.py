from window import Window
from line import Line
from point import Point
from cell import Cell
from cell_border import CellBorder

def main(): 
    win = Window(800, 600)

    p1 = Point(20, 20)
    p2 = Point(20, 80)
    
    line = Line(p1, p2)
    win.draw_line(line, "black")

    p3 = Point(80, 20)
    p4 = Point(80, 80)
    
    line2 = Line(p3, p4)
    win.draw_line(line2, "red")

    cell = Cell(win)
    cell.draw(Point(0, 0), Point(100, 100)); 

    cell = Cell(win)
    cell.draw(Point(100, 0), Point(200, 100)); 

    cell = Cell(win)
    cell.draw(Point(300, 0), Point(300, 100)); 

    cell = Cell(win)
    cell.border_type -= CellBorder.HasLeftWall
    cell.draw(Point(200, 300), Point(300, 400)); 

    cell = Cell(win)
    cell.border_type -= CellBorder.HasRightWall
    cell.draw(Point(400, 300), Point(500, 400)); 

    cell = Cell(win)
    cell.border_type -= CellBorder.HasTopWall
    cell.draw(Point(200, 600), Point(300, 700)); 

    cell = Cell(win)
    cell.border_type -= CellBorder.HasBottomWall
    cell.draw(Point(400, 600), Point(500, 700)); 


    win.wait_for_close()


main()