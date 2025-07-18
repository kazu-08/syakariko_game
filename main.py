import pygame
from Game_Manager import GameManager
from screens.config import init_screen, SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = init_screen()
    pygame.display.set_caption("じゃがりこゲーム")

    clock = pygame.time.Clock()
    manager = GameManager(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.handle_event(event)  # ← 正しい位置

        manager.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
