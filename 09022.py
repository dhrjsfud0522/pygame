import pygame
import random

sc_w = 600
sc_h = 600

BLACK = (0, 0 , 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.display.set_caption("이차식아")
screen = pygame.display.set_mode((sc_w, sc_h))
clock = pygame.time.Clock()

ball_s = 20
x = sc_w//2
y = sc_h//2
dx = 3
dy = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, [x, y], ball_s, 0)
    x += dx * 2 
    y += dy * 3
    if x >= (sc_w - ball_s) or x <= (0 + ball_s):
        dx *= -1
    if y >= (sc_h - ball_s) or y <= (0 + ball_s):
        dy *= -1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()