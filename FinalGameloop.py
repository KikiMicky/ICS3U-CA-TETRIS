import pygame

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Screen settings
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris with Music")

# Load Background Music
try:
    pygame.mixer.music.load("musicgametetris.mp3")  # Ensure the file is in the same directory
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  # Loop indefinitely
except pygame.error as e:
    print(f"Error loading music: {e}")

# Define Game Class
class Game:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.handle_events()
            screen.fill((0, 0, 0))  # Black background
            pygame.display.flip()
            self.clock.tick(30)  # Limit FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pygame.mixer.music.pause()  # Pause music
                elif event.key == pygame.K_r:
                    pygame.mixer.music.unpause()  # Resume music
                elif event.key == pygame.K_s:
                    pygame.mixer.music.stop()  # Stop music

# Run the game
game = Game()
game.run()
pygame.quit()