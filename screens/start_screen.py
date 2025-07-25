import pygame
from objects.Button import Button

def show_start_screen(screen, width, height):
    font_title = pygame.font.SysFont(None, 72)

    title_surface = font_title.render("syakariko-game", True, (0, 0, 0))
    start_button = Button(shape="circle", x=width // 2, y=height * 2 // 3, size=40, action="start")

    while True:
        screen.fill((255, 255, 255))
        screen.blit(title_surface, title_surface.get_rect(center=(width // 2, height // 3)))
        start_button.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                result = start_button.check_click(pos)
                if result == "start":
                    return "start"  # ← ここが重要
