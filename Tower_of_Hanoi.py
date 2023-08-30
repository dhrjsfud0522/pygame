import pygame
import os

SC_w = 900
SC_h = 700


current_path = os.path.dirname("__file__")
assets_path = os.path.join(current_path, "assets")

class Game():
    def __init__(self):
        pygame.mixer.music.load(os.path.join(assets_path, "bgm.mp3"))
        self.menu_on = True
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.menu_on:
                
            else:
        return True
    
    def run_logic(self, screen):     
        self.menu_on = True

    def display_menu(self, screen):
        self.draw_text(screen, "Press Space Key to Play", self.font, center_x, center_y, DARK_GROUND)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SC_w, SC_h))
    pygame.display.set_caption("Tower of Hanoi")
    clock = pygame.time.Clock()
    game = Game()
    running = True
    while running:
        running = game.process_events()
        if game.menu_on:
            game.display_menu(screen)
        else:
            game.run_logic(screen)
            game.display_frame(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

main()