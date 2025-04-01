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
        if not self.block_inside_grid():
            self.current_block.move(-1, 0)  

    def block_inside_grid(self):
        tiles = self.current_block.cell_positions()
        for tile in tiles:
            print(tile)
            if not self.grid.is_inside(tile.row, tile.column):  
               return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen)  
