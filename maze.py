from cell import *
import time
import random


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        
        self.seed = seed
        if seed is not None:
            seed = random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False



    def _break_walls_r(self, i, j):
        cur_cell = self._cells[i][j]
        cur_cell.visited = True

        while True:
            to_visit = []
            left = cur_cell
            right = cur_cell
            top = cur_cell
            bottom = cur_cell
            if 0 < i:
                left = self._cells[i-1][j]
            if i < len(self._cells) - 1:
                right = self._cells[i+1][j]
            if 0 < j:
                top = self._cells[i][j-1]
            if j < len(self._cells[0]) - 1:
                bottom = self._cells[i][j+1]

            
            if not left.visited:
                to_visit.append(left)
            if not right.visited:
                to_visit.append(right)
            if not top.visited:
                to_visit.append(top)
            if not bottom.visited:
                to_visit.append(bottom)
            
            if not to_visit:
                self._draw_cell(cur_cell)
                return
            
            direction = random.choice(to_visit)

            if direction == left:
                left.has_right_wall = False
                cur_cell.has_left_wall = False
                self._break_walls_r(i-1, j)
            elif direction == right:
                right.has_left_wall = False
                cur_cell.has_right_wall = False
                self._break_walls_r(i+1, j)
            elif direction == top:
                top.has_bottom_wall = False
                cur_cell.has_top_wall = False
                self._break_walls_r(i, j-1)
            elif direction == bottom:
                bottom.has_top_wall = False
                cur_cell.has_bottom_wall = False
                self._break_walls_r(i, j+1)
            

    def _break_entrance_and_exit(self):
        cell1 = self._cells[0][0]
        cell2 = self._cells[-1][-1]
        
        cell1.has_top_wall = False
        cell2.has_bottom_wall = False
        
        self._draw_cell(cell1)
        self._draw_cell(cell2)

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
                self._draw_cell(cell)

    def _draw_cell(self, cell):
        cell.draw(cell._x1, cell._y1, cell._x2, cell._y2)
        self._animate()
    

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.02)