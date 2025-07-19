import pygame
from objects.JagaButter import JagaButter

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Jagabutter Test")
clock = pygame.time.Clock()

# JagaButterインスタンス作成（imageは内部で読み込まれる）
jaga_butter = JagaButter(x=185, y=0, color=0, speed=3, point=10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    jaga_butter.update()
    screen.fill((255, 255, 255))
    jaga_butter.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
