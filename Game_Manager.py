import pygame
from screen.start import draw_start_screen, handle_start_event
from screen.end import draw_end_screen, handle_end_event
from game.play import GamePlay  # ゲーム本体処理

class GameManager:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.state = "start"  # start, playing, end
        self.game = None

    def handle_event(self, event):
        if self.state == "start":
            if handle_start_event(event):
                self.start_game()
        elif self.state == "playing":
            self.game.handle_event(event)
        elif self.state == "end":
            if handle_end_event(event):
                self.restart_game()

    def update(self):
        if self.state == "playing":
            self.game.update()
            if self.game.is_game_over():
                self.state = "end"

    def draw(self):
        if self.state == "start":
            draw_start_screen(self.screen, self.width, self.height)
        elif self.state == "playing":
            self.game.draw()
        elif self.state == "end":
            draw_end_screen(self.screen, self.width, self.height)

    def start_game(self):
        self.game = GamePlay(self.screen, self.width, self.height)
        self.state = "playing"

    def restart_game(self):
        self.state = "start"
        self.game = None
