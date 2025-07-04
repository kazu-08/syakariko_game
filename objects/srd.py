from objects.jga import JGA

class SRD(JGA):  # サラダ味
    def update(self, screen_width: int = 640):
        self.y += self.speed
        self.rect.y = self.y