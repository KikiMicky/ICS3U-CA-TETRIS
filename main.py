import pygame 


# Initialize the pygame
pygame.init()

dark_blue = (44, 44, 125)

screen = pygame.display.set_mode ((300, 600))
pygame.display.set_caption ("Python Tetris")

clock = pygame.time.clock()

while True:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    # drawing
    screen.fill (drak_blue)
    pygame.display.update()
    clock.tick(60)     