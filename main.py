import pygame 
from game import game
from grid import Grid
from shapes import *

# Initialize the pygame
pygame.init()

dark_blue = (44, 44, 120)

screen = pygame.display.set_mode ((300, 600))
pygame.display.set_caption ("Hehe Tetris")

clock = pygame.time.Clock()

game = game()


while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                game.move_left()

            if event.key == pygame.K_RIGHT:
                game.move_right()

            if event.key == pygame.K_DOWN:
                game.move_down()

            
            
    # drawing
    screen.fill (dark_blue)
    game.draw(screen)

    pygame.display.update()
    clock.tick(60) 
    