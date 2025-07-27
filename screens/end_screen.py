# screens/end_screen.py
import pygame
import sys
from config import init_screen, SCREEN_WIDTH, SCREEN_HEIGHT


def show_end_screen(screen, width, height, score):
    font_title = pygame.font.SysFont(None, 64)
    font_score = pygame.font.SysFont(None, 48)
    font_restart = pygame.font.SysFont(None, 32)

    title_surface = font_title.render("gameover", True, (0, 0, 0))
    score_surface = font_score.render(f"score: {score}", True, (0, 0, 128))
    restart_surface = font_restart.render("space or Esc", True, (100, 100, 100))

    while True:
        screen.fill((255, 255, 255))

        screen.blit(title_surface, title_surface.get_rect(center=(width // 2, height // 3)))
        screen.blit(score_surface, score_surface.get_rect(center=(width // 2, height // 2)))
        screen.blit(restart_surface, restart_surface.get_rect(center=(width // 2, height * 2 // 3)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    return  # 再スタート
