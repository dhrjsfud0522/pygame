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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [50, 50, 100, 100], 0)
    pygame.draw.rect(screen, BLUE, [SC_w//2 - 25, SC_h//2 - 25, 50, 50], 0)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()