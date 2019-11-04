from pico2d import *

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE_UP, SPACE_DOWN = range(6)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}

# Player States
class IdleState:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += 1
        elif event == LEFT_DOWN:
            player.velocity -= 1
        elif event == RIGHT_UP:
            player.velocity -= 1
        elif event == LEFT_UP:
            player.velocity += 1
        player.timer = 1000

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frmae * 30, 0, 30, 30, player.x, player.y)



class MoveState:
    @staticmethod
    def enter(player, event):
        if event == RIGHT_DOWN:
            player.velocity += 1
        elif event == LEFT_DOWN:
            player.velocity -= 1
        elif event == RIGHT_UP:
            player.velocity -= 1
        elif event == LEFT_UP:
            player.velocity += 1
        player.dir = player.velocicty

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.x += player.velocity
        player.x = clamp(25, player.x, 800 - 25)

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frmae * 30, 0, 30, 30, player.x, player.y)

class DashState:
    @staticmethod
    def enter(player, event):
        player.timer = 0
        pass

    @staticmethod
    def exit(player, event):
        pass

    @staticmethod
    def do(player):
        player.timer += 1
        player.x += player.velocity * 3
        if player.timer >= 5:
            player.add_event(SPACE_UP)


next_state_table = {
    IdleState: {RIGHT_UP: MoveState, LEFT_UP: MoveState,
                RIGHT_DOWN: MoveState, LEFT_DOWN: MoveState},
    MoveState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
                SPACE_DOWN: DashState,
               RIGHT_DOWN and LEFT_DOWN: MoveState},
    DashState: {LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
                LEFT_UP: IdleState, RIGHT_UP: IdleState,
                SPACE_UP: MoveState, SPACE_DOWN: DashState}
}


class Player:
    def __init__(self):
        self.x, self.y = 100, 300
        self.image = load_image('player.png')
        self.velocity = 0
        self.dir = 1
        self.frame = 0
        self.event_que = []
        self.cur_state = MoveState
        self.cur_state.enter(self, None)
        pass

    def change_state(self, state):
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass

    def draw(self):
        self.cur_state.draw(self)
        pass

    def handle_event(self, event):
        # fill here
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass

