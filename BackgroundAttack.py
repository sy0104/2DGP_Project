from pico2d import *

# stage2 - 위아래 공격
# 위
class BeatAttack_UP:
    def __init__(self):
        self.image = load_image('Resource\\image\\attack_beat_up.png')
        self.x, self.y = 640, 600
        self.frame = 0
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer % 50 == 0:
            self.frame = (self.frame + 1) % 2

    def draw(self):
        self.image.clip_draw(0, self.frame * 250, 1280, 250, 640, 600)

    def get_bb(self):
        return self.x - 640, self.y - 90, self.x + 640, self.y + 90


# 아래
class BeatAttack_Down:
    def __init__(self):
        self.image = load_image('Resource\\image\\attack_beat_down.png')
        self.x, self.y = 640, 100
        self.frame = 0
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer % 50 == 0:
            self.frame = (self.frame + 1) % 2

    def draw(self):
        self.image.clip_draw(0, self.frame * 250, 1280, 250, self.x, self.y)

    def get_bb(self):
        return self.x - 640, self.y - 90, self.x + 640, self.y + 90


# stage 4 상하좌우 벽
class UpDownWall:
    def __init__(self):
        self.image_up = load_image('Resource\\image\\wall_1.png')
        self.image_down = load_image('Resource\\image\\wall_1.png')
        self.x1, self.y1 = 640, 25
        self.x2, self.y2 = 640, 675

    def update(self):
        pass

    def draw(self):
        self.image_up.clip_draw(0, 0, 1280, 50, self.x1, self.y1)
        self.image_down.clip_draw(0, 0, 1280, 50, self.x2, self.y2)

    def get_bb(self):
        return self.x1 - 640, self.y1 - 25, self.x1 + 640, self.y1 + 25


class LeftRightWall:
    def __init__(self):
        self.image_left = load_image('Resource\\image\\wall_2.png')
        self.image_right = load_image('Resource\\image\\wall_2.png')
        self.x1, self.y1 = 25, 350
        self.x2, self.y2 = 1265, 350

    def update(self):
        pass

    def draw(self):
        self.image_left.clip_draw(0, 0, 50, 700, self.x1, self.y1)
        self.image_right.clip_draw(0, 0, 50, 700, self.x2, self.y2)

    def get_bb(self):
        return self.x1 - 25, self.y1 - 350, self.x1 + 25, self.y1 + 350
