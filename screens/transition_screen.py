import pygame
from objects.Button import Button

def show_transition_screen(screen, width, height, message, jaga_counts):
    font_title = pygame.font.SysFont(None, 48)
    font_text = pygame.font.SysFont(None, 32)

    title_surface = font_title.render(message, True, (0, 0, 0))
    title_rect = title_surface.get_rect(center=(width // 2, height // 6))

    # スタートボタン
    start_button = Button("circle", x=width // 2, y=height * 5 // 6, size=40, action="continue")

    while True:
        screen.fill((255, 255, 255))
        screen.blit(title_surface, title_rect)

        # 味ごとのカウントを描画
        for i, (flavor, count) in enumerate(jaga_counts.items()):
            text = font_text.render(f"{flavor}: {count}本", True, (0, 0, 0))
            screen.blit(text, (width // 2 - 60, height // 3 + i * 40))

        start_button.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                result = start_button.check_click(pos)
                if result == "continue":
                    return
