import pygame
from objects.Jaga import Jaga
from screens.config import init_screen, SCREEN_WIDTH, SCREEN_HEIGHT

class Cheese(Jaga):  # チーズ味
    def __init__(self, x, y, color, speed, point):
        image = pygame.image.load("assets/images/jagabata.jpeg")
        image = pygame.transform.scale(image, (30,30))
        super().__init__(x, y, color, speed, point, image)
        self.dx = speed  # 横方向の速度

    def update(self):
        self.y += self.speed
        self.x += self.dx
        if self.x <= 0 or self.x + self.rect.width >= SCREEN_WIDTH:
            self.dx *= -1  # 壁で反射
        self.rect.topleft = (self.x, self.y)

