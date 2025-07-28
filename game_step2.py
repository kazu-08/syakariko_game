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

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # 初期化
    manager.cup = Cup(x=300, y=10, screen_width=screen.get_width())

    if not hasattr(manager, "mouth"):
        # 画面上部にmouthを配置
        manager.mouth = Mouth(screen, x=screen_width // 2 - 50, y=50)

   
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
                    if manager.jagariko_list:
                        flavor = manager.jagariko_list.pop(0)
                        JagaClass = JAGA_CLASSES.get(flavor, Salad)

                        # 味からクラスを選択
                        if flavor == "srd":
                            JagaClass = Salad
                        elif flavor == "che":
                            JagaClass = Cheese
                        elif flavor == "jgb":
                            JagaClass = JagaButter
                        elif flavor == "trc":
                            JagaClass = Tarako

                        new_jaga = JagaClass(
                            x=manager.cup.rect.centerx,
                            y=manager.cup.rect.bottom,
                            speed=7,
                            point=10
                        )
                        manager.shots.append(new_jaga)
                    else:
                        print("発射できるじゃがりこがありません")

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

    # ✅ 発射も終了していたらゲーム終了
    if not manager.jagariko_list and not manager.shots:
        manager.state = "end"

    pygame.display.flip()
