import game_framework
from pico2d import *
import stage_4
name = "stage4_image"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('Resource\\image\\Stage_4.png')



def exit():
    global image
    del(image)


def update():
    global logo_time

    if logo_time > 0.5:
        logo_time = 0
        game_framework.change_state(stage_4)
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
