import pygame
import random
from objects.cup import Cup
from objects.JagaButter import JagaButter
from objects.Cheese import Cheese
from objects.Salad import Salad
from objects.Tarako import Tarako
from objects.Button import Button

# 各じゃがりこクラスをリスト化（ランダム生成用）
JAGA_CLASSES = [JagaButter, Cheese, Salad, Tarako]

def run_step1(screen, manager):
    screen.fill((200, 255, 200))

    # タイトル表示
    font = pygame.font.SysFont(None, 48)
    text = font.render("Step 1", True, (0, 100, 0))
    screen.blit(text, (100, 150))

    # 初回のみcupとじゃがりこを生成
    if not hasattr(manager, "cup"):
        manager.cup = Cup(x=300, y=500)

    if not manager.jagariko_list:
        for _ in range(10):  # 10本生成（種類はランダム）
            JagaClass = random.choice(JAGA_CLASSES)
            jagariko = JagaClass(x=random.randint(50, 550), y=0, speed=3, point=10)
            manager.jagariko_list.append(jagariko)

    # 各じゃがりこを落下・描画
    for jaga in manager.jagariko_list:
        jaga.fall()
        jaga.draw(screen)

    # カップを描画
    manager.cup.draw(screen)

    pygame.display.flip()
