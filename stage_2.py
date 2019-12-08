import random
import json
import os

import game_framework
from pico2d import *
import game_world
import stage3_image
import title_state
import gameover_image
import clear_image

from rect import Rect
from BackgroundAttack import BeatAttack_Down, BeatAttack_UP
from Enemies import SmallestEnemy, SmallEnemy, BouncingEnemy

name = "stage_2"

background = None
smallest_enemies = []
small_enemies = []
bouncing_enemies = []


# 배경
class Background:
    def __init__(self):
        self.image = load_image('Resource\\image\\background_image.png')

    def draw(self):
        self.image.draw(1280//2, 700//2)

    def update(self):
        pass


def enter():
    global rect
    rect = Rect()
    game_world.add_object(rect, 1)

    global background
    background = Background()
    game_world.add_object(background, 0)

    global beat_up
    beat_up = BeatAttack_UP()
    game_world.add_object(beat_up, 1)

    global beat_down
    beat_down = BeatAttack_Down()
    game_world.add_object(beat_down, 1)

    global smallest_enemies, SmallestEnemy
    smallest_enemies = [SmallestEnemy() for i in range(15)]
    game_world.add_objects(smallest_enemies, 0)

    global small_enemies, SmallEnemy
    small_enemies = [SmallEnemy() for j in range(10)]
    game_world.add_objects(small_enemies, 0)

    global bouncing_enemies
    bouncing_enemies = [BouncingEnemy() for k in range(5)]
    game_world.add_objects(bouncing_enemies, 0)



def exit():
    game_world.clear()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()


next_stage_time = 0
start_protecting = 0


def update():
    global next_stage_time, start_protecting
    for game_object in game_world.all_objects():
        game_object.update()

    # 처음 시작할때 잠시 무적
    start_protecting += 0.01
    if start_protecting <= 2.0:
        rect.isCollide = True

    # beat_up & rect 충돌
    if collide(rect, beat_up):
        rect.hp -= 1
        print("COLLISION")

    # beat_down & rect 충돌
    if collide(rect, beat_down):
        rect.hp -= 1
        print("COLLISION")

    # smallest_enemies & rect 충돌
    for smallest in smallest_enemies:
        if collide(smallest, rect) and not rect.isCollide:
            rect.isCollide = True
            rect.hp -= 1
            print("rect & smallest enemy COLLISION")

    # small_enemies & rect 충돌
    for small in small_enemies:
        if collide(small, rect) and not rect.isCollide:
            rect.isCollide = True
            rect.hp -= 1
            print("rect & small enemy COLLISION")

    # bouncing_enemies & rect 충돌
    for bouncing in bouncing_enemies:
        if collide(bouncing, rect) and not rect.isCollide:
            rect.isCollide = True
            rect.hp -= 1
            print("rect & bouncing enemy COLLISION")

    # stage3으로 넘어감
    next_stage_time += 0.01
    if next_stage_time > 60.0:
        game_framework.change_state(stage3_image)

    # rect.hp == 0이 되면 game over
    if rect.hp <= 0:
        game_framework.change_state(gameover_image)
    pass


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
            # hp 설정 치트키
            elif event.key == SDLK_1:
                rect.hp = 1
            elif event.key == SDLK_2:
                rect.hp = 2
            elif event.key == SDLK_3:
                rect.hp = 3
            elif event.key == SDLK_4:
                rect.hp = 1000
            # 다음 스테이지로 넘어감
            elif event.key == SDLK_n:
                game_framework.change_state(stage3_image)

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                rect.dir_y = 0
            elif event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                rect.dir_x = 0
