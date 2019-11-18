from pico2d import *
import game_framework

# 플레이어 캐릭터
class Rect:
    def __init__(self):
        self.image_hp2 = load_image('Resource\\image\\player_hp2.png')
        self.image_hp1 = load_image('Resource\\image\\player_hp1.png')
        self.x, self.y = 100, 300
        self.frame = 0
        self.time = 0
        self.hp = 2
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
        if self.hp == 2:
            self.image_hp2.clip_draw(0, 0, 30, 30, self.x, self.y)
        else:
            self.image_hp1.clip_draw(0, 0, 15, 15, self.x, self.y)

    def get_bb(self):
        if self.hp == 2:
            return self.x - 15, self.y - 15, self.x + 15, self.y + 15
        else:
            return self.x - 7.5, self.y - 7.5, self.x + 7.5, self.y + 7.5

