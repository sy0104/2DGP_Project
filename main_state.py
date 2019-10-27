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
        self.hp = 4
        self.dir_x = 0
        self.dir_y = 0

    def update(self):
        self.x += self.dir_x
        self.y += self.dir_y
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 30, 30, self.x, self.y)


# 보스 캐릭터 - 팔 움직이는 보스
class Moving_Boss:
    def __init__(self):
        self.image = load_image('boss_move.png')
        self.x, self.y = 650, 350
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 4
        #delay(0.5)

    def draw(self):
        self.image.clip_draw(self.frame * 800, 0, 800, 800, self.x, self.y)




def enter():
    global background, player, moving_boss
    player = Player()
    background = Background()
    moving_boss = Moving_Boss()


def exit():
    global background, player, moving_boss
    del(background)
    del(player)
    del(moving_boss)
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
    pass

def draw():
    clear_canvas()
    background.draw()
    player.draw()
    moving_boss.draw()
    update_canvas()





