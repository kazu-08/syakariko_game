import pygame
from objects.Jaga import Jaga
from config import SCREEN_WIDTH

class Tarako(Jaga):  # たらこ味
    def __init__(self, x, y,  speed, point, reveal_y=200):
        image = pygame.image.load("assets/images/tarako.jpeg")
        image = pygame.transform.scale(image, (10, 50))
        super().__init__(x, y,  speed, point, image)
        self.reveal_y = reveal_y
        self.visible = False 

    def update(self, screen_width: int = SCREEN_WIDTH):
        self.y += self.speed *2
        self.rect.y = self.y
        self.visible = self.y > self.reveal_y