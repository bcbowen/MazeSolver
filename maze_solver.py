from window import Window
from line import Line
from point import Point
from cell import Cell

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

    cell = Cell(win, True, True, True, True, Point(0, 0), Point(100, 100))
    cell.draw(); 

    cell = Cell(win, True, True, True, True, Point(100, 0), Point(200, 100))
    cell.draw(); 

    cell = Cell(win, True, True, True, True, Point(300, 0), Point(300, 100))
    cell.draw(); 

    cell = Cell(win, False, True, True, True, Point(200, 300), Point(300, 300))
    cell.draw(); 

    cell = Cell(win, True, False, True, True, Point(400, 300), Point(500, 300))
    cell.draw(); 

    cell = Cell(win, False, True, False, True, Point(200, 600), Point(300, 600))
    cell.draw(); 

    cell = Cell(win, True, False, True, False, Point(400, 600), Point(500, 600))
    cell.draw(); 


    win.wait_for_close()


main()