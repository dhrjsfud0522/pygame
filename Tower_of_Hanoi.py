import pygame
import os

sc_w = 800
sc_h = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BASE = (153, 102, 0)
BACKGROUND = (153, 153, 153)

#class ring():



def main():
    pygame.init()
    pygame.display.set_caption("Tower_of_Hanoi")
    screen = pygame.display.set_mode((sc_w, sc_h))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BACKGROUND)
        pygame.draw.rect(screen, BASE, [0, 500, 800, 600], 0)
        pygame.draw.rect(screen, BASE, [138, 240, 24, 300], 0)
        pygame.draw.rect(screen, BASE, [388, 240, 24, 300], 0)
        pygame.draw.rect(screen, BASE, [638, 240, 24, 300], 0)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


main()
