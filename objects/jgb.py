from objects.jga import JGA

class JGB(JGA):  # じゃがバター味
    def update(self, screen_width: int = 640):
        self.y += self.speed * 2
        self.rect.y = self.y