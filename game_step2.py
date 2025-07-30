import pygame
import random
from objects.cup import Cup
from objects.mouth import Mouth
from objects.JagaButter import JagaButter
from objects.Cheese import Cheese
from objects.Salad import Salad
from objects.Tarako import Tarako
from objects.Button import Button

JAGA_CLASSES = {
    'srd': Salad,
    'che': Cheese,
    'jgb': JagaButter,
    'trc': Tarako
}

def run_step2(screen, manager):
    screen.fill((255, 255, 240))
    font = pygame.font.SysFont(None, 36)

    # 初期化
    if not hasattr(manager, "cup"):
        manager.cup = Cup(x=400, y=50, screen_width=screen.get_width())  # ✅ 先に作って
    
    # ステップ2でのみ反転（ただし1回だけ）
    if not hasattr(manager, "cup_flipped_for_step2"):
        manager.cup.flip_vertical()
        manager.cup_flipped_for_step2 = True

    if not hasattr(manager, "mouth"):
         manager.mouth = Mouth(screen, x=0, y=450)

 
    manager.buttons = [
        Button("circle", 400, 100, 40, action="shoot")  # ← 例：上の方・中央に配置
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
                    JagaClass = random.choice(list(JAGA_CLASSES.values()))
                    new_jaga = JagaClass(
                        x=manager.cup.rect.centerx,
                        y=manager.cup.rect.bottom,
                        speed=-7,
                        point=10
                    )
                    manager.shots.append(new_jaga)

    # ✅ Cupを自動で左右に動かす！
    manager.cup.update()

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
