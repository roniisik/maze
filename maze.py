from cell import *
import time


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    
    def _create_cells(self):
        x1 = self.x1
        for i in range(self.num_cols):
            x2 = x1 + self.cell_size_x
            y1 = self.y1
            col_cells = []
            for j in range(self.num_rows):
                y2 = y1 + self.cell_size_y
                col_cells.append(Cell(Point(x1, y1), Point(x2, y2), self._win))
                y1 += self.cell_size_y
            self._cells.append(col_cells)    
            x1 += self.cell_size_x

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                cell = self._cells[i][j]
                cell.draw(cell._x1, cell._y1, cell._x2, cell._y2)
                self._animate()
    

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)