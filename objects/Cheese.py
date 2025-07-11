from objects.Jaga import Jaga

class Cheese(Jaga):  # チーズ味
    def __init__(self, x, y, color, speed, point, image):
        super().__init__(x, y, color, speed, point, image)
        self.dx = speed  # 横方向の速度
    def update(self, screen_width: int = 640):
        self.y += self.speed
        self.x += self.dx
        if self.x <= 0 or self.x + self.rect.width >= screen_width:
            self.dx *= -1  # 壁で反射
        self.rect.topleft = (self.x, self.y)