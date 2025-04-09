import pygame, sys
from game import game
from colours import colours
import random
from block import block
from shapes import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock
from position import Position
from final_loop import *

pygame.init()

screen = pygame.display.set_mode((300, 600))  # 10 columns * 30, 20 rows * 30
pygame.display.set_caption("HEHE Tetris")

game_instance = game()  # this creates the game object


def game_loop():
    clock = pygame.time.Clock()  # Create a clock to control the frame rate (speed)
    fall_time = 0  # Timer to control how often the block falls
    fall_speed = 0.5  # Speed at which blocks fall (lower = faster fall)

    running = True  # Set the game loop to keep running
    while running:  # Keep running the game loop as long as this is True
        screen.fill((44, 44, 120))  # Set the background color to a dark blue-ish color

        dt = clock.tick(60) / 1000  # Get the time delta (time passed) since the last frame
        fall_time += dt  # Add the time delta to the fall time (to control the speed of blocks falling)

        # If enough time has passed, move the block down
        if fall_time > fall_speed:
            game_instance.move_down()  # Move the current block down
            if not game_instance.block_inside_grid():  # Check if the block is inside the grid
                game_instance.move_up()  # Undo the move if the block goes out of bounds
                game_instance.lock_block()  # Lock the block in place if it can't go down further
                game_instance.clear_rows()  # Clear any full rows in the grid
                game_instance.spawn_new_block()  # Spawn a new block at the top
                if not game_instance.block_inside_grid():  # If there's no space for the new block
                    print("Game Over!")  # Print "Game Over!"
                    running = False  # End the game loop (game over)
            fall_time = 0  # Reset the fall timer after moving the block down

        # --- Handle user input ---
        for event in pygame.event.get():  # Get all the events (user actions like key presses)
            if event.type == pygame.QUIT:  # If the user closes the window
                pygame.quit()  # Quit Pygame
                sys.exit()  # Exit the program

            if event.type == pygame.KEYDOWN:  # If a key is pressed
                if event.key == pygame.K_LEFT:  # If the left arrow key is pressed
                    game_instance.move_left()  # Move the block left
                    if not game_instance.block_inside_grid():  # If the block goes out of bounds
                        game_instance.move_right()  # Undo the move and move it back to the right

                elif event.key == pygame.K_RIGHT:  # If the right arrow key is pressed
                    game_instance.move_right()  # Move the block right
                    if not game_instance.block_inside_grid():
                        game_instance.move_left()  # Undo the move if it goes out of bounds
                
                elif event.key == pygame.K_UP:  # If the up arrow key is pressed (rotate block)
                    game_instance.current_block.rotate()  # Rotate the block

                elif event.key == pygame.K_DOWN:  # If the down arrow key is pressed (manual move down)
                    game_instance.move_down()  # Move the block down
                    if not game_instance.block_inside_grid():  # Check if the block is out of bounds
                        game_instance.move_up()  # Undo the move if out of bounds
                        game_instance.lock_block()  # Lock the block in place
                        game_instance.clear_rows()  # Clear full rows
                        game_instance.spawn_new_block()  # Spawn a new block
                        if not game_instance.block_inside_grid():  # If there's no space for the new block
                            print("Game Over!")  # Print "Game Over!"
                            running = False  # End the game

            

        # --- Drawing ---
        screen.fill (PURPLE)
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

