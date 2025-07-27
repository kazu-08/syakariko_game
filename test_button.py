import pygame
from objects.Button import Button

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Button Test")
clock = pygame.time.Clock()

# テスト用のボタンを3つ作成
button_circle = Button("circle", 200, 80, 30, "shoot")
button_left   = Button("left",   100, 200, 30, "move_left")
button_right  = Button("right",  300, 200, 30, "move_right")

buttons = [button_circle, button_left, button_right]

running = True
while running:
    screen.fill((255, 255, 255))

    # ボタン描画
    for btn in buttons:
        btn.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for btn in buttons:
                result = btn.check_click(event.pos)
                if result:
                    print(f"Button clicked: {result}")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
