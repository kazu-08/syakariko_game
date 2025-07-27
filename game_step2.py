import pygame
import random
from objects.cup import Cup
from objects.mouth import Mouth
from objects.JagaButter import JagaButter
from objects.Cheese import Cheese
from objects.Salad import Salad
from objects.Tarako import Tarako
from objects.Button import Button

JAGA_CLASSES = [JagaButter, Cheese, Salad, Tarako]

def run_step2(screen, manager):
    screen.fill((255, 255, 240))
    font = pygame.font.SysFont(None, 36)

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # 初期化
    if not hasattr(manager, "cup"):
        x = screen_width // 2
        y = 50  # 画面上部の適当なY座標
        manager.cup = Cup(x=x, y=y, screen_width=screen_width, screen_height=screen_height)
        manager.cup.flip_vertical()  # 上下反転

    if not hasattr(manager, "mouth"):
        mouth_height = 60
        manager.mouth = Mouth(screen, x=screen_width // 2 - 50, y=screen_height - mouth_height - 10)

    if not hasattr(manager, "buttons"):
        manager.buttons = [
            Button("left", 100, screen_height - 60, 25, action="mouth_left"),
            Button("right", 200, screen_height - 60, 25, action="mouth_right"),
            Button("circle", screen_width - 100, screen_height - 60, 30, action="shoot")
        ]

    if not hasattr(manager, "shots"):
        manager.shots = []

    if not hasattr(manager, "score"):
        manager.score = 0

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for btn in manager.buttons:
                result = btn.check_click(pos)
                if result == "mouth_left":
                    manager.mouth.move("left")
                elif result == "mouth_right":
                    manager.mouth.move("right")
                elif result == "shoot":
                    JagaClass = random.choice(JAGA_CLASSES)
                    new_jaga = JagaClass(
                        x=manager.cup.rect.centerx,
                        y=manager.cup.rect.bottom,
                        speed=7,
                        point=10
                    )
                    manager.shots.append(new_jaga)

    # --- ここでCupを自動で左右に移動させる ---
    manager.cup.update()

    # 発射物の更新と衝突判定
    updated_shots = []
    for jaga in manager.shots:
        jaga.y += jaga.speed
        if manager.mouth.is_in_mouth(jaga):
            manager.score += jaga.point
        elif jaga.y < screen_height:
            updated_shots.append(jaga)
    manager.shots = updated_shots

    # 描画
    manager.cup.draw(screen)
    manager.mouth.draw(screen)

    for shot in manager.shots:
        shot.draw(screen)

    for btn in manager.buttons:
        btn.draw(screen)

    score_txt = font.render(f"Score: {manager.score}", True, (0, 0, 0))
    screen.blit(score_txt, (10, 10))

    pygame.display.flip()
