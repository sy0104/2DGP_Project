from pico2d import *
import random

# stage 1, 3 - 보스 얼굴
class BossFace:
    def __init__(self):
        self.image = load_image('Resource\\image\\boss_face.png')
        self.x, self.y = 640, 380

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 280, 280, self.x, self.y)

    def get_bb(self):
        return self.x - 140, self.y - 140, self.x + 140, self.y + 140


# stage 3 - 우는 보스
class CryingBoss:
    def __init__(self):
        self.image = load_image('Resource\\image\\crying_boss.png')
        self.x, self.y = 640, 550

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 280, 280, self.x, self.y)

    def get_bb(self):
        return self.x - 140, self.y - 140, self.x + 140, self.y + 140


# stage 3 - 우는 보스 눈물 (long)
class LongTear:
    def __init__(self):
        self.image = load_image('Resource\\image\\tear_long.png')
        self.eye = random.randint(0, 1)
        self.time = 0
        self.x, self.y = 570, 485
        self.speed = 0.5

    def update(self):
        self.y -= self.speed
        if self.y <= 350:
            self.speed = random.randint(1, 3)
        elif self.y > 350:
            self.speed = 0.5

        if self.y <= -110:
            self.y = 485

    def draw(self):
        self.image.clip_draw(0, 0, 20, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 50, self.x + 10, self.y + 50


# stage 3 - 우는 보스 눈물 (short)
class ShortTear:
    def __init__(self):
        self.image = load_image('Resource\\image\\tear_short.png')
        self.time = 0
        self.x, self.y = 700, 485

        self.speed = 0.5

    def update(self):
        self.y -= self.speed
        if self.y <= 350:
            self.speed = random.randint(1, 3)
        elif self.y > 350:
            self.speed = 0.5

        if self.y <= -80:
            self.y = 485

    def draw(self):
        self.image.clip_draw(0, 0, 20, 70, self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 35, self.x + 10, self.y + 35


# stage 4(final) - 팔 내리치는 보스
class MovingBoss:
    def __init__(self):
        self.image = load_image('Resource\\image\\moving_boss.png')
        self.x, self.y = 640, 250
        self.frame = 0
        self.time = 0

    def update(self):
        self.time += 1
        if self.time % 50 == 0:
            self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 600, 0, 600, 600, self.x, self.y)

    def get_bb(self):
        return self.x - 250, self.y - 300, self.x + 250, self.y + 250


