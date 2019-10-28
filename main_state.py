import random
import json
import os

from pico2d import *
import game_framework
import title_state

name = "MainState"


player = None
background = None
moving_boss = None
big_enemy = None
small_enemy = None

# 배경
class Background:
    def __init__(self):
        self.image = load_image('background_image.png')
    def draw(self):
        self.image.draw(1280//2, 700//2)


# 플레이어 캐릭터
class Player:
    def __init__(self):
        self.image = load_image('player.png')
        self.x, self.y = 100, 300
        self.frame = 0
        self.time = 0
        self.hp = 4
        self.dir_x = 0
        self.dir_y = 0

    def update(self):
        self.x += self.dir_x
        self.y += self.dir_y
        if self.x >= 1280 or self.x <= 0:
            self.dir_x = 0
        if self.y >= 700 or self.y <= 0:
            self.dir_y = 0
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 30, 30, self.x, self.y)


# 보스 캐릭터 - 팔 움직이는 보스
class Moving_Boss:
    def __init__(self):
        self.image = load_image('moving_boss.png')
        self.x, self.y = 650, 300
        self.frame = 0
        self.time = 0

    def update(self):
        self.time += 1
        if self.time % 100 == 0:
            self.frame = (self.frame + 1) % 4
        #delay(0.5)

    def draw(self):
        self.image.clip_draw(self.frame * 600, 0, 600, 600, self.x, self.y)

# big enemy
class BigEnemy:
    def __init__(self):
        self.image = load_image('big_enemy.png')
        self.x, self.y = random.randint(0, 1280), 0
        self.speed = random.randint(0, 3)

    def update(self):
        self.y += self.speed

    def draw(self):
        self.image.clip_draw(0, 0, 30, 30, self.x, self.y)

#small enemy
class SmallEnemy:
    def __init__(self):
        self.image = load_image('small_enemy.png')
        self.x, self.y = 0, random.randint(0, 700)
        self.speed = random.randint(0, 3)

    def update(self):
        self.x += self.speed

    def draw(self):
        self.image.clip_draw(0, 0, 30, 30, self.x, self.y)


def enter():
    global background, player, moving_boss, big_enemy, small_enemy
    player = Player()
    background = Background()
    moving_boss = Moving_Boss()
    big_enemy = BigEnemy()
    small_enemy = SmallEnemy()

def exit():
    global background, player, moving_boss, big_enemy, small_enemy
    del(background)
    del(player)
    del(moving_boss)
    del(big_enemy)
    del(small_enemy)
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
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                player.dir_y -= 2
            elif event.key == SDLK_UP:
                player.dir_y += 2
            elif event.key == SDLK_RIGHT:
                player.dir_x += 2
            elif event.key == SDLK_LEFT:
                player.dir_x -= 2
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP or event.key == SDLK_DOWN:
                player.dir_y = 0
            elif event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                player.dir_x = 0






def update():
    player.update()
    moving_boss.update()
    big_enemy.update()
    small_enemy.update()
    pass

def draw():
    clear_canvas()
    background.draw()
    player.draw()
    moving_boss.draw()
    big_enemy.draw()
    small_enemy.draw()
    update_canvas()





