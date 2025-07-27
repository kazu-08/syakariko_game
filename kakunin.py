import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Font Test")

# フォント設定
font = pygame.font.Font("C:/Windows/Fonts/msgothic.ttc", 36)
text = font.render("siゃがりこゲーム", True, (0, 0, 0))

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    screen.blit(text, (50, 50))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
