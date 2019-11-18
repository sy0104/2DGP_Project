from pico2d import *
import game_framework


# 플레이어 캐릭터
class Rect:
    def __init__(self):
        self.image = load_image('Resource\\image\\player.png')
        self.x, self.y = 100, 300
        self.frame = 0
        self.time = 0
        self.hp = 4
        self.dir_x = 0
        self.dir_y = 0

    def update(self):
        self.x += self.dir_x
        self.y += self.dir_y
        if self.x >= 1265 or self.x <= 15:
            self.dir_x = 0
        if self.y >= 685 or self.y <= 15:
            self.dir_y = 0
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 30, 30, self.x, self.y)

