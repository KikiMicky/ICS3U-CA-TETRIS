from grid import Grid
from shapes import *

import random
import pygame


class game: 

    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()  
        self.next_block = self.get_random_block()
    
    def get_random_block(self): 
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def move_left(self):
        self.current_block.move(0, -1)
        if not self.block_inside_grid():
            self.current_block.move(0, 1)  

    def move_right(self):
        self.current_block.move(0, 1)
        if not self.block_inside_grid():
            self.current_block.move(0, -1)  

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside_grid() == False:
            self.current_block.move(-1, 0)
            self.lock_block()  

    def lock_block(self):
        tiles = self.current_block.cell_positions()
        for pos in tiles:
            self.grid.grid[pos.row][pos.column] = self.current_block.id  # Lock the block in place
        self.current_block = self.next_block  # Move to the next block
        self.next_block = self.get_random_block()  # Get a new block
        
    
    def block_inside_grid(self):
        tiles = self.current_block.cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):  
                return False
        for tile in tiles:
            print(tile)
            if not self.grid.is_inside(tile.row, tile.column):  
               return False
        return True
    
    def move_up(self):
        self.current_block.move(-1, 0)



    def clear_rows(self):
            self.grid.clear_full_rows()  # or clear_lines() depending on what you renamed

    def spawn_new_block(self):
        self.current_block = self.next_block
        self.next_block = self.get_random_block()

    def is_valid_position(self, block):
        for pos in block.get_cell_positions():
            if not (0 <= pos.x < self.columns and 0 <= pos.y < self.rows):
                return False
            if self.grid[pos.y][pos.x] != (0, 0, 0):  # If cell is already filled
                return False
        return True
    
    def rotate (self):
        self.current_block.rotate()
        if self.block_inside_grid() == False:
            self.current_block.undo_rotate()

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 1, 1)  
        self.next_block.draw(screen, 270, 270)