from colours import colours
from position import Position
import pygame

class block:
    def __init__ (self, id):
        self.id = id  # Set a unique identifier for the block (like 'I', 'J', 'L', etc.)
        self.cells = {}  # Dictionary to store the block's rotation states
        self.cell_size = 30  # The size of each block cell in pixels
        self.row_offset = 0  # Offset for row position, to handle movement
        self.column_offset = 0  # Offset for column position, to handle movement
        self.rot_state = 0  # Initial rotation state of the block (starts at 0)
        self.colours = colours.cell_colours()  # Get block colors from the 'colours' module

    def move(self, row, column):
        self.row_offset += row  # Adjust the block's row position by the given row value
        self.column_offset += column  # Adjust the block's column position by the given column value

    def rotate(self):
        self.rot_state += 1  # Increase the rotation state (rotate the block)
        if self.rot_state == len(self.cells):
            self.rot_state = 0  # If we exceed the number of rotation states, loop back to the first state

    def undo_rotate(self):
        self.rot_state -= 1  # Decrease the rotation state (undo rotation)
        if self.rot_state == 0:
            self.rot_state = len(self.cells) - 1  # Loop back to the last rotation state

    def cell_positions(self):
        tiles = self.cells[self.rot_state]  # Get the positions of the cells for the current rotation state
        moved_tiles = []  # Create an empty list to store adjusted cell positions

        for position in tiles:
            # Adjust the position of each cell by adding row and column offsets
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)  # Add the adjusted position to the list
        return moved_tiles  # Return the list of moved cell positions

    def draw(self, screen, offset_x, offset_y):
        tiles = self.cell_positions()  # Get the current tile positions based on the block's rotation and offset

        for tile in tiles:
            # Create a rectangle for each tile to be drawn on the screen at the correct position
            tile_rectangle = pygame.Rect(offset_x + tile.column * self.cell_size,
                                          offset_y + tile.row * self.cell_size,
                                          self.cell_size - 1, self.cell_size - 1)  # Offset by the given amount and size of tile

            pygame.draw.rect(screen, self.colours[self.id], tile_rectangle)  # Draw the block with its color on the screen
