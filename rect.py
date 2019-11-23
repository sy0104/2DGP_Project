from pico2d import *
import game_framework

# 플레이어 캐릭터
class Rect:
    def __init__(self):
        self.image_hp3 = load_image('Resource\\image\\player_hp3.png')
        self.image_hp2 = load_image('Resource\\image\\player_hp2.png')
        self.image_hp1 = load_image('Resource\\image\\player_hp1.png')
        self.image_protected = load_image('Resource\\image\\protected_player.png')
        self.x, self.y = 100, 300
        self.frame = 0
        self.time = 0
        self.hp = 3
        self.dir_x = 0
        self.dir_y = 0
        self.isCollide = False
        self.protecting = False
        self.protecting_time = 0

    def update(self):
        self.x += self.dir_x
        self.y += self.dir_y
        if self.x >= 1265 or self.x <= 15:
            self.dir_x = 0
        if self.y >= 685 or self.y <= 15:
            self.dir_y = 0

        if self.isCollide:
            self.protecting = True
            self.protecting_time += 0.01
            if self.protecting_time > 4.0:
                self.isCollide = False
                self.protecting = False
                self.protecting_time = 0.0

        pass

    # hp 작을수록 rect 크기 작아짐
    # protecting 중에는 rect 색 바꿈
    def draw(self):
        if self.hp == 3 and not self.protecting:
            self.image_hp3.clip_draw(0, 0, 30, 30, self.x, self.y)
        elif self.hp == 2 and not self.protecting:
            self.image_hp2.clip_draw(0, 0, 20, 20, self.x, self.y)
        elif self.hp == 1 and not self.protecting:
            self.image_hp1.clip_draw(0, 0, 15, 15, self.x, self.y)
        elif self.protecting:
            self.image_protected.clip_draw(0, 0, 15, 15, self.x, self.y)

    # 충돌체크
    def get_bb(self):
        if self.hp == 3:
            return self.x - 15, self.y - 15, self.x + 15, self.y + 15
        elif self.hp == 2:
            return self.x - 10, self.y - 10, self.x + 10, self.y + 10
        else:
            return self.x - 7.5, self.y - 7.5, self.x + 7.5, self.y + 7.5

