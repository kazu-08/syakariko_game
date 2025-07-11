import pygame

class Mouth:
    def __init__(self, x, y, width=50, height=50):
        self.x = x
        self.y = y
        #四角を描画する場合
        self.width = width
        self.height = height
        #画像の場合
        #self.image = pygame.image.load("Mouth.png")

    def draw(self, screen):
        #四角を描画する場合
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.width, self.height))
        #画像の場合
        #screen.blit(self.imag,(self.x, self.y))
    
    def is_in_mouth(self, Jaga):
        mouth_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Jaga_rect = pygame.Rect(Jaga.x, Jaga.y, Jaga.width, Jaga.height)
        return mouth_rect.colliderect(Jaga_rect)
        #口に入ったらTrue