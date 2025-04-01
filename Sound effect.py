import pygame

# Initialize pygame
pygame.init()

# Define constants
ROWS = 20
COLUMNS = 10

# Mock event and game objects for demonstration purposes
event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
class Game:
    def __init__(self):
        self.current_piece = {"x": 0}
        self.grid = [[0] * COLUMNS for _ in range(ROWS)]
        self.score = 0

    def is_valid_move(self, dx, dy):
        # Placeholder for actual move validation logic
        return True

game = Game()

# Load Sounds
try:
    move_sound = pygame.mixer.Sound("move.wav")
    clear_sound = pygame.mixer.Sound("clear.wav")
except pygame.error:
    move_sound = None
    clear_sound = None

if event.key == pygame.K_LEFT and game.is_valid_move(-1, 0):
    game.current_piece["x"] -= 1
    if move_sound: pygame.mixer.Sound.play(move_sound)

elif event.key == pygame.K_RIGHT and game.is_valid_move(1, 0):
    game.current_piece["x"] += 1
    if move_sound: pygame.mixer.Sound.play(move_sound)

def clear_lines(self):
    full_rows = [y for y in range(ROWS) if all(self.grid[y])]
    for y in full_rows:
        del self.grid[y]
        self.grid.insert(0, [0] * COLUMNS)
    self.score += len(full_rows) * 100
    if full_rows and clear_sound:
        pygame.mixer.Sound.play(clear_sound)  # Play sound when lines are cleared
