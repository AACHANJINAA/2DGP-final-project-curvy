import random

from pico2d import*
import game_framework
import game_world
import server

from move_kirby import Kirby
from Background import BACK, POTAL
from move_monster import BASIC_MONSTER, SWORD_MONSTER, SPARK_MONSTER, BOMBER_MONSTER
from move_boss import SWORD_BOSS, SPARK_BOSS, BOMBER_BOSS,LAST_BOSS

server.kirby = None
server.background = [None, None, None, None,
                     None, None, None,
                     None, None, None, None]
server.monster = [None, None, None, None]
BM = None
server.stage_number, server.potal_number = 0, 0

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            server.kirby.handle_event(event)

def enter():
    global BM
    server.kirby = Kirby()
    server.potal = [POTAL(0, 0),
                    POTAL(1, 0),
                    POTAL(2, 0),

                    POTAL(0, 1),
                    POTAL(3, 0),
                    POTAL(4, 0),

                    POTAL(0, 2),
                    POTAL(5, 0),
                    POTAL(6, 0),

                    POTAL(0, 3),
                    POTAL(7, 0)]
    BM = [BASIC_MONSTER(500), BASIC_MONSTER(600), BASIC_MONSTER(800),
          BASIC_MONSTER(1000), BASIC_MONSTER(1200), BASIC_MONSTER(1250),
          BASIC_MONSTER(1600), BASIC_MONSTER(1900), BASIC_MONSTER(2000)]
    server.monster = [BASIC_MONSTER(300), SWORD_MONSTER(), SPARK_MONSTER(), BOMBER_MONSTER()]
    server.boss = [SWORD_BOSS(), SPARK_BOSS(), BOMBER_BOSS(), LAST_BOSS()]
    stage(server.stage_number)

def stage(n):
    global BM
    server.kirby.hp_cnt = 8.0
    match n:
        case 0:  # map(potal_num is 0)
            game_world.add_collision_group(server.kirby, server.potal[0], 'kirby:enter_potal')
            server.background = BACK(0)
            game_world.add_object(server.background, 0)
            game_world.add_object(server.potal[0], 0)
            game_world.add_object(server.kirby, 1)
        case 1:  # basic_stage_1
            server.kirby.x = 30
            game_world.add_collision_group(server.kirby, server.potal[1], 'kirby:enter_potal')
            server.background = BACK(1)
            game_world.add_object(server.background, 0)
            game_world.add_object(server.potal[1], 0)
            game_world.add_object(server.kirby, 1)
            for i in range(0, 9):
                game_world.add_object(BM[i], 1)
                game_world.add_collision_group(server.kirby, BM[i], 'kirby:basic_monster')
                game_world.add_collision_group(server.kirby, BM[i], 'kirby_skill:basic_monster')
            game_world.add_object(server.monster[1], 1)
            game_world.add_collision_group(server.kirby, server.monster[1], 'kirby:sword_monster')
            game_world.add_collision_group(server.kirby, server.monster[1], 'kirby_skill:sword_monster')
        case 2:  # boss_stage_1
            server.kirby.x = 30
            game_world.add_object(server.potal[2], 0)
            server.background = BACK(4)
            game_world.add_object(server.background, 0)
            server.mode = 1
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.boss[0], 1)
            game_world.add_collision_group(server.kirby, server.boss[0], 'kirby:sword_boss')
            game_world.add_collision_group(server.kirby, server.boss[0], 'kirby_skill:sword_boss')
        case 3:  # map(potal_num is 0)
            game_world.add_collision_group(server.kirby, server.potal[3], 'kirby:enter_potal')
            server.background = BACK(0)
            game_world.add_object(server.background, 0)
            server.mode = 0
            game_world.add_object(server.potal[3], 0)
            game_world.add_object(server.kirby, 1)
        case 4:  # basic_stage_2
            server.kirby.x = 30
            game_world.add_collision_group(server.kirby, server.potal[4], 'kirby:enter_potal')
            server.background = BACK(2)
            game_world.add_object(server.background, 0)
            game_world.add_object(server.potal[4], 0)
            game_world.add_object(server.kirby, 1)
            for i in range(0, 9):
                game_world.add_object(BM[i], 1)
                game_world.add_collision_group(server.kirby, BM[i], 'kirby:basic_monster')
                game_world.add_collision_group(server.kirby, BM[i], 'kirby_skill:basic_monster')
            game_world.add_object(server.monster[2], 1)
            game_world.add_collision_group(server.kirby, server.monster[2], 'kirby:spark_monster')
            game_world.add_collision_group(server.kirby, server.monster[2], 'kirby_skill:spark_monster')
        case 5:  # boss_stage_2
            server.kirby.x = 30
            server.background = BACK(5)
            game_world.add_object(server.background, 0)
            server.mode = 2
            game_world.add_object(server.potal[5], 0)
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.boss[1], 1)
            game_world.add_collision_group(server.kirby, server.boss[1], 'kirby:spark_boss')
            game_world.add_collision_group(server.kirby, server.boss[1], 'kirby_skill:spark_boss')
        case 6:  # map(potal_num is 0)
            game_world.add_collision_group(server.kirby, server.potal[6], 'kirby:enter_potal')
            server.background = BACK(0)
            game_world.add_object(server.background, 0)
            game_world.add_object(server.potal[6], 0)
            server.mode = 0
            game_world.add_object(server.kirby, 1)
        case 7:  # basic_stage_3
            server.kirby.x = 30
            game_world.add_collision_group(server.kirby, server.potal[7], 'kirby:enter_potal')
            server.background = BACK(3)
            game_world.add_object(server.background, 0)
            game_world.add_object(server.potal[7], 0)
            game_world.add_object(server.kirby, 1)
            for i in range(0, 9):
                game_world.add_object(BM[i], 1)
                game_world.add_collision_group(server.kirby, BM[i], 'kirby:basic_monster')
                game_world.add_collision_group(server.kirby, BM[i], 'kirby_skill:basic_monster')
            game_world.add_object(server.monster[3], 1)
            game_world.add_collision_group(server.kirby, server.monster[3], 'kirby:bomber_monster')
            game_world.add_collision_group(server.kirby, server.monster[3], 'kirby_skill:bomber_monster')
        case 8:  # boss_stage_3
            server.kirby.x = 30
            server.background = BACK(6)
            game_world.add_object(server.background, 0)
            server.mode = 3
            game_world.add_object(server.potal[8], 0)
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.boss[2], 1)
            game_world.add_collision_group(server.kirby, server.boss[2], 'kirby:bomber_boss')
            game_world.add_collision_group(server.kirby, server.boss[2], 'kirby_skill:bomber_boss')
        case 9:  # map(potal_num is 0)
            game_world.add_collision_group(server.kirby, server.potal[9], 'kirby:enter_potal')
            server.background = BACK(0)
            game_world.add_object(server.background, 0)
            game_world.add_object(server.potal[9], 0)
            server.mode = 0
            game_world.add_object(server.kirby, 1)
        case 10:  # boss_stage_final
            server.kirby.x = 30
            server.background = BACK(7)
            game_world.add_object(server.background, 0)
            server.mode = 1
            game_world.add_object(server.kirby, 1)
            game_world.add_object(server.boss[3], 1)
            game_world.add_collision_group(server.kirby, server.boss[3], 'kirby:last_boss')
            game_world.add_collision_group(server.kirby, server.boss[3], 'kirby_skill:last_boss')

def exit():
    game_world.clear()

def update():
    global BM
    if server.stage_replay:
        game_world.remove_object(server.kirby)
        print(server.stage_number - 1)
        game_world.remove_object(server.potal[server.stage_number - 1])
        game_world.remove_object(server.background)
        stage(server.stage_number)
        server.stage_replay = False
    if server.stage_restart:
        game_world.clear()
        if server.stage_number not in (2, 5, 8, 10):
            server.mode = 0
        stage(server.stage_number)
        server.stage_restart = False

    for game_object in game_world.all_objects():
        game_object.update()
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('collision by group', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)


def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()
def draw():
    clear_canvas()
    draw_world()
    update_canvas()
def pause():
    pass
def resume():
    pass
# def test_self():
#     import play_state
#
#     pico2d.open_canvas()
#     game_framework.run(play_state)
#     pico2d.clear_canvas()
#
# if __name__ == '__main__':
#     test_self()
