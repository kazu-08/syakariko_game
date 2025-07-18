import pygame
from objects.Cheese import Cheese
from config import init_screen, SCREEN_WIDTH, SCREEN_HEIGHT


pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Cheese Test")
clock = pygame.time.Clock()

# Cheeseインスタンス作成（imageは渡さない）
cheese = Cheese(x=185, y=0, color=0, speed=3, point=10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cheese.update()
    screen.fill((255, 255, 255))  # 背景白
    cheese.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
