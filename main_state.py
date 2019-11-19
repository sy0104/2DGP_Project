import random
import json
import os

from pico2d import *
import game_framework
import title_state
import game_world
import stage_1
import stage2_image

from Enemies import SmallestEnemy
from Enemies import SmallEnemy
from Enemies import BigEnemy
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
    global rect, background, boss_face, SmallestEnemy, SmallEnemy, BigEnemy
    rect = Rect()
    boss_face = BossFace()
    SmallestEnemy = [SmallestEnemy() for i in range(15)]
    SmallEnemy = [SmallEnemy() for j in range(10)]
    BigEnemy = [BigEnemy() for k in range(7)]
    background = Background()
    game_world.add_object(background, 0)
    game_world.add_object(rect, 1)
    game_world.add_object(boss_face, 1)
    for SmallestEnemy in SmallestEnemy:
        game_world.add_object(SmallestEnemy, 0)
    for SmallEnemy in SmallEnemy:
        game_world.add_object(SmallEnemy, 0)
    for BigEnemy in BigEnemy:
        game_world.add_object(BigEnemy, 0)

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



time = 0
def update():
    global time
    for game_object in game_world.all_objects():
        game_object.update()
    if collide(rect, boss_face):
        rect.hp -= 1
        print("COLLISION")

    if time > 100.0:
        logo_time = 0
        game_framework.change_state(stage2_image)
    time += 0.01
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

