import pygame
from colours import colours


class Grid:
    def __init__ (self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]
        self.colours = colours.cell_colours()


    def print_grid (self):
        for row in range(self.num_rows):
            for column in range (self.num_cols):
                print(self.grid[row][column], end = "")
            print()


    def is_inside (self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False
    
    def is_empty (self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full (self, row):
        for column in range (self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_full_rows (self):
        rows_cleared = 0
        for row in range (self.num_rows):
            if self.is_row_full(row):
                rows_cleared += 1
                for r in range (row, 0, -1):
                    for column in range (self.num_cols):
                        self.grid[r][column] = self.grid[r-1][column]
                for column in range (self.num_cols):
                    self.grid[0][column] = 0
        return rows_cleared     
    
    def move_row_down (self, row):  
        for r in range (row, 0, -1):
            for column in range (self.num_cols):
                self.grid[r][column] = self.grid[r-1][column]
        for column in range (self.num_cols):
            self.grid[0][column] = 0    

    def clear_row (self, row):
        for column in range (self.num_cols):
            self.grid[row][column] = 0
        self.move_row_down(row)

    def reset (self):
        for row in range (self.num_rows):
            for column in range (self.num_cols):
                self.grid[row][column] = 0
    
    
    def draw (self, screen): 
        for row in range (self.num_rows):
            for column in range (self.num_cols):
                cell_value = self.grid[row][column]

                # cell_rectangle = pygame.Rect (x,y,w,h)
                cell_rectangle = pygame.Rect (column * self.cell_size, row * self.cell_size,
                                              self.cell_size, self.cell_size)
                
                pygame.draw.rect (screen, self.colours[cell_value], cell_rectangle)

                
                cell_rectangle = pygame.Rect (column * self.cell_size +1 , row * self.cell_size +1 ,
                                              self.cell_size - 1, self.cell_size - 1)
                
                pygame.draw.rect (screen, self.colours[cell_value], cell_rectangle)

                pygame.draw.rect(screen, (30, 30, 30), cell_rectangle, 1)
