from pico2d import*
import game_framework
import game_world
import server


class BASIC_MONSTER:

    def __init__(self, x):
        self.store_x = x
        self.x, self.y = x, 100
        self.kx, self.ky = 70, 55
        self.frame = 0
        self.dir = -1
        self.sx, self.sy = 700, 100

        self.event_que = []
        self.cur_state = IDLE_BASIC_MONSTER
        self.cur_state.enter(self, None)

        self.Idle = load_image('basic_monster/basic/basic_monster.png')
        self.Hit = load_image('basic_monster/basic/basic_monster_hit.png')

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.sx - 25, self.sy - 25, self.sx + 25, self.sy + 25

    def handle_collision(self, other, group):
        match group:
            case 'kirby:basic_monster':
                pass
            case 'kirby_skill:basic_monster':
                if server.skill is True:
                    game_world.remove_object(self)
                pass

class IDLE_BASIC_MONSTER:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.dir = -1

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time / 2
        if self.x < 50 or self.x > self.store_x + 200 or self.x < self.store_x - 200 or self.x > 2350:
            self.dir *= -1

    @staticmethod
    def draw(self):
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom
        if self.dir == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 22, 0, 22, 19,
                                          0.0, '', self.sx, self.sy, self.kx, self.ky)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 22, 0, 22, 19,
                                          0.0, 'h', self.sx, self.sy, self.kx, self.ky)

class SWORD_MONSTER:
    def __init__(self):
        self.x, self.y = 450, 100
        self.kx, self.ky = 70, 55
        self.frame = 0
        self.dir = -1
        self.sx, self.sy = 700, 100

        self.event_que = []
        self.cur_state = IDLE_SWORD_MONSTER
        self.cur_state.enter(self, None)

        self.Idle = load_image('basic_monster/sword/sword_monster.png')
        self.Hit = load_image('basic_monster/sword/sword_monster_hit.png')

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass
    def get_bb(self):
        return self.sx - 25, self.sy - 25, self.sx + 25, self.sy + 25

    def handle_collision(self, other, group):
        match group:
            case 'kirby:sword_monster':
                pass
            case 'kirby_skill:sword_monster':
                if server.skill is True:
                    game_world.remove_object(self)
                pass

class IDLE_SWORD_MONSTER:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.dir = -1

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time / 2
        if self.x < 100 or self.x > 700:
            self.dir *= -1

    @staticmethod
    def draw(self):
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom
        if self.dir == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 27, 0, 27, 23,
                                          0.0, 'h', self.sx, self.sy, self.kx, self.ky)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 27, 0, 27, 23,
                                          0.0, '', self.sx, self.sy, self.kx, self.ky)


class SPARK_MONSTER:
    def __init__(self):
        self.x, self.y = 450, 100
        self.kx, self.ky = 70, 55
        self.frame = 0
        self.dir = -1
        self.sx, self.sy = 700, 100

        self.event_que = []
        self.cur_state = IDLE_SPARK_MONSTER
        self.cur_state.enter(self, None)

        self.Idle = load_image('basic_monster/spark/spark_monster.png')
        self.Hit = load_image('basic_monster/spark/spark_monster_hit.png')

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass
    def get_bb(self):
        return self.sx - 25, self.sy - 25, self.sx + 25, self.sy + 25

    def handle_collision(self, other, group):
        match group:
            case 'kirby:spark_monster':
                pass
            case 'kirby_skill:spark_monster':
                if server.skill is True:
                    game_world.remove_object(self)
                pass

class IDLE_SPARK_MONSTER:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.dir = -1

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time / 2
        if self.x < 100 or self.x > 700:
            self.dir *= -1

    @staticmethod
    def draw(self):
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom
        if self.dir == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 22, 0, 22, 19,
                                          0.0, 'h', self.sx, self.sy, self.kx, self.ky)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 22, 0, 22, 19,
                                          0.0, '', self.sx, self.sy, self.kx, self.ky)


class BOMBER_MONSTER:
    def __init__(self):
        self.x, self.y = 450, 100
        self.kx, self.ky = 70, 55
        self.frame = 0
        self.dir = -1
        self.sx, self.sy = 700, 100

        self.event_que = []
        self.cur_state = IDLE_BOMBER_MONSTER
        self.cur_state.enter(self, None)

        self.Idle = load_image('basic_monster/bomber/bomber_monster.png')
        self.Hit = load_image('basic_monster/bomber/bomber_monster_hit.png')

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.sx - 25, self.sy - 25, self.sx + 25, self.sy + 25

    def handle_collision(self, other, group):
        match group:
            case 'kirby:bomber_monster':
                pass
            case 'kirby_skill:bomber_monster':
                if server.skill is True:
                    game_world.remove_object(self)
                pass

class IDLE_BOMBER_MONSTER:
    @staticmethod
    def enter(self, event):
        self.frame = 0
        self.dir = -1

    @staticmethod
    def exit(self, event):
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time / 2
        if self.x < 100 or self.x > 700:
            self.dir *= -1

    @staticmethod
    def draw(self):
        self.sx = self.x - server.background.window_left
        self.sy = self.y - server.background.window_bottom
        if self.dir == -1:
            self.Idle.clip_composite_draw(int(self.frame) * 22, 0, 22, 26,
                                          0.0, 'h', self.sx, self.sy, self.kx, self.ky)
        else:
            self.Idle.clip_composite_draw(int(self.frame) * 22, 0, 22, 26,
                                          0.0, '', self.sx, self.sy, self.kx, self.ky)




PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8





