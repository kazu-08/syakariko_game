# screens/start_screen.py
import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from objects.Button import Button  # ここでButtonクラスを読み込む


def show_start_screen(screen, width, height):
    font_title = pygame.font.SysFont(None, 72)

    # タイトル表示のための surface
    title_surface = font_title.render("syakariko-game", True, (0, 0, 0))

    # "start" ボタンの作成（中心に配置）
    start_button = Button(shape="circle", x=width // 2, y=height * 2 // 3, size=40, action="start")

    while True:
        screen.fill((255, 255, 255))

        # タイトル表示
        screen.blit(title_surface, title_surface.get_rect(center=(width // 2, height // 3)))

        # ボタン表示
        start_button.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                action = start_button.check_click(pos)
                if action == "start":
                    return  # ゲーム開始（mainループやGameManagerに制御を戻す）
