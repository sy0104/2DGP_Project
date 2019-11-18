import random
import json
import os

from pico2d import *
import game_framework
import title_state
import game_world

from rect import Rect
from stage_1 import BossFace

name = "MainState"


# 배경
class Background:
    def __init__(self):
        self.image = load_image('Resource\\image\\background_image.png')
    def draw(self):
        self.image.draw(1280//2, 700//2)

    def update(self):
        pass

def enter():
    global rect, background, stage_1
    rect = Rect()
    stage_1 = BossFace()
    background = Background()
    game_world.add_object(background, 0)
    game_world.add_object(rect, 1)
    game_world.add_object(stage_1, 1)

    pass

def exit():
    game_world.clear()
    pass


def pause():
    pass


def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
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






def update():
    for game_object in game_world.all_objects():
        game_object.update()
    pass

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()





