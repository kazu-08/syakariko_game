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
        y = screen_height - 100  # 画面下部にCupを配置
        manager.cup = Cup(x=x, y=y, screen_width=screen_width, screen_height=screen_height)

    if not hasattr(manager, "mouth"):
        # 画面上部にmouthを配置
        manager.mouth = Mouth(screen, x=screen_width // 2 - 50, y=50)

    if not hasattr(manager, "buttons"):
        # 丸いボタンだけにする
        manager.buttons = [
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
                if result == "shoot":
                    # cupの中央上から上向きに発射
                    JagaClass = random.choice(JAGA_CLASSES)
                    new_jaga = JagaClass(
                        x=manager.cup.rect.centerx,
                        y=manager.cup.rect.top,
                        speed=-7,  # 上向きに飛ばす
                        point=10
                    )
                    manager.shots.append(new_jaga)

    # cupの左右自動移動（あれば）
    if hasattr(manager, "cup"):
        manager.cup.update()

    # 発射物の更新とmouthとの衝突判定
    updated_shots = []
    for jaga in manager.shots:
        jaga.y += jaga.speed  # 上に移動
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

    # スコア表示
    score_txt = font.render(f"Score: {manager.score}", True, (0, 0, 0))
    screen.blit(score_txt, (10, 10))

    pygame.display.flip()
