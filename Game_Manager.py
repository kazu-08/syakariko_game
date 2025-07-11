import pygame
import sys
from game_step1 import Step1
from game_step2 import Step2
from screens import show_start_screen, show_end_screen



# game_manager.py
class GameManager:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.state = "start"  # 最初はタイトル画面
        self.score = 0
        self.step1 = None
        self.step2 = None
    def handle_event(self, event):
        if self.state == "start":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.step1 = Step1(self.screen)
                self.state = "step1"
        elif self.state == "step1":
            self.step1.handle_event(event)
        elif self.state == "step2":
            self.step2.handle_event(event)
        elif self.state == "end":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = "start"
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    def update(self):
        if self.state == "step1":
            self.step1.update()
            if self.step1.is_finished():
                self.step2 = Step2(self.screen, self.step1.get_collected_data())
                self.state = "step2"
        elif self.state == "step2":
            self.step2.update()
            if self.step2.is_finished():
                self.score = self.step2.get_score()
                self.state = "end"
    def draw(self):
        if self.state == "start":
            show_start_screen(self.screen, self.width, self.height)
        elif self.state == "step1":
            self.step1.draw()
        elif self.state == "step2":
            self.step2.draw()
        elif self.state == "end":
            show_end_screen(self.screen, self.width, self.height, self.score)






