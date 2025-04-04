import pygame , sys
from game import game
from grid import Grid
from shapes import *


# Initialize the pygame
pygame.init()


screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("HEHE TETRIS")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
RED = (255, 69, 0)
BLUE = (100, 149, 237)
PURPLE = (128, 0, 128)

pygame.font.init()
title_font = pygame.font.Font(None, 50)
button_font = pygame.font.Font(None, 25)
score_font = pygame.font.Font(None, 20)

high_scores = [6000, 5000, 4000, 2000, 1000]
button_rect = pygame.Rect(120, 280, 60, 60)  # x, y, width, height

game = game ()

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_start_screen():
    screen.fill(BLACK)
#-----------------------------------------
# double decoration for title
    draw_text("T", title_font, (255, 69, 0), 90, 120)
    draw_text("E", title_font, (255, 160, 122), 160, 120)
    draw_text("T", title_font, (255, 244, 178), 240, 120)
    draw_text("R", title_font, (50, 205, 50), 310, 120)
    draw_text("I", title_font, (100, 149, 237), 393, 120)
    draw_text("S", title_font, (128, 0, 128), 423, 120)

    draw_text("T", title_font, (255, 255, 255), 80, 110)
    draw_text("E", title_font, (255, 255, 255), 150, 110)
    draw_text("T", title_font, (255, 255, 255), 230, 110)
    draw_text("R", title_font, (255, 255, 255), 300, 110)
    draw_text("I", title_font, (255, 255, 255), 383, 110)
    draw_text("S", title_font, (255, 255, 255), 413, 110)
   
#the triangles to play/start the game
    pygame.draw.polygon(screen, PURPLE, [(150, 250), (180, 280), (150, 310)], 0)
    pygame.draw.polygon(screen, WHITE, [(150, 250), (180, 280), (150, 310)], 2)

    draw_text("PRESS START", button_font, WHITE, 95, 340)

    draw_text("⇩ HIGH RECORDS ⇩", score_font, WHITE, 75, 400)
    pygame.draw.rect(screen, GREEN, (50, 420, 200, 120), 2)  # Green box outline

    for i, score in enumerate(high_scores):
        draw_text(f"{i+1}.   {score}", score_font, WHITE, 100, 440 + i * 20)

    pygame.display.flip()

#to let the player know the game is starting
def main():
    running = True
    while running:
        draw_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit ()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Game Started!")  
                    running = False 
                    game_loop ()
                    sys.exit ()



def game_loop ():
 clock = pygame.time.Clock()
 dark_blue = (44,44,120)

 running =True
 while running:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit ()
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
    
main()

