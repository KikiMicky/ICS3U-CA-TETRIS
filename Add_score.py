import pygame
import random

# Define constants
ROWS = 20
COLUMNS = 10
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((300, 600))

# Example tetrominoes list
tetrominoes = ["I", "O", "T", "S", "Z", "J", "L"]

class Game:
    def __init__(self):
        self.grid = [[0] * COLUMNS for _ in range(ROWS)]
        self.score = 0
        self.next_piece = random.choice(tetrominoes)
        self.current_piece = {"shape": self.next_piece, "x": COLUMNS // 2, "y": 0}

    def clear_lines(self):
        full_rows = [y for y in range(ROWS) if all(self.grid[y])]
        for y in full_rows:
            del self.grid[y]
            self.grid.insert(0, [0] * COLUMNS)
        self.score += len(full_rows) * 100  # Increase score for cleared lines

        font = pygame.font.Font(None, 30)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        self.next_piece = random.choice(tetrominoes)
        self.current_piece = {"shape": self.next_piece, "x": COLUMNS // 2, "y": 0}
        self.next_piece = random.choice(tetrominoes)
