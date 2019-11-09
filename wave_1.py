import random
import json
import os

import game_framework
from pico2d import *
import title_state
import wave_2

name = "wave_1"
background = None
rect = None
boss_face = None

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

# wave1 - 보스 얼굴
class BossFace:
    def __init__(self):
        self.image = load_image('Resource\\image\\boss_face.png')
        self.x, self.y = 650, 300

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 280, 280, self.x, self.y)

def enter():
    global background, rect, boss_face
    background = Background()
    rect = Rect()
    boss_face = BossFace()

def exit():
    global background, rect, boss_face
    del (background)
    del (rect)
    del (boss_face)


def draw():
    clear_canvas()
    background.draw()
    rect.draw()
    boss_face.draw()
    update_canvas()

time = 0

def update():
    global time
    rect.update()

    if time > 10.0:
        logo_time = 0
        game_framework.change_state(wave_2)
    time += 0.01
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

