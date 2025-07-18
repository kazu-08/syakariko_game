# screens/start_screen.py
import pygame
import sys
from screens.config import init_screen, SCREEN_WIDTH, SCREEN_HEIGHT


def show_start_screen(screen, width, height):
    font_title = pygame.font.SysFont(None, 72)
    font_start = pygame.font.SysFont(None, 36)

    title_surface = font_title.render("しゃかりこゲーム", True, (0, 0, 0))
    start_surface = font_start.render("スペースキーでスタート", True, (50, 50, 50))

    while True:
        screen.fill((255, 255, 255))

        screen.blit(title_surface, title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)))
        screen.blit(start_surface, start_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return  # スタート
