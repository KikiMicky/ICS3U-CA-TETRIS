from grid import Grid
from shapes import *

import random
import pygame



class game: 

    def __init__(self):
        self.grid = Grid()  # Initializes the grid object
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]  # Creates a list of all block types
        self.current_block = self.get_random_block()  # Gets a random block to be the current block
        self.next_block = self.get_random_block()  # Gets a random block to be the next block
    
    def get_random_block(self): 
        if len(self.blocks) == 0:  # If no blocks are left, reinitialize the list of blocks
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)  # Randomly choose a block
        self.blocks.remove(block)  # Remove that block from the list
        return block  # Return the selected block
    
    def move_left(self):
        self.current_block.move(0, -1)  # Move the block one step to the left
        if self.block_inside_grid() == False or self.block_fits() == False:  # Check if it goes out of bounds or doesn't fit
            self.current_block.move(0, 1)  # Undo the move (move back to the right)

    def move_right(self):
        self.current_block.move(0, 1)  # Move the block one step to the right
        if self.block_inside_grid() == False or self.block_fits() == False:  # Check if it goes out of bounds or doesn't fit
            self.current_block.move(0, -1)  # Undo the move (move back to the left)

    def move_down(self):
        self.current_block.move(1, 0)  # Move the block one step down
        if self.block_inside_grid() == False or self.block_fits() == False:  # If block cannot move down (due to collision or out of bounds)
            self.current_block.move(-1, 0)  # Undo the move (move the block back up)
            self.lock_block()  # Lock the block in place (so it becomes part of the grid)

    def lock_block(self):
        tiles = self.current_block.cell_positions()  # Get the positions of the block's cells
        for pos in tiles:  # Loop through each tile of the block
            self.grid.grid[pos.row][pos.column] = self.current_block.id  # Lock the block's cell on the grid
        self.current_block = self.next_block  # Set the next block as the current block
        self.next_block = self.get_random_block()  # Get a new random block for the next turn
        rows_cleared = self.clear_rows()  # Clear any full rows
        if self.block_inside_grid() == False:  # If the block doesn't fit (game over condition)
            print("Game Over!")
            self.game_over = False  # End the game
    
    def block_inside_grid(self):
        tiles = self.current_block.cell_positions()  # Get the positions of the block's cells
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):  # Check if the block's cell is inside the grid
                return False  # If any part is outside, return False
        return True  # If all parts are inside the grid, return True
    
    def move_up(self):
        self.current_block.move(-1, 0)  # Move the block one step up

    def block_fits (self):
        tiles = self.current_block.cell_positions()  # Get the positions of the block's cells
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:  # If the cell is not empty (blocked)
                return False  # Return False if the block doesn't fit
        return True  # If all cells are empty, return True (block fits)

    def clear_rows(self):
        self.grid.clear_full_rows()  # Clear full rows from the grid

    def spawn_new_block(self):
        self.current_block = self.next_block  # Set the next block as the current block
        self.next_block = self.get_random_block()  # Get a new random block for the next turn

    ''' why my blocks are overlapping
    '''
    
    def is_valid_position(self, block):
        for pos in block.get_cell_positions():  # Get the positions of the block's cells
            if not (0 <= pos.x < self.columns and 0 <= pos.y < self.rows):  # Check if the block's cell is within grid bounds
                return False  # If out of bounds, return False
            if self.grid[pos.y][pos.x] != (0, 0, 0):  # Check if the cell is already filled
                return False  # If filled, return False
        return True  # If all positions are valid, return True
    
    def rotate(self):
        self.current_block.rotate()  # Rotate the current block
        if self.block_inside_grid() == False:  # If after rotation the block is not inside the grid
            self.current_block.undo_rotate()  # Undo the rotation to revert back to the previous state

    def draw(self, screen):
        self.grid.draw(screen)  # Draw the grid on the screen
        self.current_block.draw(screen, 1, 1)  # Draw the current block on the screen
        self.next_block.draw(screen, 270, 270)  # Draw the next block on the screen
