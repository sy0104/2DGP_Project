from pico2d import *


# stage 1, 3 - 보스 얼굴
class BossFace:
    def __init__(self):
        self.image = load_image('Resource\\image\\boss_face.png')
        self.x, self.y = 650, 300

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 280, 280, self.x, self.y)

    def get_bb(self):
        return self.x - 140, self.y - 140, self.x + 140, self.y + 140


# stage 3 - 보스 팔 (좌우)
# left arm
class BossLeftArm:
    pass


# right arm
class BossRightArm:
    pass


# stage 4(final) - 팔 움직이는 보스
class MovingBoss:
    pass