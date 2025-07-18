import os
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("画像を遠くに見せる")

# 現在のディレクトリと画像ファイルのパス
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "Cup.png")

# 画像を読み込み → サイズ変更（例：元の半分に縮小）
original_img = pygame.image.load(image_path)
small_img = pygame.transform.scale(original_img, (int(original_img.get_width() * 0.1),
                                                  int(original_img.get_height() * 0.1)))

object_rect = small_img.get_rect()
object_rect.center = (400, 300)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # マウスに追従（テスト用）
    mouse_x, mouse_y = pygame.mouse.get_pos()
    object_rect.center = (mouse_x, mouse_y)

    screen.blit(small_img, object_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
