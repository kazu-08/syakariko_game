### game_manager.py
import time
from screens.start_screen import show_start_screen
from screens.end_screen import show_end_screen
from game_step1 import run_step1
from game_step2 import run_step2
from config import init_screen, SCREEN_WIDTH, SCREEN_HEIGHT
from objects.Button import Button


class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.state = "start"  # start, step1, step2, end
        self.start_time = None
        self.jagariko_list = []
        self.score = 0

    def start_game(self):
        self.state = "step1"
        self.start_time = time.time()
        self.jagariko_list = [1] * 10  # 仮のじゃがりこ10本

    def start_step2(self):
        self.state = "step2"
        self.start_time = time.time()

    def update(self):
        if self.state == "start":
            result = show_start_screen(self.screen, self.screen.get_width(), self.screen.get_height())
            if result == "start":
                self.start_game()

        elif self.state == "step1":
            elapsed = time.time() - self.start_time
            run_step1(self.screen, self)
            if elapsed > 45:
                self.start_step2()

        elif self.state == "step2":
            elapsed = time.time() - self.start_time
            run_step2(self.screen, self)
            if elapsed > 45 or len(self.jagariko_list) == 0:
                self.state = "end"

        elif self.state == "end":
            show_end_screen(
                self.screen,
                self.screen.get_width(),
                self.screen.get_height(),
                self.score
            )

        elif self.state == "step1":
            elapsed = time.time() - self.start_time
            run_step1(self.screen, self)
            if elapsed > 45:
                self.start_step2()

        elif self.state == "step2":
            elapsed = time.time() - self.start_time
            run_step2(self.screen, self)
            if elapsed > 45 or len(self.jagariko_list) == 0:
                self.show_end_screen()

        elif self.state == "end":
            show_end_screen(self.screen, self)
            if elapsed > 30 or len(self.jagariko_list) == 0:
                self.state = "end"


    def handle_event(self, event):
        if self.state == "start":
            if event.type == 1025:  # MOUSEBUTTONDOWN
                self.start_game()

    def add_score(self,points):
        self.score += points