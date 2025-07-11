# main.py
import pygame
import sys
from game_manager import GameManager

def main():
    pygame.init()
    
    # ウィンドウサイズとタイトル
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("しゃかりこゲーム")

    # フレームレート制御
    clock = pygame.time.Clock()
    fps = 60

    # ゲームマネージャの初期化
    manager = GameManager(screen, screen_width, screen_height)

    # メインループ
    running = True
    while running:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.handle_event(event)

        # ロジック更新
        manager.update()

        # 画面描画
        screen.fill((255, 255, 255))  # 背景色：白
        manager.draw()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
