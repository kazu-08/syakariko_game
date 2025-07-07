#左に移動、右に移動、発射の３種類を想定したもの。追加するなり削るなりご自由に。

import pygame

class Button:
    def __init__(self, shape, x, y, size, action):
        self.shape = shape  # "left", "right", "circle"
        self.x = x
        self.y = y
        self.size = size
        self.action = action
        self.judge = False  # 選択状態。今は使っていないが見た目変更などに使えるそうです。

        # 図形用当たり判定用の矩形（簡易）。おおまかなクリック判定が可能。
        self.rect = pygame.Rect(x - size, y - size, size * 2, size * 2)

    def draw(self, screen):
        if self.shape == "circle":
            pygame.draw.circle(screen, (100, 200, 250), (self.x, self.y), self.size)
        elif self.shape == "left":
            points = [
                (self.x - self.size, self.y),
                (self.x + self.size, self.y - self.size),
                (self.x + self.size, self.y + self.size)
            ]
            pygame.draw.polygon(screen, (200, 100, 100), points)
        elif self.shape == "right":
            points = [
                (self.x + self.size, self.y),
                (self.x - self.size, self.y - self.size),
                (self.x - self.size, self.y + self.size)
            ]
            pygame.draw.polygon(screen, (200, 100, 100), points)

    def check_click(self, pos): #pos: マウスのクリック座標
        if self.rect.collidepoint(pos): #マウスの座標がボタン内だったらTrue
            self.judge = True
            return self.action
        return None
