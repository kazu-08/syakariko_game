import pygame
from game_step1 import run_step1
from game_step2 import run_step2
from screens.start_screen import show_start_screen
from screens.end_screen import show_end_screen

class GameManager:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        pygame.mixer.init()

        # スタート画面表示
        show_start_screen(self.screen)

        # ゲーム本編ステップ1・ステップ2を実行
        run_step1(self.screen)
        run_step2(self.screen)

        # エンド画面表示
        show_end_screen(self.screen)

        # メインループ終了
        self.running = False
