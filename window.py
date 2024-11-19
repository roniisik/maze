from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()


    def close(self):
        self.running = False

    
    def draw(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    
    def draw(self, canvas, fill_color):
        p1 = self.p1
        p2 = self.p2
        canvas.create_line(
            p1.x, p1.y, p2.x, p2.y, fill=fill_color, width=2
            )
        