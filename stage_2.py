import random
import json
import os

import game_framework
from pico2d import *
import game_world
import stage3_image
from rect import Rect
from BeatAttack import BeatAttack_Down
from BeatAttack import BeatAttack_UP

name = "stage_2"


# 배경
class Background:
    def __init__(self):
        self.image = load_image('Resource\\image\\background_image.png')

    def draw(self):
        self.image.draw(1280//2, 700//2)

    def update(self):
        pass


def enter():
    global rect, background, beat_up, beat_down
    rect = Rect()
    background = Background()
    beat_up = BeatAttack_UP()
    beat_down = BeatAttack_Down()
    game_world.add_object(background, 0)
    game_world.add_object(rect, 1)
    game_world.add_object(beat_up, 0)
    game_world.add_object(beat_down, 0)


def exit():
    game_world.clear()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

time = 0
def update():
    global time
    for game_object in game_world.all_objects():
        game_object.update()
    if collide(rect, beat_up):
        rect.hp -= 1
        print("COLLISION")
    if collide(rect, beat_down):
        rect.hp -= 1
        print("COLLISION")

    # stage3으로 넘어감
    if time > 10.0:
        logo_time = 0
        game_framework.change_state(stage3_image)
    time += 0.01


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            #game_framework.change_state(title_state)
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
            # hp 설정
            elif event.key == SDLK_p:
                rect.hp = 2
            elif event.key == SDLK_o:
                rect.hp = 1

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                rect.dir_y = 0
            elif event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                rect.dir_x = 0
