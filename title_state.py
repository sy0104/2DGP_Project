import game_framework
from pico2d import *
import main_state
import stage1_image

name = "TitleState"
image = None


def enter():
    global image
    image = load_image('Resource\\image\\title_image.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
                game_framework.change_state(stage1_image)


def draw():
    clear_canvas()
    image.draw(1280//2, 700//2)
    update_canvas()


def update():
    pass

def pause():
    pass

def resume():
    pass

