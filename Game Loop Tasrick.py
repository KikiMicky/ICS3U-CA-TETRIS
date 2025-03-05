import pygame
import time

# Simple game loop with no dependencies

# Game state
game_running = False
last_time = 0
score = 0

# Game loop function
def game_loop():
    global last_time, score, game_running
    while game_running:
        # Calculate delta time (time since last frame)
        current_time = time.time() * 1000  # Convert to milliseconds
        if not last_time:
            last_time = current_time
        delta_time = current_time - last_time
        last_time = current_time

        # Update game state (once every 500ms)
        if delta_time > 500:
            # Update score
            score += 1
            print("Score:", score)

            # Example game logic: end game after score reaches 10
            if score >= 10:
                print("Game over!")
                game_running = False
                return  # Exit the loop

        time.sleep(0.016)  # Sleep to simulate frame rate (60 FPS)

#