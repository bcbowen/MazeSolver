from window import Window
from line import Line
from point import Point


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

    win.wait_for_close()


main()