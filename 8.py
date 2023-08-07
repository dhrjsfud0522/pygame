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

x = SC_w//2
y = SC_h//2

dx = 0
dy = 0

rect = pygame.Rect(0, 0, 20, 20)
rect.center = (SC_w//2, SC_h//2)

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -5
            elif event.key == pygame.K_RIGHT:
                dx = 5
            elif event.key == pygame.K_UP:
                  dy = -5
            elif event.key == pygame.K_DOWN:
                dy = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                dy = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0
    if x + dx >= 10 and x + dx <= 790:
        x += dx
    if y + dy >= 10 and y + dy <= 590:
        y += dy
    rect.center = (x, y)
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, rect, 0)
              
    
            
      
    pygame.display.flip()
    
    clock.tick(60)
pygame.quit()