import pygame
import sys
import os

# 初期化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("画像を左右に動かす")

# 現在のディレクトリと画像ファイルのパス
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "Cup.png")

# 画像を読み込む（同じフォルダに 'object.png' を置いてね）
object_img = pygame.image.load(image_path)
small_img = pygame.transform.scale(original_img, (int(original_img.get_width() * 0.1),
                                                  int(original_img.get_height() * 0.1)))

object_rect = small_img.get_rect()
object_rect.center = (400, 300)  # 初期位置

# メインループ
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((255, 255, 255))  # 背景を白に

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キーの状態を取得 ここはテストできてないからごめんね
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        object_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        object_rect.x += 5

    # 画像を描画
    screen.blit(object_img, object_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
