import pygame
import random
from objects.cup import Cup
from objects.JagaButter import JagaButter
from objects.Cheese import Cheese
from objects.Salad import Salad
from objects.Tarako import Tarako
from objects.Button import Button

# 各じゃがりこクラス（種類ごとに名前を定義）
JAGA_CLASSES = [JagaButter, Cheese, Salad, Tarako]
JAGA_NAMES = {
    "JagaButter": "JagaButter",
    "Cheese": "Cheese",
    "Salad": "Salad",
    "Tarako": "Tarako"
}

def run_step1(screen, manager):
    screen.fill((200, 255, 200))
    font = pygame.font.SysFont(None, 36)

    # 初回のみcup・じゃがりこ・ボタン・カウント生成
    if not hasattr(manager, "cup"):
        manager.cup = Cup(x=300, y=500, screen_width=screen.get_width())

    if not hasattr(manager, "buttons"):
        manager.buttons = [
            Button("left", 100, 550, 30, action="left"),
            Button("right", 200, 550, 30, action="right"),
        ]

    if not hasattr(manager, "jagariko_list"):
        manager.jagariko_list = []

    if not hasattr(manager, "caught_counts"):
        manager.caught_counts = {name: 0 for name in JAGA_NAMES.keys()}

    if len(manager.jagariko_list) < 1:
        # 新しいじゃがりこを追加（1本ずつ）
        JagaClass = random.choice(JAGA_CLASSES)
        jagariko = JagaClass(x=random.randint(50, 550), y=0, speed=3, point=10)
        manager.jagariko_list.append(jagariko)

    # 入力処理（マウス）
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for btn in manager.buttons:
                result = btn.check_click(pos)
                if result == "left":
                    manager.cup.move_left()
                elif result == "right":
                    manager.cup.move_right()

    # 各じゃがりこを落下・描画・衝突判定
    updated_list = []
    for jaga in manager.jagariko_list:
        jaga.update()
        if jaga.rect.colliderect(manager.cup.rect):
            class_name = jaga.__class__.__name__
            manager.caught_counts[class_name] += 1
        elif jaga.rect.top < screen.get_height():
            updated_list.append(jaga)
        # 落ち切ったら消えるが、拾われたものはカウントされている
    manager.jagariko_list = updated_list

    for jaga in manager.jagariko_list:
        jaga.draw(screen)

    # カップ描画
    manager.cup.draw(screen)

    # ボタン描画
    for btn in manager.buttons:
        btn.draw(screen)

    # 捕獲数を表示
    y_offset = 10
    total = 0
    for class_name, count in manager.caught_counts.items():
        flavor_name = JAGA_NAMES[class_name]
        txt = font.render(f"{flavor_name}: {count}", True, (0, 0, 0))
        screen.blit(txt, (10, y_offset))
        y_offset += 30
        total += count

    total_txt = font.render(f"total: {total}", True, (0, 0, 0))
    screen.blit(total_txt, (10, y_offset))

    pygame.display.flip()
