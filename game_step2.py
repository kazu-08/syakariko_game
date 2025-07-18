import pygame

def run_step2(screen, manager):
    screen.fill((200, 200, 255))
    font = pygame.font.SysFont(None, 48)
    text = font.render("Step 2: 食べる時間！", True, (0, 0, 100))
    screen.blit(text, (100, 150))
