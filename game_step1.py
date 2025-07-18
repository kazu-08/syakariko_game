import pygame

def run_step1(screen, manager):
    screen.fill((200, 255, 200))
    font = pygame.font.SysFont(None, 48)
    text = font.render("Step 1", True, (0, 100, 0))
    screen.blit(text, (100, 150))
