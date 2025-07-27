import pygame
import os
from .Button import Button

class Cup:
    def __init__(self, screen_width=800, screen_height=600):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # カップ画像の読み込み
        current_dir = os.path.dirname(__file__)
        image_path = os.path.normpath(os.path.join(current_dir, "../assets/images/Cup.png"))
        original_img = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(original_img, (int(original_img.get_width() * 0.1),
                                                           int(original_img.get_height() * 0.1)))

        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 100)

    def move_left(self):
        self.rect.x -= 10
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.x += 10
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width

    def shoot(self):
        print("発射！（仮の処理）")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# テスト実行時のみ
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cup Test with Buttons")
    clock = pygame.time.Clock()

    cup = Cup()

    # ボタン作成
    left_button = Button("left", 100, 550, 30, action="left")
    right_button = Button("right", 200, 550, 30, action="right")
    fire_button = Button("circle", 700, 550, 30, action="fire")
    buttons = [left_button, right_button, fire_button]

    running = True
    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in buttons:
                    result = btn.check_click(pos)
                    if result == "left":
                        cup.move_left()
                    elif result == "right":
                        cup.move_right()
                    elif result == "fire":
                        cup.shoot()

        # ボタン描画
        for btn in buttons:
            btn.draw(screen)

        # カップ描画
        cup.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
