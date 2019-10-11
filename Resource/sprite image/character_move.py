from pico2d import *

def handle_events():
    global running
    global x, y
    global now_x, now_y
    global dir_x, dir_y
    global player_move
    global player_jump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        # 키보드 입력 - 플레이어 캐릭터 상하좌우 이동
        elif event.type == SDL_KEYDOWN:
            player_move = True
            now_x, now_y = x, y
            if event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
        # 문제 해결해야함 - 방향키 두개 동시에 누르고 있을때 하나를 때면 움직임 멈춤
        elif event.type == SDL_KEYUP:
            dir_x, dir_y = 0, 0

        # 키보드 입력 - 플레이어 캐릭터 점프
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE and event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_SPACE and event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_SPACE and event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_SPACE and event.key == SDLK_LEFT:
                dir_x -= 1

            elif event.key == SDLK_ESCAPE:
                running = False
    pass

BACKGROUND_WIDTH, BACKGROUND_HEIGHT = 1280, 900
running = True
player_move = False
player_jump = False
x, y = 100, 300
now_x, now_y = 0, 0
dir_x, dir_y = 0, 0

open_canvas()

background = load_image('background.png')
character = load_image('player.png')
character_jump = load_image('player_jump.png')
boss_move = load_image('boss_move.png')


while running:
    clear_canvas()
    background.draw(BACKGROUND_WIDTH // 2, BACKGROUND_HEIGHT // 2)

    if player_move:
        character.clip_draw(0, 0, 30, 30, x, y)

    else:
        dir_x, dir_y = 0, 0

    update_canvas()
    handle_events()
    x += dir_x * 3
    y += dir_y * 3
    delay(0.01)



close_canvas()