import pygame 
from grid import Grid

# Initialize the pygame
pygame.init()

dark_blue = (44, 44, 120)

screen = pygame.display.set_mode ((300, 600))
pygame.display.set_caption ("Python Tetris")

clock = pygame.time.Clock()

game_grid = Grid ()

game_grid.grid [0][0] = 1
game_grid.grid [3][4] = 4
game_grid.grid [17][8] = 7


game_grid.print_grid()

while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    # drawing
    screen.fill (dark_blue)
    game_grid.draw(screen)
    pygame.display.update()
    clock.tick(60)     