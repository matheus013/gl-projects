from OpenGL.GL import *
from OpenGL.raw.GLUT import glutSwapBuffers

from cg_final.constants import DataUtil
from cg_final.textures.gl_texture import FileTexture, RandomTexture


def valid_points(points, r, object_name):
    for i in points:
        if len(i) != r:
            print('Invalid point after build ' + object_name + ' p: ' + str(i))
            return
    # print('Build points from ' + object_name + ' is great!')
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
    # print('Build edges from ' + object_name + ' is great!')


def make_edges(vertices, zero):
    edges = ()
    for i in range(zero, zero + len(vertices)):
        if i < zero + len(vertices) - 1:
            edges += ((i, i + 1),)
        else:
            edges += ((zero, i),)
    return edges


def make_surface(vertices, zero):
    surface = ()
    for i in range(zero, zero + len(vertices)):
        surface += (i,)
    return (surface,)


def texture_init(type_texture):
    if type_texture is None:
        type_texture = "wall"
            # return

    fileName = DataUtil.path_textures[type_texture]
    texture = FileTexture(fileName)
    texture_id = glGenTextures(1)

    if texture is None:
        return

    glBindTexture(GL_TEXTURE_2D, texture_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)

    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

    glTexImage2D(GL_TEXTURE_2D, 0, 3, texture.width, texture.height, 0,
                 GL_RGB, GL_UNSIGNED_BYTE, texture.raw_reference)

    glEnable(GL_TEXTURE_2D)


def build(edges, points, surfaces, type_texture=None):
    ref_texture = ((0, 1), (0, 0), (1, 0), (1, 1))
    if DataUtil.face_view:
        glBegin(GL_QUADS)
        texture_init(type_texture)
        for surface in surfaces:
            x = 0
            for vertex in surface:
                x += 1
                index_texture = x - 1
                glColor3fv(DataUtil.colors[x])
                glVertex3fv(points[vertex])
                glTexCoord2f(ref_texture[index_texture][0], ref_texture[index_texture][1])
        glEnd()
        glutSwapBuffers()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(points[vertex])
            # print(vertex % 4)

    glEnd()
    glLineWidth(1)


def mid(a, b):
    return (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, (a[2] + b[2]) / 2


def quad(origin, end, h):
    return (
        origin,
        (origin[0], origin[1] + h, origin[2]),
        (end[0], end[1] + h, end[2]),
        end,
    )
