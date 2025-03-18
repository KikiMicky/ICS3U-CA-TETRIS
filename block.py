from colours import colours
from position import Position
import pygame


class block:
    def __init__ (self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rot_state = 0
        self.colours = colours.cell_colours()


    def move (self, row, column):
        self.row_offset += row
        self.column_offset += column


    def cell_positions (self):
        tiles = self.cells[self.rot_state]
        moved_tiles = []

        for position in tiles:
            position = Position (position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles


    def draw (self, screen):
        tiles = self.cell_positions()

        for tile in tiles:
            tile_rectangle = pygame.Rect (tile.column * self.cell_size +1, tile.row * self.cell_size +1,
                                          self.cell_size -1, self.cell_size -1)
            

            pygame.draw.rect (screen, self.colours[self.id], tile_rectangle)