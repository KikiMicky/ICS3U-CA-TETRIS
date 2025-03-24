# the cover of the game 

import pygame

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Game Start Screen")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (50, 205, 50)
RED = (255, 69, 0)
BLUE = (100, 149, 237)
PURPLE = (128, 0, 128)

pygame.font.init()
title_font = pygame.font.Font(None, 180)
button_font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 30)

high_scores = [6000, 5000, 4000, 2000, 1000]
button_rect = pygame.Rect(250, 360, 70, 40)  # x, y, width, height


def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw():
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
    pygame.draw.polygon(screen, PURPLE, [(250, 330), (320, 380), (250, 430)], 0)
    pygame.draw.polygon(screen, WHITE, [(250, 330), (320, 380), (250, 430)], 2)

    draw_text("PRESS START", button_font, WHITE, 170, 450)

    draw_text("⇩ HIGH RECORDS ⇩", score_font, WHITE, 200, 520)
    pygame.draw.rect(screen, GREEN, (150, 550, 300, 200), 2)  # Green box outline

    for i, score in enumerate(high_scores):
        draw_text(f"{i+1}.   {score}", score_font, WHITE, 200, 580 + i * 30)

    pygame.display.flip()

#to let the player know the game is starting
def main():
    running = True
    while running:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("Game Started!")  #message
        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()
