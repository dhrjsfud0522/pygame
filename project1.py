import pygame
import random
import time

SC_w = 800
SC_h = 600

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.display.set_caption("project")
screen = pygame.display.set_mode((SC_w, SC_h))
clock = pygame.time.Clock()

now = 0

def frame(n):
    screen.fill(BLACK)
    font = pygame.font.SysFont("맑은 고딕", 100, False, False)
    text = font.render(n, True, WHITE)
    screen.blit(text, [SC_w//2 - 130, SC_h//2 - 25])

def wait():
    time.sleep(random.randint(2, 3))
    screen.fill(GREEN)
    return 1

running = True
frame("REDAY")
pygame.display.flip()
now = wait()
pygame.display.flip()
while running:
    print(now)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if now == 1:
                frame("WIN")
            else:
                frame("LOSE")
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

