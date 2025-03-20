import pygame
import random
try:
    from colours import colours
    from position import Position
    from blocks import Block  # Assuming different block shapes are defined in blocks.py
except ImportError:
    import sys
    sys.path.append('c:/Users/ASUS/Desktop/path_to_your_modules')
    from colours import colours
    from position import Position
    from blocks import Block

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
CELL_SIZE = 30
GRID_ROWS = SCREEN_HEIGHT // CELL_SIZE
GRID_COLUMNS = SCREEN_WIDTH // CELL_SIZE
BACKGROUND_COLOR = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Create blocks list (assuming Block subclasses for each shape)
block_types = [Block(0), Block(1), Block(2), Block(3), Block(4), Block(5), Block(6)]
current_block = random.choice(block_types)
next_block = random.choice(block_types)

# Game loop variables
clock = pygame.time.Clock()
running = True

def spawn_new_block():
    """Replace current block with the next one and generate a new 'next' block."""
    global current_block, next_block
    current_block = next_block
    next_block = random.choice(block_types)  # Pick a new random block

while running:
    screen.fill(BACKGROUND_COLOR)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_block.move(0, -1)
            elif event.key == pygame.K_RIGHT:
                current_block.move(0, 1)
            elif event.key == pygame.K_DOWN:
                current_block.move(1, 0)
            elif event.key == pygame.K_UP:
                current_block.rotate()

    # Move block down automatically
    current_block.move(1, 0)

    # TODO: Collision detection to check if block landed
    # If block reaches the bottom, spawn a new one
    if current_block.row_offset >= GRID_ROWS - 1:  # Simple collision check
        spawn_new_block()

    # Draw current block
    current_block.draw(screen)

    pygame.display.flip()
    clock.tick(5)  # Control speed of falling blocks

pygame.quit()
