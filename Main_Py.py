import pygame
try:
    from FinalGameloop import Game  # Ensure the file "Final_Game_loop.py" exists in the same directory as this script
except ModuleNotFoundError:
    raise ImportError("The module 'Final_Game_loop' could not be found. Ensure the file 'Final_Game_loop.py' exists in the same directory.")

# Initialize pygame
pygame.init()

# Game setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Title")
RED = (255, 0, 0)

# Initialize game object
game = Game()

# Load sound
try:
    move_sound = pygame.mixer.Sound("move.wav")  # Ensure move.wav exists in the same directory
except pygame.error:
    move_sound = None

clock = pygame.time.Clock()
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
                if move_sound:
                    pygame.mixer.Sound.play(move_sound)
            elif event.key == pygame.K_RIGHT and game.is_valid_move(1, 0):
                game.current_piece["x"] += 1
                if move_sound:
                    pygame.mixer.Sound.play(move_sound)
            elif event.key == pygame.K_DOWN and game.is_valid_move(0, 1):
                game.current_piece["y"] += 1
            elif event.key == pygame.K_SPACE:
                while game.is_valid_move(0, 1):
                    game.current_piece["y"] += 1
                game.lock_piece()
            elif event.key == pygame.K_UP:
                game.rotate_piece()

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
