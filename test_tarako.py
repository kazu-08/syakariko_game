import pygame
from objects.Tarako import Tarako
from config import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tarako Test")
clock = pygame.time.Clock()

# Tarakoインスタンスを作成（画像はTarako内で読み込む）
tarako = Tarako(x=185, y=0, color=0, speed=3, point=10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tarako.update()  # yが200を超えるとvisible=True
    screen.fill((255, 255, 255))  # 背景白

    if hasattr(tarako, "visible") and tarako.visible:
        tarako.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
