import pygame

# Initialize pygame
pygame.init()

# Colors
DARK_BLUE = (44, 44, 120)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Tetris")

# Clock
clock = pygame.time.Clock()

class Grid:
    def __init__(self):
        self.grid = [[0 for _ in range(10)] for _ in range(20)]

    def print_grid(self):
        for row in self.grid:
            print(row)

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell != 0:
                    pygame.draw.rect(screen, (200, 200, 200), 
                                     (x * 30, y * 30, 30, 30), 0)

# Placeholder for game object
class Game:
    def __init__(self):
        self.current_piece = {"x": 4, "y": 0}
        self.game_over = False
        self.grid = Grid()

    def is_valid_move(self, piece, dx, dy):
        new_x = piece["x"] + dx
        new_y = piece["y"] + dy
        return 0 <= new_x < 10 and 0 <= new_y < 20  # Basic boundary check

    def rotate_piece(self, piece):
        pass  # Placeholder for piece rotation

    def drop_piece(self):
        pass  # Placeholder for piece dropping

    def update(self):
        self.current_piece["y"] += 1  # Simple falling logic
        if self.current_piece["y"] >= 19:
            self.game_over = True  # End game if piece reaches bottom

    def draw(self, screen):
        pygame.draw.rect(screen, RED, 
                         (self.current_piece["x"] * 30, 
                          self.current_piece["y"] * 30, 30, 30))
        self.grid.draw(screen)

# Initialize game
game = Game()

# Game loop
running = True
fall_time = 0

while running:
    screen.fill(BLACK)
    fall_speed = 500  # 500ms per move down
    time_passed = clock.tick(60)
    fall_time += time_passed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and game.is_valid_move(game.current_piece, -1, 0):
                game.current_piece["x"] -= 1
            elif event.key == pygame.K_RIGHT and game.is_valid_move(game.current_piece, 1, 0):
                game.current_piece["x"] += 1
            elif event.key == pygame.K_DOWN and game.is_valid_move(game.current_piece, 0, 1):
                game.current_piece["y"] += 1
            elif event.key == pygame.K_UP:
                game.rotate_piece(game.current_piece)
            elif event.key == pygame.K_SPACE:
                game.drop_piece()

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
