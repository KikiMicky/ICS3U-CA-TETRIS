import pygame
import time

# Simple game loop with no dependencies

# Game state
game_running = False
last_time = 0
score = 0

# Game loop function
def game_loop():
    global last_time, score, game_running
    while game_running:
        # Calculate delta time (time since last frame)
        current_time = time.time() * 1000  # Convert to milliseconds
        if not last_time:
            last_time = current_time
        delta_time = current_time - last_time
        last_time = current_time

        # Update game state (once every 500ms)
        if delta_time > 500:
            # Update score
            score += 1
            print("Score:", score)

            # Example game logic: end game after score reaches 10
            if score >= 10:
                print("Game over!")
                game_running = False
                return  # Exit the loop

        time.sleep(0.016)  # Sleep to simulate frame rate (60 FPS)

# Start the game
def start_game():
    global game_running, score, last_time
    if not game_running:
        score = 0
        game_running = True
        last_time = 0
        print("Game started!")
        game_loop()

# Stop the game
def stop_game():
    global game_running
    game_running = False
    print("Game stopped!")

#import pygame
import random
from grid import Grid
from pygame.locals import *

# Initialize the pygame
pygame.init()

# Colors
dark_blue = (44, 44, 120)
colors = [
    (0, 0, 0),
    (120, 37, 179),  # Purple
    (100, 179, 179), # Cyan
    (80, 34, 22),    # Brown
    (80, 134, 22),   # Green
    (180, 34, 22),   # Red
    (180, 34, 122),  # Pink
    (180, 180, 22),  # Yellow
]

# Game dimensions
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

# Clock for controlling game speed
clock = pygame.time.Clock()

# Create grid
game_grid = Grid()

# Tetromino shapes
tetrominos = [
    [[1, 1, 1, 1]],                      # I
    [[1, 1, 1], [0, 1, 0]],              # T
    [[1, 1], [1, 1]],                    # O
    [[1, 1, 0], [0, 1, 1]],              # Z
    [[0, 1, 1], [1, 1, 0]],              # S
    [[1, 0, 0], [1, 1, 1]],              # J
    [[0, 0, 1], [1, 1, 1]]               # L
]

# Game variables
current_piece = None
current_piece_x = 0
current_piece_y = 0
current_piece_color = 0
score = 0
level = 1
lines_cleared = 0
game_over = False
fall_time = 0
fall_speed = 0.5  # seconds
next_piece = random.randint(0, len(tetrominos) - 1)

# Font for score display
font = pygame.font.SysFont('Arial', 20)

# Create a new piece
def new_piece():
    global current_piece, current_piece_x, current_piece_y, current_piece_color, next_piece
    current_piece = tetrominos[next_piece]
    current_piece_color = next_piece + 1
    next_piece = random.randint(0, len(tetrominos) - 1)
    
    # Position at top center
    current_piece_x = int(game_grid.columns / 2) - int(len(current_piece[0]) / 2)
    current_piece_y = 0
    
    # Check if game is over (collision on spawn)
    if check_collision(0, 0):
        return False
    return True

# Check for collision
def check_collision(offset_x, offset_y):
    for y in range(len(current_piece)):
        for x in range(len(current_piece[y])):
            if current_piece[y][x] == 0:
                continue
                
            new_x = current_piece_x + x + offset_x
            new_y = current_piece_y + y + offset_y
            
            # Check boundaries
            if new_x < 0 or new_x >= game_grid.columns or new_y >= game_grid.rows:
                return True
                
            # Skip if above the top
            if new_y < 0:
                continue
                
            # Check if already filled
            if game_grid.grid[new_y][new_x] != 0:
                return True
                
    return False

# Rotate the piece
def rotate_piece():
    global current_piece
    
    # Save the current piece
    original_piece = current_piece
    
    # Create a new rotated piece
    rotated = []
    for x in range(len(original_piece[0])):
        new_row = []
        for y in range(len(original_piece) - 1, -1, -1):
            new_row.append(original_piece[y][x])
        rotated.append(new_row)
    
    # Try the rotation
    current_piece = rotated
    if check_collision(0, 0):
        # Revert if there's a collision
        current_piece = original_piece
        return False
    return True

# Lock the piece in place
def lock_piece():
    for y in range(len(current_piece)):
        for x in range(len(current_piece[y])):
            if current_piece[y][x] == 0:
                continue
                
            # Skip if above the top
            if current_piece_y + y < 0:
                continue
                
            game_grid.grid[current_piece_y + y][current_piece_x + x] = current_piece_color

# Check for completed lines
def check_lines():
    global score, level, lines_cleared
    
    lines = 0
    for y in range(game_grid.rows - 1, -1, -1):
        if 0 not in game_grid.grid[y]:
            # Move all rows above down
            for y2 in range(y, 0, -1):
                game_grid.grid[y2] = game_grid.grid[y2 - 1].copy()
            
            # Clear the top row
            game_grid.grid[0] = [0] * game_grid.columns
            
            lines += 1
            y += 1  # Check the same row again
    
    if lines > 0:
        lines_cleared += lines
        score += lines * 100 * level
        level = lines_cleared // 10 + 1

# Draw the current piece
def draw_current_piece():
    for y in range(len(current_piece)):
        for x in range(len(current_piece[y])):
            if current_piece[y][x] == 0:
                continue
                
            # Draw only if visible on screen
            if current_piece_y + y >= 0:
                pygame.draw.rect(
                    screen, 
                    colors[current_piece_color],
                    [
                        (current_piece_x + x) * game_grid.cell_size, 
                        (current_piece_y + y) * game_grid.cell_size, 
                        game_grid.cell_size, 
                        game_grid.cell_size
                    ]
                )
                pygame.draw.rect(
                    screen, 
                    (255, 255, 255),
                    [
                        (current_piece_x + x) * game_grid.cell_size, 
                        (current_piece_y + y) * game_grid.cell_size, 
                        game_grid.cell_size, 
                        game_grid.cell_size
                    ],
                    1
                )

# Create the first piece
new_piece()

# Main game loop
running = True
while running:
    # Time tracking for piece falling
    delta_time = clock.get_rawtime() / 1000
    fall_time += delta_time
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Key press events
        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT:
                    if not check_collision(-1, 0):
                        current_piece_x -= 1
                        
                elif event.key == pygame.K_RIGHT:
                    if not check_collision(1, 0):
                        current_piece_x += 1
                        
                elif event.key == pygame.K_DOWN:
                    if not check_collision(0, 1):
                        current_piece_y += 1
                        
                elif event.key == pygame.K_UP:
                    rotate_piece()
                    
                elif event.key == pygame.K_SPACE:
                    # Hard drop
                    while not check_collision(0, 1):
                        current_piece_y += 1
                    lock_piece()
                    check_lines()
                    if not new_piece():
                        game_over = True
    
    # Make the piece fall automatically
    if fall_time >= fall_speed and not game_over:
        fall_time = 0
        if not check_collision(0, 1):
            current_piece_y += 1
        else:
            # Lock the piece and create a new one
            lock_piece()
            check_lines()
            if not new_piece():
                game_over = True
    
    # Drawing
    screen.fill(dark_blue)
    
    # Draw the grid
    game_grid.draw(screen)
    
    # Draw the current piece
    if not game_over:
        draw_current_piece()
    
    # Draw score and level
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    # Draw game over text
    if game_over:
        game_over_text = font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(game_over_text, (
            screen.get_width() // 2 - game_over_text.get_width() // 2,
            screen.get_height() // 2 - game_over_text.get_height() // 2
        ))
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit() Example usage:
# start_game()
# Later: stop_game()
 
