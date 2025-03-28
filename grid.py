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
