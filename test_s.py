import pygame
from objects.Salad import Salad

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Salad Test")
clock = pygame.time.Clock()

# Saladインスタンス作成
salad = Salad(x=185, y=0, color=0, speed=3, point=10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    salad.update()
    screen.fill((255, 255, 255))  # 背景白
    salad.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
