import pygame
import os


class Cup:
    def __init__(self, x=400, y=500, screen_width=800, screen_height=600):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # カップ画像の読み込みと縮小
        current_dir = os.path.dirname(__file__)
        image_path = os.path.normpath(os.path.join(current_dir, "../assets/images/Cup.png"))
        original_img = pygame.image.load(image_path)
        self.image = pygame.transform.scale(original_img, (int(original_img.get_width() * 0.05),
                                                       int(original_img.get_height() * 0.05)))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

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

# テスト実行時のみ
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cup Test with Buttons")
    clock = pygame.time.Clock()

    cup = Cup()

    running = True
    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

     


        # カップ描画
        cup.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
