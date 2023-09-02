import pygame
import os

sc_w = 800
sc_h = 400

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
SKY_BLUE = (153, 255, 255)
RED = (255, 0, 0)


pygame.init()
pygame.display.set_caption("복습")
screen = pygame.display.set_mode((sc_w, sc_h))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

fish_image = pygame.image.load(os.path.join(assets_path, 'fish.png'))


x = 200
y = 200
dx = 0
dy = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key ==pygame. K_UP:
                    dy = -4
            elif event.key ==pygame. K_DOWN:
                dy = 4
            elif event.key ==pygame. K_RIGHT:
                dx = 4
            elif event.key ==pygame. K_LEFT:
                dx = -4
        elif event.type == pygame.KEYUP:
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                dx = 0
            elif(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                dy = 0
    screen.fill(WHITE)
    pygame.draw.line(screen, RED, [50, 50], [300, 300], 50)
    pygame.draw.line(screen, RED, [300, 50], [50, 300], 50)
    pygame.draw.rect(screen, GREEN, [200, 200, 50, 50], 0)
    pygame.draw.circle(screen, BLACK, [300, 300], 10, 3)
    
    font = pygame.font.SysFont("Malgun Gothic", 120, False, False)
    text = font.render("이서준 저리가", True, BLACK)
    screen.blit(text, [10, 10])
    font = pygame.font.SysFont("Malgun Gothic", 10, False, False)
    text2 = font.render("9월 2일 토요일", True, BLACK)
    screen.blit(text2, [50, 50])
    screen.blit(fish_image, [x, y])

    x += dx
    y +=dy
    pygame.display.flip()
    clock.tick(60)
pygame.quit()