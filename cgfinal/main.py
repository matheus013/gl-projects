import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pygame.locals import *

from cgfinal.constants import *

from cgfinal.support import *
from cgfinal.builder import *


def draw_game():
    glMatrixMode(GL_MODELVIEW)

    glPushMatrix()
    build(DataUtil.edges, DataUtil.vertices)
    glPopMatrix()

    pass


def generate(x, y, z):
    build_front(x, y, z)
    build_right(x, y, z)
    # build_ground(x, y, z)
    build_left(x, y, z)
    build_back(x, y, z)
    # build_top(x, y, z)
    pass


if __name__ == '__main__':
    pygame.init()
    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(30, (display[0] / display[1]), 0.1, 50.0)
    generate(1, 1, 0)

    gluOrtho2D(0, 30, 30, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0, 0, 1.0)
                if event.button == 5:
                    glTranslatef(0, 0, -1.0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)

                if event.key == pygame.K_COMMA:
                    glRotatef(5, 0, 1, 0)
                if event.key == pygame.K_PERIOD:
                    glRotatef(-5, 0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glRotatef(1, 0, 1, 0)

        draw_game()

        pygame.display.flip()
        pygame.time.wait(10)
