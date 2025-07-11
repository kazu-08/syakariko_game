from objects.Jaga import Jaga

class JagaButter(Jaga):  # じゃがバター味
    def update(self, screen_width: int = 640):
        self.y += self.speed * 2
        self.rect.y = self.y