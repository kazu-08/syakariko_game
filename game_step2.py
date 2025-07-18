import pygame

def run_step2(screen):
    font = pygame.font.SysFont(None, 60)
    text = font.render("Step 2 - 最終任務！キーを押して終了画面へ", True, (255, 255, 255))
    running = True

    while running:
        screen.fill((100, 50, 150))
        screen.blit(text, (50, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                running = False  # キーが押されたらエンド画面へ
