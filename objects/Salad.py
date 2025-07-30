import pygame
from objects.Jaga import Jaga

class Salad(Jaga):  # サラダ味
    def __init__(self, x, y,  speed, point=None):
        image = pygame.image.load("assets/images/salad.jpeg")
        image = pygame.transform.scale(image, (10,50))
        point = 10 if point is None else point
        super().__init__(x, y,  speed, point, image)
        
    def update(self, screen_width: int = 640):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)