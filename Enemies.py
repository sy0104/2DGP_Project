from pico2d import *
import random


class SmallestEnemy:
    def __init__(self):
        self.image = load_image('Resource\\image\\smallest_enemy.png')
        self.x, self.y = random.randint(100, 1600), random.randint(100, 600)
        self.speed_x = random.randint(1, 5)
        self.speed_y = random.randint(1, 5)
        self.dir = random.randint(0, 1)
        self.drawing = 0

    def update(self):
        if self.dir == 0:
            self.x += self.speed_x
        else:
            self.y += self.speed_y

    def draw(self):
        self.image.clip_draw(0, 0, 5, 5, self.x, self.y)

    def get_bb(self):
        return self.x - 2.5, self.y - 2.5, self.x + 2.5, self.y + 2.5


class SmallEnemy:
    def __init__(self):
        self.image = load_image('Resource\\image\\small_enemy.png')
        self.x, self.y = random.randint(100, 1600), random.randint(100, 600)
        self.speed_x = random.randint(1, 5)
        self.speed_y = random.randint(1, 5)
        self.dir = random.randint(0, 1)
        self.drawing = 0

    def update(self):
        if self.dir == 0:
            self.x += self.speed_x
        else:
            self.y += self.speed_y

    def draw(self):
        self.image.clip_draw(0, 0, 15, 15, self.x, self.y)

    def get_bb(self):
        return self.x - 7.5, self.y - 7.5, self.x + 7.5, self.y + 7.5


class BigEnemy:
    def __init__(self):
        self.image = load_image('Resource\\image\\big_enemy.png')
        self.x, self.y = random.randint(100, 1600), random.randint(100, 600)
        self.speed_x = random.randint(1, 5)
        self.speed_y = random.randint(1, 5)
        self.dir = random.randint(0, 1)
        self.drawing = 0

    def update(self):
        if self.dir == 0:
            self.x += self.speed_x
        else:
            self.y += self.speed_y

    def draw(self):
        self.image.clip_draw(0, 0, 30, 30, self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15