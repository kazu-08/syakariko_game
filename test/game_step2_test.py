import pygame
import random
from objects.cup import Cup
from objects.mouth import Mouth
from objects.JagaButter import JagaButter
from objects.Cheese import Cheese
from objects.Salad import Salad
from objects.Tarako import Tarako
from objects.Button import Button

# 使用するじゃがりこクラス
JAGA_CLASSES = [JagaButter, Cheese, Salad, Tarako]
JAGA_NAMES = {
    "JagaButter": "JagaButter",
    "Cheese": "Cheese",
    "Salad": "Salad",
    "Tarako": "Tarako"
}

def run_step2(screen, manager):
    screen.fill((255, 255, 240))
    font = pygame.font.SysFont(None, 36)

    # 初期化
    if not hasattr(manager, "cup"):
        manager.cup = Cup(x=100, y=500, screen_width=screen.get_width())

    if not hasattr(manager, "mouth"):
        manager.mouth = Mouth(x=300, y=100)

    if not hasattr(manager, "buttons"):
        manager.buttons = [
            Button("←", 100, 550, 30, action="mouth_left"),
            Button("→", 200, 550, 30, action="mouth_right"),
            Button("発射", 500, 550, 40, action="shoot")
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
                    # 発射: カップの位置から1本生成して上に向かって発射
                    JagaClass = random.choice(JAGA_CLASSES)
                    new_jaga = JagaClass(x=manager.cup.x + manager.cup.width // 2, y=manager.cup.y, speed=-7, point=10)
                    manager.shots.append(new_jaga)

    # じゃがりこ発射物の更新と判定
    updated_shots = []
    for jaga in manager.shots:
        jaga.y += jaga.speed
        if manager.mouth.is_in_mouth(jaga):
            manager.score += jaga.point
        elif jaga.y > 0:
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
