import numpy as np
from OpenGL.GL import *

from cg_final.constants import DataUtil
from cg_final.textures.gl_texture import FileTexture


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
    no_tail = ()
    for i in range(zero, zero + len(vertices)):
        if i < zero + len(vertices) - 1:
            edges += ((i, i + 1),)
            no_tail += ((i - zero, i + 1 - zero),)
        else:
            edges += ((zero, i),)
            no_tail += ((0, i - zero),)
    return edges, no_tail


def make_surface(vertices, zero):
    surface = ()
    no_tail = ()
    for i in range(zero, zero + len(vertices)):
        surface += (i,)
        no_tail += (i - zero,)
    return (surface,), (no_tail,)


def texture_init(type_texture):
    if type_texture is None:
        return False, None
    texture_id = DataUtil.textures_id[type_texture]
    return True, texture_id


def draw(obj):
    draw_object(obj, DataUtil.textures_id[obj.type_name], DataUtil.face_view)


def draw_object(obj, texture, wire_frame=False):
    edges, points, surfaces = obj.values()
    if texture is not None and not wire_frame:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, texture)  # target, texture
        build(edges, points, surfaces, texture)
        glDisable(GL_TEXTURE_2D)
    else:
        build(edges, points, surfaces)


def build(edges, points, surfaces, type_texture=None, c=None):
    # ref_texture = ((0, 1), (0, 0), (1, 0), (1, 1))
    # glBegin(GL_LINES)
    for face in surfaces:
        ref_texture = get_tex(face)
        glBegin(GL_QUADS)
        for t, vertex in enumerate(face):
            if type_texture is not None:
                # print(type_texture)
                if c is not None:
                    glColor3fv(c)
                glTexCoord2fv(ref_texture[t])
            glVertex3fv(points[vertex])
        glEnd()
    # glEnd()


def get_tex(face, from_obj=None):
    def dist(u, v):
        diff = np.asarray(u) - np.asarray(v)
        return np.linalg.norm(diff)

    if from_obj == 'door':
        f = list(face[1:])
        f.append(face[0])
        face = tuple(f)

    v1, v2, v3, v4 = face
    s1 = 0
    s2 = dist(v1, v2)
    t1 = 0
    t2 = dist(v2, v3)
    tc = [(s1, t1), (s2, t1), (s2, t2), (s1, t2)]

    return tc


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
    for i in DataUtil.path_textures:
        if DataUtil.path_textures[i] is not None:
            print('loading texture', i, DataUtil.path_textures[i])
            DataUtil.textures_id[i] = gen_texture_id(i)
