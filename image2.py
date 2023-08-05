import pygame
import os

# 스크린 크기
SCREEN_WIDTH = 640 #가로
SCREEN_HEIGHT = 320 #세로
# 색
LAND = (160, 120, 40)
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
background_image = pygame.image.load(os.path.join(assets_path, 'terrain.png'))
mushroom_image_1 = pygame.image.load(os.path.join(assets_path, 'mushroom1.png'))
mushroom_image_2 = pygame.image.load(os.path.join(assets_path, 'mushroom2.png'))
mushroom_image_3 = pygame.image.load(os.path.join(assets_path, 'mushroom3.png'))
# 게임종료 여부
done = False
# 게임 반복 구간
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(LAND)
    screen.blit(background_image, background_image.get_rect())
    screen.blit(mushroom_image_1, [100, 80])
    screen.blit(mushroom_image_2, [300, 100])
    screen.blit(mushroom_image_3, [450, 140])

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)
pygame.quit()