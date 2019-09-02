import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *

from cg_final.builder import *
from cg_final.support import register_texture, draw_object, draw

ref_x = 1
ref_y = 1
ref_z = 0


def draw_game():
    glMatrixMode(GL_MODELVIEW)
    for i in DataUtil.objects:
        glPushMatrix()
        draw(i)
        glPopMatrix()

    build_arcs(ref_x, ref_y, ref_z)

    # mid front door
    build_door(door_conf['front'][0], ('front', 0))
    build_door(door_conf['front'][1], ('front', 1))
    build_door(door_conf['front'][2], ('front', 2))
    build_door(door_conf['front'][3], ('front', 3))
    build_door(door_conf['front'][4], ('front', 4))
    build_door(door_conf['right'][0], ('right', 0))
    build_door(door_conf['right'][1], ('right', 1))
    build_door(door_conf['right'][2], ('right', 2))
    build_door(door_conf['left'][0], ('left', 0))

    # build_candle((0,0,0), 0.2, 5)


def turn_on_light():
    ambient_light = [0.2, 0.2, 0.2, 1]
    diffused_light = [0.9, 0.9, 0.9, 1]
    specular_light = [1.0, 1.0, 1.0, 1]
    position_light = [0.0, 600.0, 0.8, 1]

    glShadeModel(ref_light['model'])

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_light)

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffused_light)
    glLightfv(GL_LIGHT0, GL_SPECULAR, specular_light)
    glLightfv(GL_LIGHT0, GL_POSITION, position_light)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)


def generate(x, y, z):
    center_ground = (center_point[0], center_point[1], center_point[2])
    origin_ground = (x, y, z)

    if ground:
        build_ground(center_ground, origin_ground, 3)  # OK surface

    front = build_front(x, y, z)  # OK surface
    for i in front:
        DataUtil.objects.append(i)

    right = build_right(x, y, z)  # OK surface
    for i in right:
        DataUtil.objects.append(i)

    left = build_left(x, y, z)  # OK surface
    for i in left:
        DataUtil.objects.append(i)

    back = build_back(x, y, z)  # OK surface
    DataUtil.objects.append(back)

    top = build_top(x, y, z)
    for i in top:
        DataUtil.objects.append(i)

    tower = build_tower(x, y, z)  # OK surface
    for i in tower:
        DataUtil.objects.append(i)

    build_internal(x, y, z)  # OK surface


if __name__ == '__main__':
    pygame.init()
    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | GL_RGB)
    gluPerspective(30, (display[0] / display[1]), 0.1, 50.0)
    generate(ref_x, ref_y, ref_z)
    turn_on_light()
    register_texture()
    xa, ya, za = 0, 0, 0

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
                if event.button == 5:
                    glTranslatef(0, 0, -1.0)
                    za -= 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1, 0, 0)
                    xa -= 1
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1, 0, 0)
                    xa += 1
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                    ya += 1
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)
                    ya -= 1

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
                if event.key == pygame.K_6:
                    k = ('right', 0)
                    door_conf[k[0]][k[1]].run_reverse()
                if event.key == pygame.K_7:
                    k = ('right', 1)
                    door_conf[k[0]][k[1]].run_reverse()
                if event.key == pygame.K_8:
                    k = ('right', 2)
                    door_conf[k[0]][k[1]].run_reverse()
                if event.key == pygame.K_9:
                    k = ('left', 0)
                    door_conf[k[0]][k[1]].run_reverse()

                # rotate over X
                if event.key == pygame.K_w:
                    glTranslate(center_point[0], center_point[1], center_point[2])
                    glRotatef(5, 1, 0, 0)
                    glTranslate(-center_point[0], -center_point[1], -center_point[2])
                if event.key == pygame.K_s:
                    glTranslate(center_point[0], center_point[1], center_point[2])
                    glRotatef(-5, 1, 0, 0)
                    glTranslate(-center_point[0], -center_point[1], -center_point[2])
                # rotate over Y
                if event.key == pygame.K_a:
                    glTranslate(center_point[0], center_point[1], center_point[2])
                    glRotatef(5, 0, 1, 0)
                    glTranslate(-center_point[0], -center_point[1], -center_point[2])
                if event.key == pygame.K_d:
                    glTranslate(center_point[0], center_point[1], center_point[2])
                    glRotatef(-5, 0, 1, 0)
                    glTranslate(-center_point[0], -center_point[1], -center_point[2])

                if event.key == pygame.K_TAB:
                    DataUtil.face_view = not DataUtil.face_view

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_game()

        pygame.display.flip()
        pygame.time.wait(10)
