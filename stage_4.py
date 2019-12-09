import random
import json
import os

import game_framework
from pico2d import *
import game_world
import clear_image
import gameover_image
from rect import Rect
from Boss import MovingBoss
from BackgroundAttack import UpDownWall, LeftRightWall
from Enemies import BouncingEnemy, CircleEnemy, SmallestEnemy

name = "stage_4"


# 배경
class Background:
    def __init__(self):
        self.image = load_image('Resource\\image\\background_image.png')

    def draw(self):
        self.image.draw(1280 // 2, 700 // 2)

    def update(self):
        pass


def enter():
    global rect
    rect = Rect()
    game_world.add_object(rect, 1)

    global background
    background = Background()
    game_world.add_object(background, 0)

    global moving_boss
    moving_boss = MovingBoss()
    game_world.add_object(moving_boss, 0)

    global up_down_wall
    up_down_wall = UpDownWall()
    game_world.add_object(up_down_wall, 1)

    global left_right_wall
    left_right_wall = LeftRightWall()
    game_world.add_object(left_right_wall, 1)

    global bouncing_enemies
    bouncing_enemies = [BouncingEnemy() for k in range(5)]
    game_world.add_objects(bouncing_enemies, 0)

    global circles
    circles = [CircleEnemy() for w in range(7)]
    game_world.add_objects(circles, 0)

    global smallest_enemies
    smallest_enemies = [SmallestEnemy() for i in range(15)]
    game_world.add_objects(smallest_enemies, 0)



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

    # rect & moving boss 충돌체크
    if collide(rect, moving_boss) and not rect.isCollide:
        rect.isCollide = True
        rect.hp -= 1
        print("rect & moving boss COLLISION")

    # rect & wall 충돌체크
    if collide(rect, up_down_wall) and not rect.isCollide:
        rect.isCollide = True
        rect.hp -= 1
        print("rect & wall COLLISION")

    if collide(rect, left_right_wall) and not rect.isCollide:
        rect.isCollide = True
        rect.hp -= 1
        print("rect & wall COLLISION")

    # rect & bouncing ball 충돌체크
    for bouncing in bouncing_enemies:
        if collide(bouncing, rect) and not rect.isCollide:
            rect.isCollide = True
            rect.hp -= 1
            print("rect & bouncing enemy COLLISION")

    # rect & circle 충돌체크
    for circle in circles:
        if collide(circle, rect) and not rect.isCollide:
            rect.isCollide = True
            rect.hp -= 1
            print("rect & circle COLLISION")

    # rect & smallest ball 충돌체크
    for smallest in smallest_enemies:
        if collide(smallest, rect) and not rect.isCollide:
            rect.isCollide = True
            rect.hp -= 1
            print("rect & smallest enemy COLLISION")

    # clear 로 넘어감
    next_stage_time += 0.01
    if next_stage_time > 80.0:
        game_framework.change_state(clear_image)

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
        # elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
        # game_framework.change_state(title_state)
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

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                rect.dir_y = 0
            elif event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                rect.dir_x = 0
            elif event.key == SDLK_n:
                game_framework.change_state(clear_image)
