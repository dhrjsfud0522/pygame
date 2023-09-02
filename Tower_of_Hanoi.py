import pygame
import os

sc_w = 800
sc_h = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
B = (153, 102, 0)
C = (153, 153, 153)

pygame.init()
pygame.display.set_caption("Tower_of_Hanoi")
screen = pygame.display.set_mode((sc_w, sc_h))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(C)
    pygame.draw.rect(screen, B, [0, 500, 800, 600], 0)
    pygame.draw.rect(screen, B, [135, 240, 30, 300], 0)
    pygame.draw.rect(screen, B, [385, 240, 30, 300], 0)
    pygame.draw.rect(screen, B, [635, 240, 30, 300], 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

