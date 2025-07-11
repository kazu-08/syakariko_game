import pygame
import sys
from game_manager import GameManager

def main():
    pygame.init()

    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("しゃかりこゲーム")

    clock = pygame.time.Clock()
    fps = 60

    manager = GameManager(screen, screen_width, screen_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.handle_event(event)

        manager.update()

        screen.fill((255, 255, 255))
        manager.draw()

        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
