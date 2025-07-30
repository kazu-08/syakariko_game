import pygame
from objects.Jaga import Jaga

class JagaButter(Jaga):  # じゃがバター味
    def __init__(self, x, y,  speed, point=None):
        image = pygame.image.load("assets/images/jagabata.jpeg")
        image = pygame.transform.scale(image, (10,50))
        point = 30 if point is None else point
        super().__init__(x, y,  speed, point, image)
        
    def update(self, screen_width: int = 640):
        self.y += self.speed * 2
        self.rect.topleft = (self.x, self.y)