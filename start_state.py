import game_framework
from pico2d import *
import title_state

name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('Resource\\image\\start_image.png')


def exit():
    global image
    del(image)


def update():
    global logo_time

    if logo_time > 1.0:
        logo_time = 0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01


def draw():
    global image
    clear_canvas()
    image.draw(1280//2, 700//2)
    update_canvas()

def handle_events():
    events = get_events()
    pass
