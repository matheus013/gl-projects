import math

import numpy
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *

CIRCLE_ANGLE_INC = 0.5

thickness = 1.0

width = 1.2
height = 0.9

p_width = 0.165
p_height = 0.403

g_width = 0.055
g_height = 0.183

t_width = 0.035
t_height = 0.08

radius = 0.0915

field = ()
edges_field = ()

delta_x = 0.0
delta_y = 0.0
delta_z = 0.0

alpha = 0.02

team_right = 0
team_left = 0

bres = False


def draw_bresenham(x1, y1, x2, y2):
    x1 *= 1000
    x2 *= 1000
    y1 *= 1000
    y2 *= 1000

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    # print x1, x2, y1, y2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = 0
    if x1 != x2:
        slope = dy / float(dx)

    x, y = x1, y1

    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx

    glVertex2f(x, y)

    for k in range(2, dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        glVertex2f(x, y)


def draw_text(text_string):
    font = pygame.font.Font(None, 64)
    text_surface = font.render(text_string, True, (255, 255, 255, 255), (0, 0, 0, 255))

    ref_x = (text_surface.get_width() / -600.0)
    ref_y = height * 0.7

    position = (ref_x, ref_y, 0)  # define start render

    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    glRasterPos3d(*position)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)


def draw_solid_circle(rad):
    glLineWidth(thickness)
    glBegin(GL_TRIANGLE_FAN)

    glVertex2f(0.0, 0.0)

    angle = 0
    while True:
        rads = math.radians(angle)
        glVertex3f(math.cos(rads) * rad, math.sin(rads) * rad, 0.0)
        angle += CIRCLE_ANGLE_INC
        if angle > 360:
            break

    glEnd()
    glLineWidth(1)


def draw_circle(rad, side_num, edge_only):
    glLineWidth(thickness)
    if edge_only:
        glBegin(GL_LINE_LOOP)
    else:
        glBegin(GL_POLYGON)

    for vertex in range(0, side_num):
        angle = float(vertex) * 2.0 * numpy.pi / side_num
        glVertex3f(numpy.cos(angle) * rad, numpy.sin(angle) * rad, 0.0)

    glEnd()
    glLineWidth(1)


def valid_points(points, r, object_name):
    for i in points:
        if len(i) != r:
            print('Invalid point after build ' + object_name + ' p: ' + str(i))
            return
    print('Build points from ' + object_name + ' is great!')
    pass


def valid_edges(edges, points, object_name):
    for i in edges:
        if len(i) == 2:
            if i[0] >= len(points) or i[0] < 0:
                print('Invalid edges after build ' + object_name + ' p: ' + str(i))
                return
            if i[1] >= len(points) or i[1] < 0:
                print('Invalid edges after build ' + object_name + ' p: ' + str(i))
                return
    print('Build edges from ' + object_name + ' is great!')


def build_border(x, y):
    global field, edges_field
    size = len(field)
    field += ((x + width / 2, y + height / 2, 0),
              (x - width / 2, y + height / 2, 0),
              (x - width / 2, y - height / 2, 0),
              (x + width / 2, y - height / 2, 0))
    edges_field += ((size, size + 1),
                    (size + 1, size + 2),
                    (size + 2, size + 3),
                    (size + 3, size))
    valid_points(field, 3, 'border')
    valid_edges(edges_field, field, 'border')


def build_goal(x, y):
    global field, edges_field
    size = len(field)
    # side one
    field += ((x - width / 2 + g_width, y + g_height / 2, 0),
              (x - width / 2, y + g_height / 2, 0),
              (x - width / 2, y - g_height / 2, 0),
              (x - width / 2 + g_width, y - g_height / 2, 0))

    edges_field += ((size, size + 1),
                    (size + 1, size + 2),
                    (size + 2, size + 3),
                    (size + 3, size))
    size = len(field)
    # side two
    field += ((x + width / 2 - g_width, y + g_height / 2, 0),
              (x + width / 2, y + g_height / 2, 0),
              (x + width / 2, y - g_height / 2, 0),
              (x + width / 2 - g_width, y - g_height / 2, 0))

    edges_field += ((size, size + 1),
                    (size + 1, size + 2),
                    (size + 2, size + 3),
                    (size + 3, size))

    valid_points(field, 3, 'goal')
    valid_edges(edges_field, field, 'goal')
    pass


def build_penalty(x, y):
    global field, edges_field
    size = len(field)
    # side one
    field += ((x - width / 2 + p_width, y + p_height / 2, 0),
              (x - width / 2, y + p_height / 2, 0),
              (x - width / 2, y - p_height / 2, 0),
              (x - width / 2 + p_width, y - p_height / 2, 0))

    edges_field += ((size, size + 1),
                    (size + 1, size + 2),
                    (size + 2, size + 3),
                    (size + 3, size))
    size = len(field)
    # side two
    field += ((x + width / 2 - p_width, y + p_height / 2, 0),
              (x + width / 2, y + p_height / 2, 0),
              (x + width / 2, y - p_height / 2, 0),
              (x + width / 2 - p_width, y - p_height / 2, 0))

    edges_field += ((size, size + 1),
                    (size + 1, size + 2),
                    (size + 2, size + 3),
                    (size + 3, size))

    valid_points(field, 3, 'penalty')
    valid_edges(edges_field, field, 'penalty')
    pass


def build_center_line(x, y):
    global field, edges_field
    size = len(field)
    # side one
    field += ((x, y + height / 2, 0),
              (x, y - height / 2, 0))
    edges_field += ((size, size + 1),)
    valid_points(field, 3, 'center_line')
    valid_edges(edges_field, field, 'center_line')
    pass


def build_crossbar(x, y):
    global field, edges_field
    size = len(field)
    # side one
    field += ((x - width / 2 - t_width, y + t_height / 2, 0),
              (x - width / 2, y + t_height / 2, 0),
              (x - width / 2, y - t_height / 2, 0),
              (x - width / 2 - t_width, y - t_height / 2, 0))

    edges_field += ((size, size + 1),
                    (size + 1, size + 2),
                    (size + 2, size + 3),
                    (size + 3, size))
    size = len(field)
    # side two
    field += ((x + width / 2 + t_width, y + t_height / 2, 0),
              (x + width / 2, y + t_height / 2, 0),
              (x + width / 2, y - t_height / 2, 0),
              (x + width / 2 + t_width, y - t_height / 2, 0))

    edges_field += ((size, size + 1),
                    (size + 1, size + 2),
                    (size + 2, size + 3),
                    (size + 3, size))

    valid_points(field, 3, 'crossbar')
    valid_edges(edges_field, field, 'crossbar')
    pass


def generate():
    build_border(0.0, 0.0)
    build_goal(0.0, 0.0)
    build_penalty(0.0, 0.0)
    build_center_line(0.0, 0.0)
    build_crossbar(0.0, 0.0)


def build(edges, points):
    glLineWidth(thickness)
    glBegin(GL_LINES)
    for edge in edges:
        if bres:
            draw_bresenham(points[edge[0]][0], points[edge[0]][1], points[edge[1]][0], points[edge[1]][0])
        else:

            for vertex in edge:
                glVertex3fv(points[vertex])

    glEnd()
    glLineWidth(1)


def is_goal():
    global team_left, team_right
    # side right
    right = valid_move(delta_x, delta_y, radius / 8, t_width, t_height, width / 2 + t_width / 2, 0)
    # side left
    left = valid_move(delta_x, delta_y, radius / 8, t_width, t_height, -(width / 2 + t_width / 2), 0)

    if right:
        team_right += 1
        to_mid()
    if left:
        team_left += 1
        to_mid()
    return right or left

    pass


def valid_move(center_ball_x, center_ball_y, rad, rec_width, rec_height, center_rec_x, center_rec_y):
    dist_x = abs(center_ball_x - center_rec_x)
    dist_y = abs(center_ball_y - center_rec_y)

    if dist_x > (rec_width / 2 + rad):
        return False
    if dist_y > (rec_height / 2 + rad):
        return False

    if dist_x <= (rec_width / 2):
        return True
    if dist_y <= (rec_height / 2):
        return True

    corner_distance_sq = (dist_x - rec_width / 2) ** 2 + (dist_y - rec_height / 2) ** 2

    return corner_distance_sq <= rad ** 2

    pass


def to_left():
    global delta_x, delta_y

    if valid_move(delta_x - alpha, delta_y, radius / 8, width, height, 0, 0) or is_goal():
        delta_x -= alpha
    pass


def to_right():
    global delta_x, delta_y

    if valid_move(delta_x + alpha, delta_y, radius / 8, width, height, 0, 0) or is_goal():
        delta_x += alpha
    pass


def to_up():
    global delta_x, delta_y

    if valid_move(delta_x, delta_y + alpha, radius / 8, width, height, 0, 0) or is_goal():
        delta_y += alpha
    pass


def to_down():
    global delta_x, delta_y

    if valid_move(delta_x, delta_y - alpha, radius / 8, width, height, 0, 0) or is_goal():
        delta_y -= alpha
    pass


def to_mid():
    global delta_x, delta_y
    delta_y = 0.0
    delta_x = 0.0


def draw_game():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)

    # draw field
    glPushMatrix()
    build(edges_field, field)
    draw_circle(radius, 9999, True)
    glPopMatrix()

    # draw ball
    glPushMatrix()
    glTranslatef(delta_x, delta_y, delta_z)
    draw_solid_circle(radius / 8)
    glPopMatrix()

    # draw score
    glPushMatrix()
    draw_text(str(team_left) + ' x ' + str(team_right))
    glPopMatrix()

    pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    win = (600, 600)
    pygame.display.set_mode(win, DOUBLEBUF | OPENGL)

    generate()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    to_mid()
                if event.key == pygame.K_LEFT:
                    to_left()
                if event.key == pygame.K_RIGHT:
                    to_right()
                if event.key == pygame.K_UP:
                    to_up()
                if event.key == pygame.K_DOWN:
                    to_down()
                if event.key == pygame.K_EQUALS:
                    thickness += 0.5
                if event.key == pygame.K_MINUS:
                    if thickness >= 1:
                        thickness -= 0.5
                if event.key == pygame.K_TAB:
                    bres = not bres
                    print('bresenham:', bres)

        draw_game()
