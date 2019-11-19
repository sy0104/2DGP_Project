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
