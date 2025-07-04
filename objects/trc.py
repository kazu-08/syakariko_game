from objects.jga import JGA

class TRC(JGA):  # たらこ味
    def __init__(self, x, y, color, speed, point, image, reveal_y=200):
        super().__init__(x, y, color, speed, point, image)
        self.reveal_y = reveal_y

    def update(self, screen_width: int = 640):
        self.y += self.speed
        self.rect.y = self.y
        self.visible = self.y > self.reveal_y