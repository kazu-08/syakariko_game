import pygame

class Mouth:
    def __init__(self, screen, x=0, y=None, width=800):
        self.screen = screen
        self.width = width
        self.image = pygame.image.load("assets/images/kuti.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.image.get_height()))
        self.height = self.image.get_height()
        self.x = x

        # 👇 実際の当たり判定範囲を口の部分だけに限定（調整してください）
        self.hitbox = pygame.Rect(300,300,300,100)  # x, y, width, height は目視で調整

        # yが指定されていない場合は画面下に合わせる
        if y is None:
            self.y = screen.get_height() - self.height
        else:
            self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

        # ⬇️ 当たり判定の範囲を赤枠で描画（デバッグ用）
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


    def is_in_mouth(self, Jaga):
        return self.hitbox.colliderect(Jaga.rect)
