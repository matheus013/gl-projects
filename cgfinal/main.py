import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *

from cgfinal.builder import *

ref_x = 1
ref_y = 1
ref_z = 0


def draw_game():
    glMatrixMode(GL_MODELVIEW)

    glPushMatrix()
    build(DataUtil.edges, DataUtil.vertices, DataUtil.surfaces)
    glPopMatrix()

    build_arcs(ref_x, ref_y, ref_z)

    # mid front door
    build_door(door_conf['front'][0], ('front', 0))
    build_door(door_conf['front'][1], ('front', 1))
    build_door(door_conf['front'][2], ('front', 2))
    build_door(door_conf['front'][3], ('front', 3))
    build_door(door_conf['front'][4], ('front', 4))


def generate(x, y, z):
    build_front(x, y, z)  # OK surface
    # print(door_conf['front'][0].print())
    build_right(x, y, z)  # OK surface

    center_ground = (center_point[0], center_point[1], center_point[2])
    origin_ground = (x, y, z)
    if ground:
        build_ground(center_ground, origin_ground, 3)  # OK surface
    build_left(x, y, z)  # OK surface
    build_back(x, y, z)  # OK surface
    build_top(x, y, z)
    build_tower(x, y, z)  # OK surface

    build_pillar(x + tower_width, y, z + depth * (2 / 15), height, width / 20)
    build_pillar(x + tower_width, y, z + depth * (4 / 15), height, width / 20)
    build_pillar(x + tower_width, y, z + depth * (6 / 15), height, width / 20)

    build_pillar(x + width - tower_width, y, z + depth * (2 / 15), height, width / 20)
    build_pillar(x + width - tower_width, y, z + depth * (4 / 15), height, width / 20)
    build_pillar(x + width - tower_width, y, z + depth * (6 / 15), height, width / 20)

    build_wall((x, y, z + depth * 0.4 + attachment_depth), (x + tower_width, y, z + depth * 0.4 + attachment_depth),
               height)
    build_pillar(x + tower_width, y, z + depth * 0.4 + attachment_depth, height, width / 20)

    build_wall((x + width - tower_width, y, z + depth * 0.4 + attachment_depth),
               (x + width, y, z + depth * 0.4 + attachment_depth),
               height)
    build_pillar(x + width - tower_width, y, z + depth * 0.4 + attachment_depth, height, width / 20)

    build_wall((x + tower_width * 1.5, y, z + depth * 0.4 + attachment_depth),
               (x + tower_width, y, z + depth * 0.4 + attachment_depth),
               height)

    build_wall((x + width - tower_width * 1.5, y, z + depth * 0.4 + attachment_depth),
               (x + width, y, z + depth * 0.4 + attachment_depth),
               height)


if __name__ == '__main__':
    pygame.init()
    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(30, (display[0] / display[1]), 0.1, 50.0)
    generate(ref_x, ref_y, ref_z)
    xa = 0
    ya = 0
    za = 0

    glOrtho(-5, 30, 10, -30, 15, 30)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)
                    za += 1
                    # print(xa, ya, za)
                if event.button == 5:
                    glTranslatef(0, 0, -1.0)
                    za -= 1
                    # print(xa, ya, za)
            if event.type == pygame.KEYDOWN:
                print(event.key, pygame.K_3)
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1, 0, 0)
                    xa -= 1
                    # print(xa, ya, za)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1, 0, 0)
                    xa += 1
                    # print(xa, ya, za)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                    ya += 1
                    # print(xa, ya, za)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)
                    ya -= 1
                    # print(xa, ya, za)

                if event.key == pygame.K_1:
                    k = ('front', 0)
                    door_conf[k[0]][k[1]].run_reverse()
                if event.key == pygame.K_2:
                    k = ('front', 1)
                    door_conf[k[0]][k[1]].run_reverse()
                if event.key == pygame.K_3:
                    k = ('front', 2)
                    door_conf[k[0]][k[1]].run_reverse()
                if event.key == pygame.K_4:
                    k = ('front', 3)
                    door_conf[k[0]][k[1]].run_reverse()
                if event.key == pygame.K_5:
                    k = ('front', 4)
                    door_conf[k[0]][k[1]].run_reverse()

                if event.key == pygame.K_COMMA:
                    glRotatef(5, 0, 1, 0)
                if event.key == pygame.K_PERIOD:
                    glRotatef(-5, 0, 1, 0)
                if event.key == pygame.K_TAB:
                    DataUtil.face_view = not DataUtil.face_view

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_game()

        pygame.display.flip()
        pygame.time.wait(10)
