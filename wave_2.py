import random
import json
import os

import game_framework
from pico2d import *
import title_state

name = "wave_2"
background = None
rect = None
beat_up = None
beat_down = None


# 배경
class Background:
    def __init__(self):
        self.image = load_image('Resource\\image\\background_image.png')

    def draw(self):
        self.image.draw(1280//2, 700//2)

# 플레이어 캐릭터
class Rect:
    def __init__(self):
        self.image = load_image('Resource\\image\\player.png')
        self.x, self.y = 100, 300
        self.frame = 0
        self.time = 0
        self.hp = 4
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
        self.image.clip_draw(0, 0, 30, 30, self.x, self.y)

# wave2 - 위아래 공격
# 위
class BeatAttack_UP:
    def __init__(self):
        self.image = load_image('Resource\\image\\attack_beat_up.png')
        self.frame = 0
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer % 50 == 0:
            self.frame = (self.frame + 1) % 2

    def draw(self):
        self.image.clip_draw(0, self.frame * 300, 1280, 300, 640, 550)

# 아래
class BeatAttack_Down:
    def __init__(self):
        self.image = load_image('Resource\\image\\attack_beat.png')
        self.frame = 0
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer % 50 == 0:
            self.frame = (self.frame + 1) % 2

    def draw(self):
        self.image.clip_draw(0, self.frame * 300, 1280, 300, 640, 150)

#small enemy
class SmallEnemy:
    def __init__(self):
        self.image = load_image('Resource\\image\\small_enemy.png')
        self.x, self.y = 0, random.randint(0, 700)
        self.speed = random.randint(0, 3)

    def update(self):
        self.x += self.speed

    def draw(self):
        self.image.clip_draw(0, 0, 15, 15, self.x, self.y)

#smallest enemy
class SmallestEnemy:
    def __init__(self):
        self.image = load_image('Resource\\image\\smallest_enemy.png')
        self.x, self.y = random.randint(0, 1280), random.randint(0, 700)
        self.speed = random.randint(0, 3)

    def update(self):
        self.y += self.speed

    def draw(self):
        self.image.clip_draw(0, 0, 5, 5, self.x, self.y)


small = SmallEnemy()
smallest = SmallestEnemy()

small_enemies = [SmallEnemy() for i in range(10)]
smallest_enemies = [SmallestEnemy() for i in range(10)]

def enter():
    global background, rect, beat_up, beat_down, small, smallest
    background = Background()
    rect = Rect()
    beat_up = BeatAttack_UP()
    beat_down = BeatAttack_Down()


def exit():
    global background, rect, beat_up, beat_down
    del (background)
    del (rect)
    del (beat_up)
    del (beat_down)


def draw():
    clear_canvas()
    background.draw()
    rect.draw()
    beat_up.draw()
    beat_down.draw()
    for small in small_enemies:
        small.draw()
    for smallest in smallest_enemies:
        smallest.draw()
    update_canvas()


def update():
    rect.update()
    beat_up.update()
    beat_down.update()
    for small in small_enemies:
        small.update()
    for smallest in smallest_enemies:
        smallest.update()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        # 상하좌우 이동
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                rect.dir_y -= 2
            elif event.key == SDLK_UP:
                rect.dir_y += 2
            elif event.key == SDLK_RIGHT:
                rect.dir_x += 2
            elif event.key == SDLK_LEFT:
                rect.dir_x -= 2

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                rect.dir_y = 0
            elif event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                rect.dir_x = 0

def pause():
    pass

def resume():
    pass

