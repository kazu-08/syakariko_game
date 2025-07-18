import pygame

class Cup:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 30
        self.color = (150, 150, 250)
        self.point = 0      # 得点
        self.collect = 0    # 収集したじゃがりこ数

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed
        # 上下は使わない仕様なので省略

    def draw(self, screen):
        top_width = self.width
        bottom_width = self.width * 0.67  # 底辺は上辺の半分
        half_top = top_width / 2
        half_bottom = bottom_width / 2

        top_center_x = self.x + self.width / 2
        top_y = self.y
        bottom_y = self.y + self.height

        points = [
            (top_center_x - half_top, top_y),         # 左上
            (top_center_x + half_top, top_y),         # 右上
            (top_center_x + half_bottom, bottom_y),   # 右下
            (top_center_x - half_bottom, bottom_y)    # 左下
        ]

        pygame.draw.polygon(screen, self.color, points)

    def get_top_rect(self):
        """カップの上辺部分のみの当たり判定矩形を返す"""
        top_width = self.width
        top_height = 10  # 上辺の高さだけを判定用に狭くする
        top_center_x = self.x + self.width / 2
        top_y = self.y

        return pygame.Rect(top_center_x - top_width / 2, top_y, top_width, top_height)

    def checkCollect(self, jga):
        """じゃがりこがカップの上辺に触れたか判定し加点"""
        if self.get_top_rect().colliderect(jga.get_rect()):
            self.collect += 1
            self.point += 10  # 例えば10点加算
            return True
        return False
