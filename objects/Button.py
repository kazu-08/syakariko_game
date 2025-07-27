import pygame

class Button:
    def __init__(self, shape, x, y, size, action):
        self.shape = shape  # "left", "right", "circle"
        self.x = x
        self.y = y
        self.size = size
        self.action = action
        self.judge = False  # 選択状態

        self.rect = pygame.Rect(x - size, y - size, size * 2, size * 2)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        is_hover = self.rect.collidepoint(mouse_pos)

        # 色：マウスが上にあるかどうかで変更
        if is_hover:
            color = (255, 150, 150)  # 明るい赤
        else:
            color = (200, 100, 100)  # 通常色

        if self.shape == "circle":
            color = (150, 250, 250) if is_hover else (100, 200, 250)
            pygame.draw.circle(screen, color, (self.x, self.y), self.size)

        elif self.shape == "left":
            points = [
                (self.x - self.size, self.y),
                (self.x + self.size, self.y - self.size),
                (self.x + self.size, self.y + self.size)
            ]
            pygame.draw.polygon(screen, color, points)

        elif self.shape == "right":
            points = [
                (self.x + self.size, self.y),
                (self.x - self.size, self.y - self.size),
                (self.x - self.size, self.y + self.size)
            ]
            pygame.draw.polygon(screen, color, points)

    def check_click(self, pos):
        mx, my = pos

        if self.shape == "circle":
            dx = mx - self.x
            dy = my - self.y
            if dx * dx + dy * dy <= self.size * self.size:
                self.judge = True
                return self.action

        elif self.shape in ("left", "right"):
            if not self.rect.collidepoint(pos):
                return None

            if self.shape == "left":
                p1 = (self.x - self.size, self.y)
                p2 = (self.x + self.size, self.y - self.size)
                p3 = (self.x + self.size, self.y + self.size)
            else:
                p1 = (self.x + self.size, self.y)
                p2 = (self.x - self.size, self.y - self.size)
                p3 = (self.x - self.size, self.y + self.size)

            def sign(p1, p2, p3):
                return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

            b1 = sign(pos, p1, p2) < 0.0
            b2 = sign(pos, p2, p3) < 0.0
            b3 = sign(pos, p3, p1) < 0.0

            if (b1 == b2) and (b2 == b3):
                self.judge = True
                return self.action

        return None
