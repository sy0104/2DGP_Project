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


# stage 3 - 보스 팔 (좌우)
# left arm
class BossLeftArm:
    def __init__(self):
        self.image = load_image('Resource\\image\\boss_arm_left.png')
        self.x, self.y = 450, 200

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 212, 471, self.x, self.y)

    def get_bb(self):
        return self.x - 106, self.y - 235, self.x + 106, self.y + 235



# right arm
class BossRightArm:
    def __init__(self):
        self.image = load_image('Resource\\image\\boss_arm_right.png')
        self.x, self.y = 830, 200

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 212, 417, self.x, self.y)

    def get_bb(self):
        return self.x - 106, self.y - 235, self.x + 106, self.y + 235


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

        # 왼쪽 눈에서 떨어짐
        if self.eye == 0:
            self.x = random.randint(560, 600)
            self.y = 500
        # 오른쪽 눈에서 떨어짐
        elif self.eye == 1:
            self.x = random.randint(590, 710)
            self.y = 460

        self.speed = 0.5

    def update(self):
        self.eye = random.randint(0, 1)
        self.y -= self.speed
        if self.y <= 350:
            self.speed = 2
        elif self.y > 350:
            self.speed = 0.5

        if self.y - 50 <= 0:
            if self.eye == 0:
                self.y = 500
            elif self.eye == 1:
                self.y = 460

    def draw(self):
        self.image.clip_draw(0, 0, 20, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 50, self.x + 10, self.y + 50


# stage 3 - 우는 보스 눈물 (short)
class ShortTear:
    def __init__(self):
        self.image = load_image('Resource\\image\\tear_short.png')
        self.eye = random.randint(0, 1)
        self.time = 0

        # 왼쪽 눈에서 떨어짐
        if self.eye == 0:
            self.x = random.randint(560, 600)
            self.y = 500
        # 오른쪽 눈에서 떨어짐
        elif self.eye == 1:
            self.x = random.randint(590, 710)
            self.y = 460

        self.speed = 0.5

    def update(self):
        self.eye = random.randint(0, 1)
        self.y -= self.speed
        if self.y <= 350:
            self.speed = 2
        elif self.y > 350:
            self.speed = 0.5

        if self.y - 35 <= 0:
            if self.eye == 0:
                self.y = 500
            elif self.eye == 1:
                self.y = 460

    def draw(self):
        self.image.clip_draw(0, 0, 20, 70, self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 35, self.x + 10, self.y + 35


# stage 4(final) - 팔 움직이는 보스
class MovingBoss:
    def __init__(self):
        self.image = load_image('Resource\\image\\moving_boss.png')
        self.x, self.y = 640, 400
        self.frame = 0
        self.time = 0

    def update(self):
        self.time += 1
        if self.time % 50 == 0:
            self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 600, 0, 600, 600, self.x, self.y)

    def get_bb(self):
        return self.x - 250, self.y - 250, self.x + 250, self.y + 250