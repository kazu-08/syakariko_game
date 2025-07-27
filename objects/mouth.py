import pygame

class Mouth:
    def __init__(self, screen, x=0, y=None, width=800):
        self.screen = screen
        self.width = width
        self.image = pygame.image.load("assets/images/mouth.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.image.get_height()))
        self.height = self.image.get_height()
        self.x = x

        # yが指定されていない場合は画面下に合わせる
        if y is None:
            self.y = screen.get_height() - self.height
        else:
            self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_in_mouth(self, Jaga):
        mouth_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        jaga_rect = pygame.Rect(Jaga.x, Jaga.y, Jaga.width, Jaga.height)
        return mouth_rect.colliderect(jaga_rect)
