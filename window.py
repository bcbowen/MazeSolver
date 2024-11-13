from tkinter import Tk, BOTH, Canvas
from line import Line

class Window: 
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.__rootWidget = Tk()
        self.__running = False
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)


    def redraw(self): 
        self.__rootWidget.update_idletasks()
        self.__rootWidget.update()

    def wait_for_close(self): 
        self.__running = True
        while self.__running: 
            self.redraw()
        print("window closed...")

    def close(self): 
        self.__running = False

    def draw_line(self, line: Line, fill_color: str): 
        line.draw(self.__canvas, fill_color=fill_color)