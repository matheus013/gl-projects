from OpenGL.GL import *

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
        return False, None
    texture_id = DataUtil.textures_id[type_texture]
    return True, texture_id


def build(edges, points, surfaces, type_texture=None):
    ref_texture = ((0, 1), (0, 0), (1, 0), (1, 1))
    if DataUtil.face_view:
        glBegin(GL_QUADS)
        texture_ok, texture_id = texture_init(type_texture)
        # print(texture_ok, texture_id)
        for surface in surfaces:
            x = 0
            for vertex in surface:
                x += 1
                index_texture = x - 1
                if texture_ok:
                    glTexCoord2f(ref_texture[index_texture][0], ref_texture[index_texture][1])
                else:
                    glColor3fv(DataUtil.colors[x])
                glVertex3fv(points[vertex])
        glEnd()
        # glutSwapBuffers()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(points[vertex])

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


def gen_texture_id(obj_name):
    filename = DataUtil.path_textures[obj_name]
    f = FileTexture(filename)
    texture_id = f.read_texture()
    return texture_id


def register_texture():
    obj_names = ['wall', 'ground0']
    for i in obj_names:
        DataUtil.textures_id[i] = gen_texture_id(i)
    print(DataUtil.textures_id)
