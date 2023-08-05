import pygame
import os

SCREEN_WIDTH = 640
SCREEN_HIEGHT = 400

BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("sound")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIEGHT))
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
equalizer_image = pygame.image.load(os.path.join(assets_path, "equalizer.png"))
pygame.mixer.music.load(os.path.join(assets_path, "bgm.wav"))
pygame.mixer.music.play(-1)
sound = pygame.mixer.Sound(os.path.join(assets_path, 'sound.wav'))
done = False

while(not done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif(event.type == pygame.MOUSEBUTTONDOWN):
            sound.play()
    screen.fill(BLACK)
    screen.blit(equalizer_image, equalizer_image.get_rect())
    pygame.display.flip()
    clock.tick(60)

pygame.quit()