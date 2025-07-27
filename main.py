import pygame
from Game_Manager import GameManager
from config import init_screen, SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = init_screen()
    pygame.display.set_caption("syakariko-game")

    clock = pygame.time.Clock()
    manager = GameManager(screen)
    
    # 日本語フォントを指定（1回だけでOK）
    font = pygame.font.Font("C:/Windows/Fonts/msgothic.ttc", 36)
    text = font.render("じゃがりこゲーム", True, (0, 0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.handle_event(event)  # ← 正しい位置

        screen.fill((255, 255, 255))
        manager.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
