import pygame
from abc import ABC, abstractmethod #抽象基底クラス

class Jaga(ABC):
    def __init__(self, x: int, y: int, color: int, speed: int, point: int, image: pygame.Surface):
        self.x = x #x軸
        self.y = y #y軸
        self.color = color #色
        self.speed = speed #スピード
        self.point = point #得点数
        self.collect = 0  #カップに収集されたか
        self.eat = 0      #口に届いたか
        self.image = image #見た目
        self.rect = image.get_rect(topleft=(x, y)) #画像の位置情報
        self.visible = True #trcに使用(trueなら描写)

    @abstractmethod
    def update(self, screen_width: int = 640): #動き
        pass

    def draw(self, screen): #画像を表示
        if self.visible:
            screen.blit(self.image, (self.x, self.y))

    def is_off_screen(self, height): #画面外かどうか(trueなら画面外)
        return self.y > height