import pygame
import os


# 스크린 크기
SCREEN_WIDTH = 800 #가로
SCREEN_HEIGHT = 600 #세로
# 색
LAND = (255, 200, 120)

# 초기화
pygame.init()
# 윈도우 제목
pygame.display.set_caption("image")
# 창 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 게임화면 업데이트 속도
clock = pygame.time.Clock()
# 이미지 불러오기
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')
effect_image = pygame.image.load(os.path.join(assets_path, 'click.png'))
# 게임종료 여부
done = False
# 게임 반복 구간
while not done:
    screen.fill(LAND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                size = effect_image.get_width()
                effect_image.get_rect()
                screen.blit(effect_image, (pygame.mouse.get_pos()[0] - size, pygame.mouse.get_pos()[1] - size))

    pygame.display.flip()

    clock.tick(60)
pygame.quit()

