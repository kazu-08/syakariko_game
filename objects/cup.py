# cup.py
import pygame
import os

class Cup:
    def __init__(self, x=400, y=300):
        current_dir = os.path.dirname(__file__)
        image_path = os.path.normpath(os.path.join(current_dir, "../assets/images/Cup.png"))

        # 画像読み込みと縮小（10%）
        original_img = pygame.image.load(image_path)
        self.image = pygame.transform.scale(
            original_img,
            (int(original_img.get_width() * 0.1), int(original_img.get_height() * 0.1))
        )

        # 表示位置を設定
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move_left(self, speed=5):
        self.rect.x -= speed

    def move_right(self, speed=5):
        self.rect.x += speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
