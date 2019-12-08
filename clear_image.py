import game_framework
from pico2d import *

name = "clear"
image = None
bgm = None

def enter():
    global image, bgm
    image = load_image('Resource\\image\\Clear.png')
    bgm = load_music('Resource\\sound\\game_clear.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()



def exit():
    global image
    del(image)


def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(1280//2, 700//2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
    pass
