import pygame
pygame.init()
window = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
pygameSurface = pygame.image.load('click_.png').convert_alpha()
background = pygame.Surface(window.get_size())
ts, w, h, c1, c2 = 50, *window.get_size(), (160, 160, 160), (192, 192, 192)
tiles = [((x*ts, y*ts, ts, ts), c1 if (x+y) % 2 == 0 else c2) for x in range((w+ts-1)//ts) for y in range((h+ts-1)//ts)]
for rect, color in tiles:
    pygame.draw.rect(background, color, rect)
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.blit(background, (0, 0))
    window.blit(pygameSurface, pygameSurface.get_rect(center = window.get_rect().center))
    pygame.display.flip()
pygame.quit()
exit()




