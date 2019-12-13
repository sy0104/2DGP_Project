from pico2d import *
import random

# start_place
# 1)    x = random,        y = 0 + pivot
# 2)    x = 0 + pivot,     y = random
# 3)    x = random,        y = 700 - pivot
# 4)    x = 1280 - pivot,  y = random


class SmallestEnemy:
    def __init__(self):
        self.image = load_image('Resource\\image\\smallest_enemy.png')
        self.speed = random.randint(1, 2)
        self.start_place = random.randint(1, 4)

        if self.start_place == 1:
            self.x, self.y = random.randint(5, 1275), 5
        elif self.start_place == 2:
            self.x, self.y = 5, random.randint(5, 695)
        elif self.start_place == 3:
            self.x, self.y = random.randint(5, 1275), 695
        elif self.start_place == 4:
            self.x, self.y = 1275, random.randint(5, 695)

    def update(self):
        if self.start_place == 1:
            self.y += self.speed
            if self.y >= 700-2.5 or self.y <= 0-2.5:
                self.speed *= -1
        elif self.start_place == 2:
            self.x += self.speed
            if self.x >= 1280-2.5 or self.x <= 0+2.5:
                self.speed *= -1
        elif self.start_place == 3:
            self.y -= self.speed
            if self.y <= 0+2.5 or self.y >= 700-2.5:
                self.speed *= -1
        elif self.start_place == 4:
            self.x -= self.speed
            if self.x <= 0+2.5 or self.x >= 1280-2.5:
                self.speed *= -1

    def draw(self):
        self.image.clip_draw(0, 0, 5, 5, self.x, self.y)

    def get_bb(self):
        return self.x - 2.5, self.y - 2.5, self.x + 2.5, self.y + 2.5


class SmallEnemy:
    def __init__(self):
        self.image = load_image('Resource\\image\\small_enemy.png')
        self.speed = random.randint(1, 2)
        self.start_place = random.randint(1, 4)

        if self.start_place == 1:
            self.x, self.y = random.randint(15, 1265), 15
        elif self.start_place == 2:
            self.x, self.y = 15, random.randint(15, 685)
        elif self.start_place == 3:
            self.x, self.y = random.randint(15, 1265), 685
        elif self.start_place == 4:
            self.x, self.y = 1265, random.randint(15, 685)

    def update(self):
        if self.start_place == 1:
            self.y += self.speed
            if self.y >= 700-7.5 or self.y <= 0-7.5:
                self.speed *= -1
        elif self.start_place == 2:
            self.x += self.speed
            if self.x >= 1280-7.5 or self.x <= 0+7.5:
                self.speed *= -1
        elif self.start_place == 3:
            self.y -= self.speed
            if self.y <= 0+7.5 or self.y >= 700-7.5:
                self.speed *= -1
        elif self.start_place == 4:
            self.x -= self.speed
            if self.x <= 0+7.5 or self.x >= 1280-7.5:
                self.speed *= -1

    def draw(self):
        self.image.clip_draw(0, 0, 15, 15, self.x, self.y)

    def get_bb(self):
        return self.x - 7.5, self.y - 7.5, self.x + 7.5, self.y + 7.5


class BigEnemy:
    def __init__(self):
        self.image = load_image('Resource\\image\\big_enemy.png')
        self.speed = random.randint(1, 3)
        self.start_place = random.randint(1, 4)

        if self.start_place == 1:
            self.x, self.y = random.randint(30, 1250), 30
        elif self.start_place == 2:
            self.x, self.y = 30, random.randint(30, 670)
        elif self.start_place == 3:
            self.x, self.y = random.randint(30, 1250), 670
        elif self.start_place == 4:
            self.x, self.y = 1250, random.randint(30, 670)

    def update(self):
        if self.start_place == 1:
            self.y += self.speed
            if self.y >= 700-15 or self.y <= 0-15:
                self.speed *= -1
        elif self.start_place == 2:
            self.x += self.speed
            if self.x >= 1280-15 or self.x <= 0+15:
                self.speed *= -1
        elif self.start_place == 3:
            self.y -= self.speed
            if self.y <= 0+15 or self.y >= 700-15:
                self.speed *= -1
        elif self.start_place == 4:
            self.x -= self.speed
            if self.x <= 0+15 or self.x >= 1280-15:
                self.speed *= -1

    def draw(self):
        self.image.clip_draw(0, 0, 30, 30, self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 15, self.x + 15, self.y + 15


# Bouncing Enemy 15X15
class BouncingEnemy:
    def __init__(self):
        self.image = load_image('Resource\\image\\bouncing_enemy.png')
        self.x, self.y = random.randint(15, 1265), 15
        self.speed_x = random.randint(1, 2)
        self.speed_y = random.randint(1, 2)

    def update(self):
        self.y += self.speed_y
        if self.y >= 700:
            self.x += self.speed_x
            if self.y >= 680 or self.y <= 15:
                self.speed_y *= -1
            if self.x >= 1265 or self.x <= 15:
                self.speed_x *= -1
        else:
            self.x -= self.speed_x
            if self.y >= 680or self.y <= 15:
                self.speed_y *= -1
            if self.x >= 1265 or self.x <= 15:
                self.speed_x *= -1

    def draw(self):
        self.image.clip_draw(0, 0, 15, 15, self.x, self.y)

    def get_bb(self):
        return self.x - 7.5, self.y - 7.5, self.x + 7.5, self.y + 7.5


# stage 3 떨어지는 톱니바퀴
class Cogwheel:
    def __init__(self):
        self.image = load_image('Resource\\image\\cogwheel_1.png')
        self.x, self.y = random.randint(40, 1260), 720
        self.speed_y = random.randint(1, 4)

    def update(self):
        self.y -= self.speed_y
        if self.y <= -40:
            self.x = random.randint(40, 1260)
            self.y = random.randint(740, 900)

    def draw(self):
        self.image.clip_draw(0, 0, 40, 40, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


# stage 3 원모양 enemy
class CircleEnemy:
    def __init__(self):
        self.image = load_image('Resource\\image\\enemy_circle.png')
        self.x, self.y = random.randint(15, 1265), 715
        self.speed_y = random.randint(1, 3)

    def update(self):
        self.y -= self.speed_y
        if self.y <= -30:
            self.x = random.randint(15, 1265)
            self.y = random.randint(730,  850)

    def draw(self):
        self.image.clip_draw(0, 0, 15, 15, self.x, self.y)

    def get_bb(self):
        return self.x - 7.5, self.y - 7.5, self.x + 7.5, self.y + 7.5

