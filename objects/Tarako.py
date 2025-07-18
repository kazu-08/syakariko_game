from objects.Jaga import Jaga

class Tarako(Jaga):  # たらこ味
    def __init__(self, x, y, color, speed, point, image, reveal_y=200):
        image = pygame.image.load("assets/images/tarako.jpeg")
        image = pygame.transform.scale(image, (30, 30))
        super().__init__(x, y, color, speed, point, image)
        self.reveal_y = reveal_y
        self.visible = False 

    def update(self, screen_width: int = SCREEN_WIDTH):
        self.y += self.speed
        self.rect.y = self.y
        self.visible = self.y > self.reveal_y