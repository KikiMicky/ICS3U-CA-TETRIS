import pygame, sys
from game import game
from colours import colours
import random
from block import block
from shapes import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock
from position import Position

pygame.init()

screen = pygame.display.set_mode((300, 600))  # 10 columns * 30, 20 rows * 30
pygame.display.set_caption("HEHE Tetris")

game_instance = game()  # this creates the game object

def game_loop():
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.5  # Seconds per block drop (adjust this to change fall speed)

    running = True
    while running:
        screen.fill((44, 44, 120))  # Background color

        # Track time passed to trigger block falling automatically
        fall_time += clock.get_rawtime() / 1000  # Convert milliseconds to seconds
        clock.tick(60)  # 60 FPS

        # If it's time to move the block down, do it automatically
        if fall_time > fall_speed:
            game_instance.move_down()  # Moves the block down one step
            # If the block hits the bottom or another block, lock it
            if not game_instance.block_inside_grid():
                game_instance.move_up()  # Undo move down
                game_instance.lock_block()  # Lock the block in place
                game_instance.clear_rows()  # Clear full rows
                game_instance.spawn_new_block()  # Spawn a new block
                # Game over condition (if new block can't be placed)
                if not game_instance.block_inside_grid():
                    print("Game Over!")
                    running = False  # End game
            fall_time = 0  # Reset fall time to start the cycle again

        # --- Handle Events (User Input) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game_instance.move_left()
                    if not game_instance.block_inside_grid():
                        game_instance.move_right()  # Undo move if it goes out of bounds

                elif event.key == pygame.K_RIGHT:
                    game_instance.move_right()
                    if not game_instance.block_inside_grid():
                        game_instance.move_left()  # Undo move if it goes out of bounds

                elif event.key == pygame.K_DOWN:
                    game_instance.move_down()  # Manual move down
                    if not game_instance.block_inside_grid():
                        game_instance.move_up()  # Undo move if it goes out of bounds
                        game_instance.lock_block()  # Lock the block in place
                        game_instance.clear_rows()  # Clear full rows
                        game_instance.spawn_new_block()  # Spawn a new block
                        if not game_instance.block_inside_grid():
                            print("Game Over!")
                            running = False  # End game

        # --- Drawing ---
        game_instance.draw(screen)  # Draw the game state (grid + current block)
        pygame.display.update()  # Update the display


# To let the player know the game is starting
def main():
    running = True
    while running:
        draw_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Game Started!")
                    running = False
                    game_loop()
                    sys.exit()


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def draw_start_screen():
    screen.fill(BLACK)
    # Double decoration for title
    draw_text("T", title_font, (255, 69, 0), 20, 120)
    draw_text("E", title_font, (255, 160, 122), 70, 120)
    draw_text("T", title_font, (255, 244, 178), 110, 120)
    draw_text("R", title_font, (50, 205, 50), 150, 120)
    draw_text("I", title_font, (100, 149, 237), 210, 120)
    draw_text("S", title_font, (128, 0, 128), 230, 120)

    draw_text("T", title_font, (255, 255, 255), 12, 115)
    draw_text("E", title_font, (255, 255, 255), 62, 115)
    draw_text("T", title_font, (255, 255, 255), 92, 115)
    draw_text("R", title_font, (255, 255, 255), 132, 115)
    draw_text("I", title_font, (255, 255, 255), 192, 115)
    draw_text("S", title_font, (255, 255, 255), 212, 115)

    # The triangles to play/start the game
    pygame.draw.polygon(screen, PURPLE, [(135, 240), (195, 280), (135, 320)], 0)
    pygame.draw.polygon(screen, WHITE, [(135, 240), (195, 280), (135, 320)], 3)

    draw_text("PRESS START", button_font, WHITE, 30, 340)

    draw_text("⇩ HIGH RECORDS ⇩", score_font, WHITE, 60, 400)
    pygame.draw.rect(screen, GREEN, (50, 430, 200, 120), 2)  # Green stuff

    for i, score in enumerate(high_scores):
        draw_text(f"{i+1}.   {score}", score_font, WHITE, 100, 440 + i * 20)

    pygame.display.flip()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
RED = (255, 69, 0)
BLUE = (100, 149, 237)
PURPLE = (128, 0, 128)

pygame.font.init()
title_font = pygame.font.Font(None, 120)
button_font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 30)

high_scores = [6000, 5000, 4000, 2000, 1000]
button_rect = pygame.Rect(90, 220, 120, 120)  # x, y, width, height

game = game()

# Start the game
main()
