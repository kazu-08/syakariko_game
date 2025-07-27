import pygame
from objects.Button import Button

def show_start_screen(screen, manager, height):
    screen.fill((255, 255, 255))

    font_title = pygame.font.Font("C:/Windows/Fonts/msgothic.ttc", 72)
    font_start = pygame.font.Font("C:/Windows/Fonts/msgothic.ttc", 36)

    title_surface = font_title.render("じゃがりこゲーム", True, (0, 0, 0))
    start_surface = font_start.render("スペースキーでスタート", True, (50, 50, 50))

    screen.blit(title_surface, title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)))
    screen.blit(start_surface, start_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3)))


"""
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
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return  # スタート
