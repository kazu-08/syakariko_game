import pygame
from objects.Jaga import Jaga

class Salad(Jaga):  # サラダ味
    def __init__(self, x, y, color, speed, point):
        image = pygame.image.load("assets/images/jagabata.jpeg")
        image = pygame.transform.scale(image, (30,30))
        super().__init__(x, y, color, speed, point, image)
        
    def update(self, screen_width: int = 640):
        self.y += self.speed
        self.rect.y = self.y