from window import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)
    """ line1 = Line(Point(0, 0), Point(800, 600))
    #win.draw(line1, "red")
    cell1 = Cell(Point(200, 200), Point(300, 300), win)
    cell2 = Cell(Point(400, 400), Point(500, 500), win)
    cell1.has_bottom_wall = False
    cell1.draw(cell1._x1, cell1._y1, cell1._x2, cell1._y2)
    cell2.draw(cell2._x1, cell2._y1, cell2._x2, cell2._y2)
    cell2.draw_move(cell1) """
    maze = Maze(20, 20, 10, 10, 50, 50, win, 3)
    print(maze.solve())
    

    win.wait_for_close()















if __name__ == "__main__":
    main()