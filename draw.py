import pygame

# 스크린 크기
SCREEN_WIDTH = 800 #가로
SCREEN_HEIGHT = 800 #세로
# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# 초기화
pygame.init()
# 윈도우 제목
pygame.display.set_caption("그림그리기")
# 창 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 게임화면 업데이트 속도
clock = pygame.time.Clock()

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
    screen.fill(WHITE)
    # 화면 그리기
    pygame.draw.line(screen, RED, [50, 50], [500, 500], 10)
    pygame.draw.line(screen, RED, [500, 50], [50, 500], 10)
    pygame.draw.rect(screen, BLUE, [0, 0, 500, 500], 10)
    pygame.draw.line(screen, BLUE, [250, 0], [250, 500], 10)
    pygame.draw.line(screen, BLUE, [0, 250], [500, 250], 10)
    pygame.draw.circle(screen, GREEN, [300, 300], 200, 0)
    pygame.draw.polygon(screen, RED, [[400,200],[200,400],[600,400]], 0)
    pygame.draw.ellipse(screen, BLUE, [200, 400, 200, 100], 10)
    font = pygame.font.SysFont("맑은 고딕", 100, False, True)
    text = font.render("Text", True, BLACK)
    screen.blit(text, [200, 600])

    # 화면 업데이트
    pygame.display.flip()
    # 초당 60프레임으로 업데이트
    clock.tick(60)
pygame.quit()

