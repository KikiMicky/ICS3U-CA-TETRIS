import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30  # Size of each block
COLUMNS = WIDTH // GRID_SIZE
ROWS = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris Game")
clock = pygame.time.Clock()

# Tetromino shapes
tetrominoes = [
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # O
    [(0, 0), (-1, 0), (1, 0), (2, 0)],  # I
    [(0, 0), (1, 0), (-1, 0), (-1, 1)],  # L
    [(0, 0), (1, 0), (-1, 0), (1, 1)],  # J
    [(0, 0), (-1, 0), (0, 1), (1, 1)],  # S
    [(0, 0), (1, 0), (0, 1), (-1, 1)],  # Z
    [(0, 0), (-1, 0), (1, 0), (0, 1)],  # T
]

# Load Sounds
try:
    move_sound = pygame.mixer.Sound("move.wav")
    clear_sound = pygame.mixer.Sound("clear.wav")
except pygame.error:
    move_sound = None
    clear_sound = None

class Game:
    def __init__(self):
        self.current_piece = {"shape": random.choice(tetrominoes), "x": COLUMNS // 2, "y": 0}
        self.grid = [[0] * COLUMNS for _ in range(ROWS)]
        self.game_over = False

    def is_valid_move(self, dx, dy):
        for block in self.current_piece["shape"]:
            x = self.current_piece["x"] + block[0] + dx
            y = self.current_piece["y"] + block[1] + dy
            if x < 0 or x >= COLUMNS or y >= ROWS or (y >= 0 and self.grid[y][x] != 0):
                return False
        return True

    def drop_piece(self):
        if self.is_valid_move(0, 1):
            self.current_piece["y"] += 1
        else:
            self.lock_piece()

    def lock_piece(self):
        for block in self.current_piece["shape"]:
            x = self.current_piece["x"] + block[0]
            y = self.current_piece["y"] + block[1]
            if y >= 0:
                self.grid[y][x] = 1
        self.current_piece = {"shape": random.choice(tetrominoes), "x": COLUMNS // 2, "y": 0}
        if not self.is_valid_move(0, 0):
            self.game_over = True

    def update(self):
        self.drop_piece()

    def draw(self, screen):
        screen.fill(BLACK)
        for block in self.current_piece["shape"]:
            x = (self.current_piece["x"] + block[0]) * GRID_SIZE
            y = (self.current_piece["y"] + block[1]) * GRID_SIZE
            pygame.draw.rect(screen, WHITE, (x, y, GRID_SIZE, GRID_SIZE))
        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.grid[y][x] == 1:
                    pygame.draw.rect(screen, WHITE, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Game instance
game = Game()

# Game loop
running = True
fall_time = 0
fall_speed = 500

while running:
    time_passed = clock.tick(60)
    fall_time += time_passed

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
            elif event.key == pygame.K_DOWN and game.is_valid_move(0, 1):
                game.current_piece["y"] += 1
            elif event.key == pygame.K_SPACE:
                while game.is_valid_move(0, 1):
                    game.current_piece["y"] += 1
                game.lock_piece()

    if fall_time >= fall_speed:
        game.update()
        fall_time = 0

    game.draw(screen)
    pygame.display.update()

    if game.game_over:
        font = pygame.font.Font(None, 50)
        text = font.render("Game Over!", True, RED)
        screen.blit(text, (WIDTH // 4, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

pygame.quit()