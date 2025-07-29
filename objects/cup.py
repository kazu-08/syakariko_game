import pygame
import os

class Cup:
    def __init__(self, x=400, y=100, screen_width=800, screen_height=600):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.direction = 1  # 右に動く（-1で左）
        self.speed = 3      # Cupの移動速度

        # カップ画像の読み込みと縮小
        current_dir = os.path.dirname(__file__)
        image_path = os.path.normpath(os.path.join(current_dir, "../assets/images/Cup.png"))
        original_img = pygame.image.load(image_path)
        self.image = pygame.transform.scale(
            original_img,
            (int(original_img.get_width() * 0.05), int(original_img.get_height() * 0.05))
        )

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y

    def update(self):
        self.rect.x += self.speed * self.direction

        # 画面端に達したら反転
        if self.rect.right >= self.screen_width:
            self.rect.right = self.screen_width
            self.direction *= -1
        elif self.rect.left <= 0:
            self.rect.left = 0
            self.direction *= -1

    def move_left(self):
        self.rect.x -= 20
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += 20
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

    def shoot(self):
        print("発射！（仮の処理）")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def flip_vertical(self):
        print("updown")  # デバッグ表示

        # 画像を上下反転
        self.image = pygame.transform.flip(self.image, False, True)

        # 反転後、位置を明示的に更新
        old_centerx = self.rect.centerx
        self.rect = self.image.get_rect()
        self.rect.centerx = old_centerx

        # ✅ カップを画面上部に固定（必要に応じて微調整）
        self.rect.top = 50


# テスト実行時のみ動作確認
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cup Test with Movement")
    clock = pygame.time.Clock()

    cup = Cup()
    cup.flip_vertical()  # ← 上下反転テスト（必要なら）

    running = True
    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        cup.update()        # ← ここが必要（Cupを自動で動かす）
        cup.draw(screen)    # 描画

        pygame.display.flip()
        clock.tick(60)      # 60FPS

    pygame.quit()
