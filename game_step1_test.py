import pygame
import random
from objects.cup import Cup
from objects.JagaButter import JagaButter
from objects.Salad import JagaSalad
from objects.Tarako import JagaTarako
from objects.Cheese import JagaCheese

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def run_step1(screen, jagariko_list, cup):
    screen.fill((200, 255, 200))

    # じゃがりこを更新・描画
    for jaga in jagariko_list:
        jaga.fall()
        jaga.draw(screen)

    # cupを描画
    cup.draw(screen)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Step 1 Test")
    clock = pygame.time.Clock()

    # cupの作成
    cup = Cup(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 100)

    # じゃがりこを複数生成（例として4種類）
    jagariko_list = []
    for _ in range(10):
        x = random.randint(0, SCREEN_WIDTH - 30)
        y = random.randint(-600, -50)
        jaga_type = random.choice([JagaButter, JagaSalad, JagaTarako, JagaCheese])
        jagariko_list.append(jaga_type(x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        run_step1(screen, jagariko_list, cup)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
