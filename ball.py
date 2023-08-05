import pygame

# 스크린 크기
SCREEN_WIDTH = 15 #가로
SCREEN_HEIGHT = 20 #세로
# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# 초기화
pygame.init()
# 윈도우 제목
pygame.display.set_caption("ball")
# 창 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 게임화면 업데이트 속도
clock = pygame.time.Clock()
# 초기화
ball_x = int(SCREEN_WIDTH / 2)
ball_y = int(SCREEN_HEIGHT / 2)
ball_dx = 10
ball_dy = 10
ball_size = int(SCREEN_WIDTH / 10)
# 게임종료 여부
done = False
# 게임 반복 구간
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # 게임 로직 구간
    ball_x += ball_dx
    ball_y += ball_dy
    # 공이 스크린을 나간다!!!
    if(ball_x <= (0 + ball_size) or ball_x >= (SCREEN_WIDTH - ball_size)):
        ball_dx *= -1
    if(ball_y <= (0 + ball_size) or ball_y >= (SCREEN_HEIGHT - ball_size)):
        ball_dy *= -1
    # 화면 삭제 구간
    # 스크린 채우기
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, [ball_x, ball_y], ball_size, 0)
    
    # 화면 그리기
    # 화면 업데이트
    pygame.display.flip()
    # 초당 60프레임으로 업데이트
    clock.tick(60)
pygame.quit()

