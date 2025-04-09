import pygame
from colours import colours
from block import block
from shapes import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock
import random


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

    
    def print_grid(self):
        for row in range(self.num_rows):  # Loop through each row
            for column in range(self.num_cols):  # Loop through each column in the row
                print(self.grid[row][column], end="")  # Print the grid value (0 or 1) in each cell
            print()  # Print a newline after each row

    def is_inside(self, row, column):
        # Check if the given (row, column) is within the grid's boundaries
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True  # Return True if inside the grid
        return False  # Return False if outside the grid
    
    def is_empty(self, row, column):
        # Check if the cell at (row, column) is empty (contains 0)
        if self.grid[row][column] == 0:
            return True  # Return True if the cell is empty
        return False  # Return False if the cell is not empty
    
    def is_row_full(self, row):
        # Check if the entire row is full (contains no zeros)
        for column in range(self.num_cols):  # Loop through each column in the row
            if self.grid[row][column] == 0:  # If there is an empty cell (0)
                return False  # Return False, row is not full
        return True  # Return True, row is full if no zeros are found
    
    def clear_full_rows(self):
        rows_cleared = 0  # Variable to count the number of cleared rows
        for row in range(self.num_rows):  # Loop through each row
            if self.is_row_full(row):  # Check if the row is full
                rows_cleared += 1  # Increment the cleared rows counter

                for r in range(row, 0, -1):  # Shift rows down to fill the cleared row
                    for column in range(self.num_cols):  # Loop through each column in the row
                        # move the row down
                        self.grid[r][column] = self.grid[r - 1][column] 

                    '''
                        This part of the code ensures that after shifting rows down to fill a cleared row,
                        the new top row (which was previously row 1) is reset to be empty.
                        This is important (i think so) for maintaining the grid structure and ensuring that
                        new blocks do not inadvertently be placed in the wrong position
                    '''

                for column in range(self.num_cols):  # Set the top row to empty after shifting
                    self.grid[0][column] = 0
        return rows_cleared  # Return the number of rows cleared

    def move_row_down(self, row):
        # Move the given row and all rows above it one position down
        for r in range(row, 0, -1):  # Loop from the specified row to the top
            for column in range(self.num_cols):  # Loop through each column
                self.grid[r][column] = self.grid[r - 1][column]  # Move the row down
        for column in range(self.num_cols):  # Set the topmost row to empty
            self.grid[0][column] = 0

    def clear_row(self, row):
        # Clear the specified row (set all cells in the row to 0)
        for column in range(self.num_cols):  # Loop through each column in the row
            self.grid[row][column] = 0  # Set the cell to empty
        self.move_row_down(row)  # Move rows down to fill the cleared row

    def reset(self):
        # Reset the entire grid to be empty (set all cells to 0)
        for row in range(self.num_rows):  # Loop through each row
            for column in range(self.num_cols):  # Loop through each column
                self.grid[row][column] = 0  # Set the cell to empty
    
    def draw(self, screen):
        # Draw the grid on the pygame screen
        for row in range(self.num_rows):  # Loop through each row
            for column in range(self.num_cols):  # Loop through each column
                cell_value = self.grid[row][column]  # Get the value of the cell (0 or 1)

                # Create a rectangle to represent the cell on the screen
                cell_rectangle = pygame.Rect(column * self.cell_size, row * self.cell_size,
                                              self.cell_size, self.cell_size)
                
                pygame.draw.rect(screen, self.colours[cell_value], cell_rectangle)  # Draw the cell with the corresponding color

                # Draw a smaller rectangle inside the cell to create a border effect
                cell_rectangle = pygame.Rect(column * self.cell_size + 1, row * self.cell_size + 1,
                                              self.cell_size - 1, self.cell_size - 1)
                
                pygame.draw.rect(screen, self.colours[cell_value], cell_rectangle)  # Draw the smaller rectangle inside the cell

                # Draw a border around the cell
                pygame.draw.rect(screen, (30, 30, 30), cell_rectangle, 1)  # Draw the border with a dark color