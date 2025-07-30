import unittest
import pygame
from objects.mouth import Mouth
from config import SCREEN_HEIGHT  # SCREEN_HEIGHT を使用するよう修正

class DummyJagariko:
    def __init__(self, x, y, width=10, height=30):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class TestMouth(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.mouth = Mouth(x=100)

    def test_draw_does_not_crash(self):
        # 描画がクラッシュしないか確認
        try:
            self.mouth.draw(self.screen)
        except Exception as e:
            self.fail(f"draw() failed: {e}")

    def test_mouth_position_bottom(self):
        # デフォルト位置が画面下であることを確認
        expected_y = SCREEN_HEIGHT - self.mouth.height - 10
        self.assertEqual(self.mouth.y, expected_y)

    def test_collision_true(self):
        # 衝突がある場合
        jaga = DummyJagariko(x=self.mouth.x + 5, y=self.mouth.y + 5)
        self.assertTrue(self.mouth.is_in_mouth(jaga))

    def test_collision_false(self):
        # 衝突がない場合
        jaga = DummyJagariko(x=self.mouth.x + 200, y=self.mouth.y + 200)
        self.assertFalse(self.mouth.is_in_mouth(jaga))

if __name__ == "__main__":
    unittest.main()
