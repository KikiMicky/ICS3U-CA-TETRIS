import pygame

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Define constants
ROWS = 20
COLUMNS = 10

# Load Background Music
try:
    pygame.mixer.music.load("/mnt/data/musicgametetris.mp3")  # Use the uploaded file
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # Play in a loop
except pygame.error as e:
    print(f"Error loading music: {e}")

# Game Class
class Game:
    def __init__(self):
        self.current_piece = {"x": 0}
        self.grid = [[0] * COLUMNS for _ in range(ROWS)]
        self.score = 0
        self.game_over = False  # Added attribute

    def is_valid_move(self, dx, dy):
        return True  # Placeholder

    def clear_lines(self):
        full_rows = [y for y in range(ROWS) if all(self.grid[y])]
        for y in full_rows:
            del self.grid[y]
            self.grid.insert(0, [0] * COLUMNS)
        self.score += len(full_rows) * 100
        if full_rows and clear_sound:
            pygame.mixer.Sound.play(clear_sound)

# Initialize game
game = Game()
running = True

# Main Game Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and game.is_valid_move(-1, 0):
                game.current_piece["x"] -= 1
                if move_sound: pygame.mixer.Sound.play(move_sound)
            elif event.key == pygame.K_RIGHT and game.is_valid_move(1, 0):
                game.current_piece["x"] += 1
                if move_sound: pygame.mixer.Sound.play(move_sound)
            elif event.key == pygame.K_p:  # Pause Music
                pygame.mixer.music.pause()
            elif event.key == pygame.K_r:  # Resume Music
                pygame.mixer.music.unpause()
    
    if game.game_over:
        pygame.mixer.music.stop()

pygame.quit()

