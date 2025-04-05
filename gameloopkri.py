import pygame, sys
from game import game
from colours import colours
import random
from block import block
from shapes import IBlock, JBlock, LBlock, OBlock, SBlock, TBlock, ZBlock
from position import Position   

pygame.init()

screen = pygame.display.set_mode((300, 600))  # 10 columns * 30, 20 rows * 30
pygame.display.set_caption("Tetris")

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

