from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


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


def make_edges(vertices, zero):
    edges = ()
    for i in range(zero, zero + len(vertices)):
        if i < zero + len(vertices) - 1:
            edges += ((i, i + 1),)
        else:
            edges += ((zero, i),)
    print(vertices)
    print(edges)
    return edges


def build(edges, points):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(points[vertex])

    glEnd()
    glLineWidth(1)
