import pygame
import os

# 스크린 크기
SCREEN_WIDTH = 800 #가로
SCREEN_HEIGHT = 600 #세로
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
background_image = pygame.image.load(os.path.join(assets_path, 'land.jpg'))
# 게임종료 여부
done = False
# 게임 반복 구간
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # 게임 로직 구간
    # 화면 삭제 구간
    # 스크린 채우기
    screen.fill(LAND)
    screen.blit(background_image, background_image.get_rect())
    # 화면 그리기
    # 화면 업데이트
    pygame.display.flip()
    # 초당 60프레임으로 업데이트
    clock.tick(60)
pygame.quit()

