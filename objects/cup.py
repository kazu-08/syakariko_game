import pygame

class Cup:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 30
        self.color = (150, 150, 250)
        self.speed = 10

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        elif direction == "up":
            self.y -= self.speed
        elif direction == "down":
            self.y += self.speed
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        """当たり判定用の矩形を返す"""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision(self, jagariko):
        """じゃがりことの衝突判定"""
        return self.get_rect().colliderect(jagariko.get_rect())
