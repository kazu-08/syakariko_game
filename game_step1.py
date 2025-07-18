import pygame

def run_step1(screen):
    font = pygame.font.SysFont(None, 60)
    text = font.render("Step 1 - 任務開始！キーを押して進む", True, (255, 255, 255))
    running = True

    while running:
        screen.fill((50, 100, 150))
        screen.blit(text, (50, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                running = False  # キーが押されたらStep2へ
