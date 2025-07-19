import pygame
from objects.Mouth import Mouth

class DummyJaga:
    def __init__(self, x, y, width=20, height=20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Mouth Test")

mouth = Mouth(100, 100)
jaga = DummyJaga(110, 110)  # 口の中にいる想定

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # 白背景
    mouth.draw(screen)

    # Jagaの表示（青い矩形）
    pygame.draw.rect(screen, (0, 0, 255), (jaga.x, jaga.y, jaga.width, jaga.height))

    # 衝突しているかをコンソールに出力
    if mouth.is_in_mouth(jaga):
        print("Jaga is in mouth!")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
