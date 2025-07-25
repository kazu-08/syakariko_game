import pygame
from objects.mouth import Mouth
from objects.Button import Button
from config import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouth Move Test")
clock = pygame.time.Clock()

# Mouth インスタンス（画像で表示）
mouth = Mouth(x=SCREEN_WIDTH // 2 - 25, y=SCREEN_HEIGHT - 60, width=50, height=50)

# Button インスタンス（左右移動用）
buttons = [
    Button("left", 100, SCREEN_HEIGHT - 30, 30, "left"),
    Button("right", 200, SCREEN_HEIGHT - 30, 30, "right"),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for btn in buttons:
                action = btn.check_click(pos)
                if action == "left":
                    mouth.move("left")
                elif action == "right":
                    mouth.move("right")

    screen.fill((255, 255, 255))  # 背景白
    mouth.draw(screen)

    for btn in buttons:
        btn.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
