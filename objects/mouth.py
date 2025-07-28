import pygame

class Mouth:
    def __init__(self, screen, x=0, y=None, width=800):
        self.screen = screen
        self.width = width
        self.image = pygame.image.load("assets/images/kuti.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.image.get_height()))
        self.height = self.image.get_height()
        self.x = x

       
        # yが指定されていない場合は画面下に合わせる
        if y is None:
            self.y = screen.get_height() - self.height
        else:
            self.y = y

        # 👇 画像の位置・サイズをもとに当たり判定を自動で設定（例：画像中央下）
        hitbox_width = 400
        hitbox_height = int(self.height * 0.2)
        hitbox_x = self.x+300
        hitbox_y = self.y + 50

        self.hitbox = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

        # ⬇️ 当たり判定の範囲を赤枠で描画（デバッグ用）
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


    def is_in_mouth(self, Jaga):
        return self.hitbox.colliderect(Jaga.rect)
