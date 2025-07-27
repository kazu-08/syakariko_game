import pygame
from game_step1 import run_step1

class DummyManager:
    def __init__(self):
        self.jagariko_list = []

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 600))
    pygame.display.set_caption("Step1 Test")
    clock = pygame.time.Clock()

    manager = DummyManager()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        run_step1(screen, manager)
        clock.tick(60)  # 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
