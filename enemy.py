from pico2d import *
import random

# big enemy
class Enemy:
    def __init__(self):
        self.image = load_image('big_enemy.png')
        self.x, self.y = random.randint(0, 1280), 0
        self.speed = random.randint(0, 10)

    def update(self):
        self.x += self.speed
        self.y += self.speed


    def draw(self):
        self.image.clup_draw(0, 0, 30, 30, self.x, self.y)


