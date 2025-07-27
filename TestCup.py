import os
import pygame
from objects.cup import Cup
from objects.Button import Button
import sys


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("画像を遠くに見せる")
clock = pygame.time.Clock()  # ← これが必要！


cup = Cup()

# Button のインスタンス
left_button = Button("left", 100, 550, 30, action="left")
right_button = Button("right", 200, 550, 30, action="right")
buttons = [left_button, right_button]

running = True
while running:
    screen.fill((255, 255, 255))  # 背景白

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                action = button.check_click(pos)
                if action == "left":
                    cup.move_left()
                elif action == "right":
                    cup.move_right()

    # ボタンの描画
    for button in buttons:
        button.draw(screen)

    # カップの描画
    cup.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
