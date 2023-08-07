import pygame

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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [50, 50, 100, 100], 0)
    rect2 = pygame.Rect(0, 0, 50, 50)
    rect2.center = (SC_w//2, SC_h//2)
    pygame.draw.rect(screen, BLUE, rect2, 0)
    rect3 = pygame.Rect(200, 200, 20, 20)
    rect4 = pygame.Rect(200, 200, 40, 40)
    pygame.draw.rect(screen, GREEN, rect4, 0)
    pygame.draw.rect(screen, RED, rect3, 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()