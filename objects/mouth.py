import pygame
from config import SCREEN_WIDTH

class Mouth:
    def __init__(self, x, y, width=50, height=50):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load("assets/images/mouth.jpeg")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        #四角を描画する場合
        #pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.width, self.height))
        #画像の場合
        screen.blit(self.image,(self.x, self.y))

    def move(self, direction, step=10):
        if direction == "left":
            self.x = max(0, self.x - step)
        elif direction == "right":
            self.x = min(SCREEN_WIDTH - self.width, self.x + step)
    
    def is_in_mouth(self, Jaga):
        mouth_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Jaga_rect = pygame.Rect(Jaga.x, Jaga.y, Jaga.width, Jaga.height)
        return mouth_rect.colliderect(Jaga_rect)
        #口に入ったらTrue
        