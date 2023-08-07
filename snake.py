import pygame
import random
from time import sleep

SCREEN_WIDTH = 800
SCRENN_HEIGHT = 600

GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH / GRID_SIZE
GRID_HEIGHTH = SCRENN_HEIGHT / GRID_SIZE

WHITE = (255, 255, 255)
ORANGE = (2250, 150, 0)
GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake():
    """뱀 객체"""
    def __init__(self):
        self.create()

    def create(self):
        """뱀 새로 생성"""
        self.length = 2
        self.positions = [(int(SCREEN_WIDTH / 2), int(SCRENN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def control(self, xy):
        """뱀 방향 조정"""
        if (xy[0] * -1, xy[1] * -1) == self.direction:
            return
        else:
            self.direction = xy

    def move(self):
        """뱀 이동"""
        cur = self.positions[0]
        x, y = self.direction
        new = (cur[0] + (x * GRID_SIZE)), (cur[1] + (y * GRID_SIZE))
        if new in self.positions[2:]:
            sleep(1)
            self.create()
        elif new[0] < 0 or new[0] >= SCREEN_WIDTH or \
             new[1] < 0 or new[1] >= SCRENN_HEIGHT:
            sleep(1)
            self.create()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
            
    def eat(self):
        """뱀이 먹이를 먹을 때"""
        self.length += 1

    def draw(self, screen):
        """뱀 그리기"""
        for p in self.positions:
            rect = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, GRAY, rect)

class Feed():
    """먹이 객체"""
    def __init__(self):
        
        self.position = (0,0)
        self.color = ORANGE
        self.create()
    
    def create(self):
        """먹이 생성"""
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHTH - 1)
        self.position = x * GRID_SIZE, y * GRID_SIZE

    def draw(self, screen):
        """먹이 그리기"""
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.color, rect)

class Game():
    """게임 객체"""
    def __init__(self):
        self.snake = Snake()
        self.feed = Feed()
        self.speed = 5

    def process_events(self):
        """게임 이벤트 처리 및 조작"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.control(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.control(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.control(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.control(RIGHT)
        return False
    
    def run_logic(self):
        """게임 로직 수행"""
        self.snake.momve()
        self.check_eat(self.snake, self.feed)
        self.speed = (10 + self.snake.length) / 2
    
    def check_eat(snake, feed):
        """뱀이 먹이를 먹었는지 체크"""
        if snake.positions[0] == feed.position:
            snake.eat()
            feed.create()
    
    def draw_info(self, length, speed, screen):
        """게임 정보 출력"""
        info = "Length: " + str(length) + "     " + "Speed: " + str(round(speed, 2))
        font = pygame.font.SysFont("FixedSys", 30, False, False)
        text_obj = font.render(info, True, BLACK)
        text_rect = text_obj.get_rect()
        text_rect.x, text_rect.y = 10, 10
        screen.blit(text_obj, text_rect)

    def display_frame(self, screen):
        """게임 프레임 정리"""
        screen.fill(WHITE)
        self.draw_info(self.snake.length, self.speed, screen)
        self.snake.draw(screen)
        self.feed.draw(screen)
        screen.blit(screen, (0, 0))

def main():
    """게임 초기화 및 환경 설정"""
    pygame.init()
    pygame.display.set_caption("Snake Game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCRENN_HEIGHT))
    clock = pygame.time.Clock()

    done = False
    while(not done):
        game = Game()
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(game.speed)
        

    pygame.quit

if(__name__ == '__main__'):
    main()