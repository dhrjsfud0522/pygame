import pygame
import random
SC_w = 800
SC_h = 600

pygame.init()
pygame.display.set_caption("pygame")
screen  = pygame.display.set_mode((SC_w, SC_h))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen.fill(WHITE)
rect = pygame.Rect(0, 0, 100, 100)
rect.center = (SC_w//2, SC_h//2)
pygame.draw.rect(screen, BLACK, rect, 0)
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.draw.rect(screen, random.choice([RED, BLUE, GREEN, BLACK]), rect, 0)
                
    
            

    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()