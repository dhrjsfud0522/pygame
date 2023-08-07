import pygame

SC_w = 800
SC_h = 600

pygame.init()
pygame.display.set_caption("pygame")
screen  = pygame.display.set_mode((SC_w, SC_h))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()