import math

from OpenGL.GL import *

from cg_final.constants import *
from cg_final.support import valid_points, valid_edges, make_edges, make_surface, quad, mid, build, draw_object


class DrawableObject:
    def __init__(self, surfaces, vertices, edges, type_name):
        self.type_name = type_name
        self.edges = edges
        self.surface = surfaces
        self.vertices = vertices

    def values(self):
        return self.edges, self.vertices, self.surface


def config_door(base_left, base_right, ref, index):
    print('configure door: ', ref, index)
    door_conf[ref][index].base_left = base_left
    door_conf[ref][index].base_right = base_right


def build_arc_wall(arc_center, top_origin, top_end, radius, x_or_z, h, parent=None, t=''):
    vertices = (
        top_origin,
        top_end
    )

    for i in range(180, 360):
        rad = math.pi * i / 180
        x = arc_center[0] + radius * math.cos(rad) if x_or_z else arc_center[0]
        y = arc_center[1] + radius * math.sin(rad)
        z = arc_center[2] if x_or_z else arc_center[2] + radius * math.cos(rad)
        vertices += ((x, y, z),)

    with_tail_edges, no_tail_edges = make_edges(vertices, len(DataUtil.vertices))
    with_tail_surfaces, no_tail_surfaces = make_surface(vertices, len(DataUtil.vertices))

    DataUtil.edges += with_tail_edges
    DataUtil.surfaces += with_tail_surfaces
    DataUtil.vertices += vertices

    if parent is not None:
        parent.vertices += vertices
        parent.edges += no_tail_edges
        parent.surfaces = no_tail_surfaces
        return parent

    return DrawableObject(no_tail_surfaces, vertices, no_tail_edges, type_name=t)


def build_half_circle_xy(x_center, y_center, z_center, radius):
    glBegin(GL_LINE_STRIP)
    for i in range(180, 360):
        rad = math.pi * i / 180
        x = x_center + radius * math.cos(rad)
        y = y_center + radius * math.sin(rad)
        glVertex(x, y, z_center)
    glEnd()


def build_half_circle_yz(x_center, y_center, z_center, radius):
    glBegin(GL_LINE_STRIP)
    for i in range(180, 360):
        rad = math.pi * i / 180
        z = z_center + radius * math.cos(rad)
        y = y_center + radius * math.sin(rad)
        glVertex(x_center, y, z)
    glEnd()


def build_pillar(x_center, y_center, z_center, h, d, t='wall'):
    vertices = (
        # base
        (x_center - d / 2, y_center, z_center + d / 2),
        (x_center + d / 2, y_center, z_center + d / 2),
        (x_center + d / 2, y_center, z_center - d / 2),
        (x_center - d / 2, y_center, z_center - d / 2),

    )
    obj = build_wall(vertices[0], vertices[1], h, type_name=t)
    DataUtil.objects.append(obj)
    obj = build_wall(vertices[1], vertices[2], h, type_name=t)
    DataUtil.objects.append(obj)
    obj = build_wall(vertices[2], vertices[3], h, type_name=t)
    DataUtil.objects.append(obj)
    obj = build_wall(vertices[0], vertices[3], h, type_name=t)
    DataUtil.objects.append(obj)
    return obj


def build_wall(origin, end, h, notify=False, type_name="wall", parent=None):
    vertices = quad(origin, end, h)
    if notify:
        print('wall', vertices)

    with_tail_edges, no_tail_edges = make_edges(vertices, len(DataUtil.vertices))
    with_tail_surfaces, no_tail_surfaces = make_surface(vertices, len(DataUtil.vertices))

    DataUtil.edges += with_tail_edges
    DataUtil.surfaces += with_tail_surfaces
    DataUtil.vertices += vertices

    valid_points(DataUtil.vertices, 3, 'wall')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'wall')

    if parent is not None:
        parent.vertices += vertices
        parent.edges += no_tail_edges
        parent.surfaces = no_tail_surfaces
        return parent

    return DrawableObject(no_tail_surfaces, vertices, no_tail_edges, type_name)


def build_plain(origin, end, d, parent=None):
    vertices = (
        origin,
        (origin[0], origin[1], origin[2] + d),
        (end[0], end[1], end[2] + d),
        end,
    )
    with_tail_edges, no_tail_edges = make_edges(vertices, len(DataUtil.vertices))
    with_tail_surfaces, no_tail_surfaces = make_surface(vertices, len(DataUtil.vertices))

    DataUtil.edges += with_tail_edges
    DataUtil.surfaces += with_tail_surfaces
    DataUtil.vertices += vertices

    valid_points(DataUtil.vertices, 3, 'plain')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'plain')

    if parent is not None:
        parent.vertices += vertices
        parent.edges += no_tail_edges
        parent.surfaces = no_tail_surfaces
        return parent

    return DrawableObject(no_tail_surfaces, vertices, no_tail_edges, '')


def build_front(x_origin, y_origin, z_origin):
    front = []
    obj = build_wall((x_origin, y_origin, z_origin), (x_origin + (tower_width / 3), y_origin, z_origin),
                     height, type_name='wall')
    front.append(obj)
    # door 1
    obj = build_wall((x_origin + tower_width / 3, y_origin + door_height[0], z_origin),
                     (x_origin + tower_width / 3 + door_width[0], y_origin + door_height[0], z_origin),
                     height - door_height[0], type_name='wall')
    front.append(obj)
    config_door((x_origin + tower_width / 3, y_origin, z_origin),
                (x_origin + tower_width / 3 + door_width[0], y_origin, z_origin), 'front', 0)

    obj = build_wall((x_origin + (tower_width / 3) + door_width[0], y_origin, z_origin),
                     (x_origin + 4 * (tower_width / 3), y_origin, z_origin), height, type_name='wall')
    front.append(obj)
    # door 2
    obj = build_wall((x_origin + 4 * (tower_width / 3), y_origin + door_height[1], z_origin),
                     (x_origin + 4 * (tower_width / 3) + door_width[1], y_origin + door_height[1], z_origin),
                     height - door_height[1], type_name='wall')
    front.append(obj)
    config_door((x_origin + 4 * (tower_width / 3), y_origin, z_origin),
                (x_origin + 4 * (tower_width / 3) + door_width[1], y_origin, z_origin), 'front', 1)

    obj = build_wall((x_origin + 4 * (tower_width / 3) + door_width[1], y_origin, z_origin),
                     (x_origin + width / 2 - door_width[2] / 2, y_origin, z_origin),
                     height, type_name='wall')
    front.append(obj)
    # door 3
    obj = build_wall((x_origin + width / 2 + door_width[2] / 2, y_origin + door_height[2], z_origin),
                     (x_origin + width / 2 - door_width[2] / 2, y_origin + door_height[2], z_origin),
                     height - door_height[2], type_name='wall')
    front.append(obj)
    config_door((x_origin + width / 2 - door_width[2] / 2, y_origin, z_origin),
                (x_origin + width / 2 + door_width[2] / 2, y_origin, z_origin),
                'front', 2)

    obj = build_wall((x_origin + width / 2 + door_width[2] / 2, y_origin, z_origin),
                     (x_origin + width - 4 * (tower_width / 3) - door_width[1], y_origin, z_origin), height,
                     type_name='wall')
    front.append(obj)
    # door 2
    obj = build_wall((x_origin + width - 4 * (tower_width / 3) - door_width[1], y_origin + door_height[1], z_origin),
                     (x_origin + width - 4 * (tower_width / 3), y_origin + door_height[1], z_origin),
                     height - door_height[1], type_name='wall')
    front.append(obj)
    config_door((x_origin + width - 4 * (tower_width / 3) - door_width[1], y_origin, z_origin),
                (x_origin + width - 4 * (tower_width / 3), y_origin, z_origin), 'front', 3)

    obj = build_wall((x_origin + width - 4 * (tower_width / 3), y_origin, z_origin),
                     (x_origin + width - (tower_width / 3) - door_width[0], y_origin, z_origin),
                     height, type_name='wall')
    front.append(obj)
    # door 1
    obj = build_wall((x_origin + width - (tower_width / 3), y_origin + door_height[0], z_origin),
                     (x_origin + width - (tower_width / 3) - door_width[0], y_origin + door_height[0], z_origin),
                     height - door_height[0], type_name='wall')
    front.append(obj)
    config_door((x_origin + width - (tower_width / 3) - door_width[0], y_origin, z_origin),
                (x_origin + width - (tower_width / 3), y_origin, z_origin),
                'front', 4)

    obj = build_wall((x_origin + width - (tower_width / 3), y_origin, z_origin),
                     (x_origin + width, y_origin, z_origin),
                     height, type_name='wall')
    front.append(obj)
    return front


def build_tower(x_origin, y_origin, z_origin):
    tower = []
    # left
    left = build_wall((x_origin, y_origin + height, z_origin), (x_origin + tower_width, y_origin + height, z_origin),
                      tower_height, type_name='wall')
    tower.append(left)

    left = build_wall((x_origin, y_origin + height, z_origin), (x_origin, y_origin + height, z_origin + tower_width),
                      tower_height, type_name='wall')
    tower.append(left)

    left = build_wall((x_origin + tower_width, y_origin + height, z_origin),
                      (x_origin + tower_width, y_origin + height, z_origin + tower_width),
                      tower_height, type_name='wall')
    tower.append(left)

    left = build_wall((x_origin, y_origin + height, z_origin + tower_width),
                      (x_origin + tower_width, y_origin + height, z_origin + tower_width),
                      tower_height, type_name='wall')
    tower.append(left)

    # right
    right = build_wall((x_origin + width, y_origin + height, z_origin),
                       (x_origin + width - tower_width, y_origin + height, z_origin),
                       tower_height, type_name='wall')
    tower.append(right)

    right = build_wall((x_origin + width, y_origin + height, z_origin),
                       (x_origin + width, y_origin + height, z_origin + tower_width),
                       tower_height, type_name='wall')
    tower.append(right)

    right = build_wall((x_origin + width - tower_width, y_origin + height, z_origin),
                       (x_origin + width - tower_width, y_origin + height, z_origin + tower_width),
                       tower_height, type_name='wall')
    tower.append(right)

    right = build_wall((x_origin + width, y_origin + height, z_origin + tower_width),
                       (x_origin + width - tower_width, y_origin + height, z_origin + tower_width),
                       tower_height, type_name='wall')
    tower.append(right)
    return tower


def build_right(x_origin, y_origin, z_origin):
    right = []
    obj = build_wall((x_origin + width, y_origin, z_origin),
                     (x_origin + width, y_origin, z_origin + depth / 3 - door_width[0]), height,
                     type_name='wall')
    right.append(obj)
    # porta lateral frente
    obj = build_wall((x_origin + width, y_origin + door_height[0], z_origin + depth / 3),
                     (x_origin + width, y_origin + door_height[0], z_origin + depth / 3 - door_width[0]),
                     height - door_height[0], type_name='wall')
    right.append(obj)
    config_door((x_origin + width, y_origin, z_origin + depth / 3 - door_width[0]),
                (x_origin + width, y_origin, z_origin + depth / 3), 'right', 0)

    obj = build_wall((x_origin + width, y_origin, z_origin + depth / 3),
                     (x_origin + width, y_origin, z_origin + 2 * depth / 3 - door_width[0]), height,
                     type_name='wall')
    right.append(obj)

    # porta lateral meio
    obj = build_wall((x_origin + width, y_origin + door_height[0], z_origin + 2 * depth / 3 - door_width[0]),
                     (x_origin + width, y_origin + door_height[0], z_origin + 2 * depth / 3),
                     height - door_height[0],
                     type_name='wall')
    right.append(obj)
    config_door((x_origin + width, y_origin, z_origin + 2 * depth / 3 - door_width[0]),
                (x_origin + width, y_origin, z_origin + 2 * depth / 3), 'right', 1)

    obj = build_wall((x_origin + width, y_origin, z_origin + 2 * depth / 3),
                     (x_origin + width, y_origin, z_origin + depth - 3 * door_width[0]), height,
                     type_name='wall')
    right.append(obj)

    # porta lateral mais fundo
    obj = build_wall((x_origin + width, y_origin + door_height[0], z_origin + depth - 3 * door_width[0]),
                     (
                         x_origin + width, y_origin + door_height[0],
                         z_origin + depth - 3 * door_width[0] + door_width[0]),
                     height - door_height[0], type_name='wall')
    right.append(obj)
    config_door((x_origin + width, y_origin, z_origin + depth - 3 * door_width[0]),
                (x_origin + width, y_origin, z_origin + depth - 3 * door_width[0] + door_width[0]),
                'right', 2)

    obj = build_wall((x_origin + width, y_origin, z_origin + depth - 3 * door_width[0] + door_width[0]),
                     (x_origin + width, y_origin, z_origin + depth), height, type_name='wall')
    right.append(obj)
    return right


def build_back(x_origin, y_origin, z_origin):
    obj = build_wall((x_origin, y_origin, z_origin + depth), (x_origin + width, y_origin, z_origin + depth), height,
                     type_name='wall')
    return obj


def build_left(x_origin, y_origin, z_origin):
    left = []
    obj = build_wall((x_origin, y_origin, z_origin), (x_origin, y_origin, z_origin + depth * 0.4), height,
                     type_name='wall')
    left.append(obj)
    # attachment begin
    obj = build_wall((x_origin, y_origin, z_origin + depth * 0.4),
                     (x_origin - attachment_width, y_origin, z_origin + depth * 0.4), height,
                     type_name='wall')
    left.append(obj)
    obj = build_wall((x_origin - attachment_width, y_origin, z_origin + depth * 0.4), (
        x_origin - attachment_width, y_origin, z_origin + depth * 0.4 + attachment_depth), height,
                     type_name='wall')
    left.append(obj)

    obj = build_wall((x_origin - attachment_width, y_origin, z_origin + depth * 0.4 + attachment_depth),
                     (x_origin, y_origin, z_origin + depth * 0.4 + attachment_depth), height,
                     type_name='wall')
    left.append(obj)
    # attachment end
    obj = build_wall((x_origin, y_origin, z_origin + depth * 0.4 + attachment_depth),
                     (x_origin, y_origin, z_origin + depth * (2 / 3) - door_width[0]), height,
                     type_name='wall')
    left.append(obj)

    # door
    obj = build_wall((x_origin, y_origin + door_height[0], z_origin + depth * (2 / 3)),
                     (x_origin, y_origin + door_height[0], z_origin + depth * (2 / 3) - door_width[0]),
                     height - door_height[0],
                     type_name='wall')
    left.append(obj)
    config_door((x_origin, y_origin, z_origin + depth * (2 / 3)),
                (x_origin, y_origin, z_origin + depth * (2 / 3) - door_width[0]), 'left', 0)

    obj = build_wall((x_origin, y_origin, z_origin + depth * (2 / 3)), (x_origin, y_origin, z_origin + depth), height,
                     type_name='wall')
    left.append(obj)

    attachment_origin = (x_origin - attachment_width, y_origin, z_origin + depth * 0.4)
    attachment_center = (math.fabs(attachment_width / 2), math.fabs(y_origin), math.fabs(attachment_depth / 2))
    if ground:
        build_ground(attachment_center, attachment_origin, 3)
    return left


def build_top(x_origin, y_origin, z_origin):
    top = []
    vertices = (
        (x_origin + width / 2, y_origin + height + tower_height * 0.2, z_origin),
        (x_origin + width / 2, y_origin + height + tower_height * 0.2, z_origin + depth),
        (x_origin + width, y_origin + height, z_origin + depth),
        (x_origin + width, y_origin + height, z_origin),
    )
    with_tail_edges, no_tail_edges = make_edges(vertices, len(DataUtil.vertices))
    with_tail_surfaces, no_tail_surfaces = make_surface(vertices, len(DataUtil.vertices))

    DataUtil.edges += with_tail_edges
    DataUtil.surfaces += with_tail_surfaces
    DataUtil.vertices += vertices
    top.append(DrawableObject(no_tail_surfaces, vertices, no_tail_edges, 'top'))

    vertices = (
        (x_origin + width / 2, y_origin + height + tower_height * 0.2, z_origin),
        (x_origin + width / 2, y_origin + height + tower_height * 0.2, z_origin + depth),
        (x_origin, y_origin + height, z_origin + depth),
        (x_origin, y_origin + height, z_origin),
    )
    with_tail_edges, no_tail_edges = make_edges(vertices, len(DataUtil.vertices))
    with_tail_surfaces, no_tail_surfaces = make_surface(vertices, len(DataUtil.vertices))

    DataUtil.edges += with_tail_edges
    DataUtil.surfaces += with_tail_surfaces
    DataUtil.vertices += vertices

    top.append(DrawableObject(no_tail_surfaces, vertices, no_tail_edges, 'top'))

    valid_points(DataUtil.vertices, 3, 'top')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'top')
    return top


def build_ground(center, origin, delta):
    base = (
        (origin[0] - delta, origin[1], origin[2] - delta),
        (origin[0] - delta, origin[1], origin[2] + delta + 2 * center[2]),
        (origin[0] + delta + 2 * center[0], origin[1], origin[2] + delta + 2 * center[2]),
        (origin[0] + 2 * center[0] + delta, origin[1], origin[2] - delta),
    )
    obj = build_wall(base[0], base[1], delta, type_name='sub_ground')
    DataUtil.objects.append(obj)

    obj = build_wall(base[1], base[2], delta, type_name='sub_ground')
    DataUtil.objects.append(obj)

    obj = build_wall(base[2], base[3], delta, type_name='sub_ground')
    DataUtil.objects.append(obj)

    obj = build_wall(base[0], base[3], delta, type_name='sub_ground')
    DataUtil.objects.append(obj)

    plain_ground = build_plain(base[0], base[3], 2 * (center[2] + delta))
    plain_ground.type_name = 'ground0'

    DataUtil.objects.append(plain_ground)


def build_door(config, key):
    center = mid(config.base_left, config.base_right)

    # left
    glPushMatrix()

    left_vertices = quad(config.base_left, center, config.height)

    with_tail_edges, no_tail_edges = make_edges(left_vertices, 0)
    with_tail_surfaces, no_tail_surfaces = make_surface(left_vertices, 0)

    left_edges = with_tail_edges
    left_surfaces = with_tail_surfaces

    glTranslate(config.base_left[0], config.base_left[1], config.base_left[2])
    glRotatef(config.alpha, 0, 1, 0)
    glTranslate(-config.base_left[0], -config.base_left[1], -config.base_left[2])

    draw_object(DrawableObject(left_surfaces, left_vertices, left_edges, 'door'), DataUtil.textures_id['door'])

    # build(left_edges, left_vertices, left_surfaces)

    if config.run:
        if config.state:
            config.alpha += delta_rotate
            if config.alpha >= limit_door[1] or config.alpha <= limit_door[0]:
                door_conf[key[0]][key[1]].run_reverse()
                door_conf[key[0]][key[1]].state_reverse()
        else:
            config.alpha -= delta_rotate
            if config.alpha >= limit_door[1] or config.alpha <= limit_door[0]:
                door_conf[key[0]][key[1]].run_reverse()
                door_conf[key[0]][key[1]].state_reverse()

    glPopMatrix()

    # right
    glPushMatrix()
    right_vertices = quad(config.base_right, center, config.height)

    with_tail_edges, no_tail_edges = make_edges(right_vertices, 0)
    with_tail_surfaces, no_tail_surfaces = make_surface(right_vertices, 0)

    right_edges = with_tail_edges
    right_surfaces = with_tail_surfaces

    glTranslate(config.base_right[0], config.base_right[1], config.base_right[2])
    glRotatef(-config.alpha, 0, 1, 0)
    glTranslate(-config.base_right[0], -config.base_right[1], -config.base_right[2])

    draw_object(DrawableObject(right_surfaces, right_vertices, right_edges, 'door'), DataUtil.textures_id['door'])
    # build(right_edges, right_vertices, right_surfaces)
    glPopMatrix()


def build_block(center, l, h, d, notify=False, type_name='ground1', sides='wall'):
    # base plain
    c = list(center)

    c[1] = c[1] - h / 2
    # print(c)
    obj = build_block_plain(c, l, d, notify, t=type_name)
    DataUtil.objects.append(obj)
    base = obj.vertices
    # top plain
    c = list(center)
    c[1] = c[1] + h / 2
    # print(c)
    obj = build_block_plain(c, l, d, notify, t=type_name)
    DataUtil.objects.append(obj)

    obj = build_wall(base[0], base[1], h, notify, type_name=sides)
    DataUtil.objects.append(obj)
    obj = build_wall(base[1], base[2], h, notify, type_name=sides)
    DataUtil.objects.append(obj)
    obj = build_wall(base[2], base[3], h, notify, type_name=sides)
    DataUtil.objects.append(obj)
    obj = build_wall(base[0], base[3], h, notify, type_name=sides)
    DataUtil.objects.append(obj)
    return obj


def build_block_plain(center, l, d, notify=False, parent=None, t='ground1'):
    vertices = (
        (center[0] - l / 2, center[1], center[2] - d / 2),
        (center[0] - l / 2, center[1], center[2] + d / 2),
        (center[0] + l / 2, center[1], center[2] + d / 2),
        (center[0] + l / 2, center[1], center[2] - d / 2),
    )

    if notify:
        print('plain', vertices)

    with_tail_edges, no_tail_edges = make_edges(vertices, len(DataUtil.vertices))
    with_tail_surfaces, no_tail_surfaces = make_surface(vertices, len(DataUtil.vertices))

    DataUtil.edges += with_tail_edges
    DataUtil.surfaces += with_tail_surfaces
    DataUtil.vertices += vertices

    valid_points(DataUtil.vertices, 3, 'plain')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'plain')
    if parent is not None:
        parent.vertices += vertices
        parent.edges += no_tail_edges
        parent.surfaces = no_tail_surfaces
        return parent

    return DrawableObject(no_tail_surfaces, vertices, no_tail_edges, t)


def build_any_plain(vertices, notify=False, parent=None, t='table'):
    if notify:
        print('plain', vertices)

    with_tail_edges, no_tail_edges = make_edges(vertices, len(DataUtil.vertices))
    with_tail_surfaces, no_tail_surfaces = make_surface(vertices, len(DataUtil.vertices))

    DataUtil.edges += with_tail_edges
    DataUtil.surfaces += with_tail_surfaces
    DataUtil.vertices += vertices

    valid_points(DataUtil.vertices, 3, 'plain')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'plain')
    if parent is not None:
        parent.vertices += vertices
        parent.edges += no_tail_edges
        parent.surfaces = no_tail_surfaces
        return parent
    return DrawableObject(no_tail_surfaces, vertices, no_tail_edges, t)


def build_bench(center, l, h, d):
    pass


def build_chair(left, right, h):
    accent_height = h * 0.08
    foot_height = h / 2 - accent_height
    backrest = h - foot_height - accent_height

    l = math.fabs(left[0] - right[0])
    foot_width = l * 0.15
    bases = (
        left,
        right,
        (right[0], right[1], right[2] - l),
        (left[0], left[1], left[2] - l)

    )
    c = mid(bases[0], bases[2])

    for i in bases:
        build_pillar(i[0], i[1] - foot_height, i[2], foot_height, foot_width, t='chair_wood')

    build_block(c, l * 1.2, accent_height, l * 1.2, type_name='chair', sides='chair_wood')

    obj = build_wall(left, right, backrest, type_name='chair')
    DataUtil.objects.append(obj)


def build_arcs(ref_x, ref_y, ref_z):
    # center front arc
    build_half_circle_xy(ref_x + width / 2, ref_y + height + ((width - 3 * tower_width) / 2) * 1.2,
                         ref_z + depth * 0.4 + attachment_depth,
                         (width - 3 * tower_width) / 2)

    const_x_arc = ref_x + tower_width
    const_y_arc = ref_y + height + ((width - 3 * tower_width) / 2)
    const_r_arc = depth * (1 / 15) - width / 40
    const_r_arc2 = (depth * 0.4 + attachment_depth - depth * (6 / 15)) / 2 - width / 40

    points_arc = (
        (const_x_arc, const_y_arc * 1.2, ref_z + depth * (3 / 15), const_r_arc),
        (const_x_arc, const_y_arc * 1.2, ref_z + depth * (5 / 15), const_r_arc),
        (const_x_arc, const_y_arc * 1.2, ref_z + depth * (6 / 15) + const_r_arc2 + width / 40, const_r_arc2),
    )

    for i in points_arc:
        build_half_circle_yz(i[0], i[1], i[2], i[3])

    const_x_arc = ref_x + width - tower_width

    points_arc = (
        (const_x_arc, const_y_arc * 1.2, ref_z + depth * (3 / 15), const_r_arc),
        (const_x_arc, const_y_arc * 1.2, ref_z + depth * (5 / 15), const_r_arc),
        (const_x_arc, const_y_arc * 1.2, ref_z + depth * (6 / 15) + const_r_arc2 + width / 40, const_r_arc2),
    )

    for i in points_arc:
        build_half_circle_yz(i[0], i[1], i[2], i[3])


def build_main_table(center, l, d, h):
    obj = build_block_plain(center, l * 0.8, d * 0.8)
    DataUtil.objects.append(obj)
    base = obj.vertices
    new_center = (center[0], center[1] + h, center[2])
    obj = build_block_plain(new_center, l, d, t='top_table')
    DataUtil.objects.append(obj)

    top = obj.vertices

    sides = []
    for i in range(len(base) - 1):
        sides.append((
            (base[i],
             base[i + 1],
             top[i + 1],
             top[i])
        ))
    sides.append(
        (base[3],
         base[0],
         top[0],
         top[3])
    )
    for i in sides:
        obj = build_any_plain(i)
        DataUtil.objects.append(obj)


def draw_cylinder(c, r, h):
    angle_step = 0.1
    angle = 0.0

    glBegin(GL_QUAD_STRIP)

    while angle < 2 * math.pi:
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        glVertex3f(c[0] + x, c[1] + h, c[1] + y)
        glVertex3f(c[1] + x, c[1], c[1] + y)
        angle += angle_step

    glVertex3f(c[1] + r, c[1] + h, c[1])
    glVertex3f(c[1] + r, c[1], c[1])

    glEnd()

    glBegin(GL_POLYGON)
    angle = 0.0
    while angle < 2 * math.pi:
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        glVertex3f(c[1] + x, c[1] + h, c[1] + y)
        angle += angle_step
    glVertex3f(c[1] + r, c[1] + h, c[1])
    glEnd()


def build_candle(center, r, h):
    dh = (
        h * 0.4,
        h * 0.05,
        h * 0.4,
        h * 0.05,
        h * 0.1,
    )
    c = (
        center,
        (center[0], center[1], center[2]),
        (center[0], center[1], center[2]),
        (center[0], center[1], center[2]),
        (center[0], center[1], center[2])
    )
    current_h = 0.0
    for i in range(5):
        current_radius = r if i % 2 == 0 else r * 1.1
        p = list(c[i])
        p[1] += current_h
        current_h += dh[i]
        draw_cylinder(p, current_radius, dh[i])

    pass


def build_bible_support(center, l, d, h):
    base = (
        (center[0] - l / 2, center[1], center[2] - d / 2),
        (center[0] - l / 2, center[1], center[2] + d / 2),
        (center[0] + l / 2, center[1], center[2] + d / 2),
        (center[0] + l / 2, center[1], center[2] - d / 2),
    )

    top = (
        (center[0] - l / 2, center[1] + h, center[2] - d / 2),
        (center[0] - l / 2, center[1] + h * 0.4, center[2] + d / 2),
        (center[0] + l / 2, center[1] + h * 0.4, center[2] + d / 2),
        (center[0] + l / 2, center[1] + h, center[2] - d / 2),
    )
    left = (base[0], base[1], top[1], top[0])
    right = (base[2], base[3], top[3], top[2])

    obj = build_any_plain(left, t='gold')
    DataUtil.objects.append(obj)

    obj = build_any_plain(right, t='gold')
    DataUtil.objects.append(obj)

    front = (
        (center[0] - l / 2, center[1], center[2] + d / 2),
        (center[0] + l / 2, center[1], center[2] + d / 2),
        (center[0] + l / 2, center[1] + h * 0.5, center[2] + d / 2),
        (center[0] - l / 2, center[1] + h * 0.5, center[2] + d / 2),
    )

    obj = build_any_plain(front, t='gold')
    DataUtil.objects.append(obj)

    upper = (
        (center[0] - (l / 2) * 1.2, center[1] + h, center[2] - d / 2),
        (center[0] - (l / 2) * 1.2, center[1] + h * 0.4, center[2] + d / 2),
        (center[0] + (l / 2) * 1.2, center[1] + h * 0.4, center[2] + d / 2),
        (center[0] + (l / 2) * 1.2, center[1] + h, center[2] - d / 2),
    )

    obj = build_any_plain(upper, t='gold')
    DataUtil.objects.append(obj)
    return top


def build_bible(center, plain, l, d, h):
    build_any_plain(plain)
    upper_plain = (
        (plain[0][0], plain[0][1] + h, plain[0][2]),
        (plain[1][0], plain[1][1] + h, plain[1][2]),
        (plain[2][0], plain[2][1] + h, plain[2][2]),
        (plain[3][0], plain[3][1] + h, plain[3][2]),
    )
    build_any_plain(upper_plain)
    side_plain = (
        plain[0],
        plain[1],
        upper_plain[1],
        upper_plain[0]
    )
    build_any_plain(side_plain)
    plain[3]
    d = 0.05

    inter_plain = (
        (plain[2][0] - d, plain[2][1], plain[2][2] - d),
        (plain[3][0] - d, plain[3][1], plain[3][2] + d),
        (upper_plain[3][0] - d, upper_plain[3][1], upper_plain[3][2] + d),
        (upper_plain[2][0] - d, upper_plain[2][1], upper_plain[2][2] - d),
    )

    build_any_plain(inter_plain)
    # inter_plain = (
    #     (plain[2][0] - d , plain[2][1], plain[2][2] - d),
    #     (plain[3][0] - d , plain[3][1], plain[3][2] + d),
    #     (upper_plain[3][0] - d, upper_plain[3][1], upper_plain[3][2] + d),
    #     (upper_plain[2][0] - d, upper_plain[2][1], upper_plain[2][2] - d),
    # )
    pass


def build_internal(x, y, z):
    build_pillar(x + tower_width, y, z + depth * (2 / 15), height, width / 20)
    build_pillar(x + tower_width, y, z + depth * (4 / 15), height, width / 20)
    build_pillar(x + tower_width, y, z + depth * (6 / 15), height, width / 20)

    build_pillar(x + width - tower_width, y, z + depth * (2 / 15), height, width / 20)
    build_pillar(x + width - tower_width, y, z + depth * (4 / 15), height, width / 20)
    build_pillar(x + width - tower_width, y, z + depth * (6 / 15), height, width / 20)

    obj = build_wall((x, y, z + depth * 0.4 + attachment_depth),
                     (x + tower_width, y, z + depth * 0.4 + attachment_depth),
                     height)
    DataUtil.objects.append(obj)
    pillar_width_altar = width / 12
    # front pillar
    build_pillar(x + tower_width, y, z + depth * 0.4 + attachment_depth, height, pillar_width_altar)
    build_pillar(x + width - tower_width, y, z + depth * 0.4 + attachment_depth, height, pillar_width_altar)

    obj = build_wall((x + width - tower_width, y, z + depth * 0.4 + attachment_depth),
                     (x + width, y, z + depth * 0.4 + attachment_depth),
                     height)
    DataUtil.objects.append(obj)

    obj = build_wall((x + tower_width * 1.5, y, z + depth * 0.4 + attachment_depth),
                     (x + tower_width, y, z + depth * 0.4 + attachment_depth),
                     height)
    DataUtil.objects.append(obj)

    obj = build_wall((x + width - tower_width * 1.5, y, z + depth * 0.4 + attachment_depth),
                     (x + width, y, z + depth * 0.4 + attachment_depth),
                     height)
    DataUtil.objects.append(obj)
    # internal wall under tower
    # ->right
    obj = build_wall((x + width - tower_width, y, z),
                     (x + width - tower_width, y, z + depth * (2 / 15)), height)
    DataUtil.objects.append(obj)
    # ->left
    obj = build_wall((x + tower_width * 0.7, y, z),
                     (x + tower_width * 0.7, y, z + depth * (2 / 15)), height)
    DataUtil.objects.append(obj)
    obj = build_wall((x + tower_width * 0.7, y, z + depth * (2 / 15)),
                     (x + tower_width, y, z + depth * (2 / 15)), height)
    DataUtil.objects.append(obj)
    obj = build_wall((x + tower_width, y, z + depth * (2 / 15)),
                     (x + tower_width, y, z + depth * (4 / 45)), height)
    DataUtil.objects.append(obj)
    obj = build_wall((x + tower_width, y, z + depth * (4 / 45)),
                     (x + tower_width - tower_width * 0.25, y, z + depth * (4 / 45)), height)
    DataUtil.objects.append(obj)
    obj = build_wall((x + tower_width - tower_width * 0.25, y, z + depth * (4 / 45)),
                     (x + tower_width - tower_width * 0.25, y, z + depth * (2 / 45)), height)
    DataUtil.objects.append(obj)
    obj = build_wall((x + tower_width - tower_width * 0.25, y, z + depth * (2 / 45)),
                     (x + tower_width, y, z + depth * (2 / 45)), height)
    DataUtil.objects.append(obj)
    obj = build_wall((x + tower_width, y, z + depth * (2 / 45)),
                     (x + tower_width, y, z), height)
    DataUtil.objects.append(obj)
    # altar
    # altar side wall(left)
    x_ref = x + tower_width
    d_height_ref = height * 0.6
    obj = build_wall((x_ref, y, z + depth * 0.4 + attachment_depth),
                     (x_ref, y, z + depth * 0.4 + attachment_depth * 1.2), height)
    DataUtil.objects.append(obj)

    obj = build_wall((x_ref, y + d_height_ref, z + depth * 0.4 + attachment_depth * 1.2),
                     (x_ref, y + d_height_ref, z + depth * 0.4 + attachment_depth * 1.2 + door_width[1]),
                     height - d_height_ref)
    DataUtil.objects.append(obj)
    obj = build_wall((x_ref, y, z + depth * 0.4 + attachment_depth * 1.2 + door_width[1]),
                     (x_ref, y, z + depth * 0.95), height)
    DataUtil.objects.append(obj)
    # altar side wall(right)
    x_ref = x + width - tower_width
    obj = build_wall((x_ref, y, z + depth * 0.4 + attachment_depth),
                     (x_ref, y, z + depth * 0.4 + attachment_depth * 1.2), height)
    DataUtil.objects.append(obj)

    obj = build_wall((x_ref, y + d_height_ref, z + depth * 0.4 + attachment_depth * 1.2),
                     (x_ref, y + d_height_ref, z + depth * 0.4 + attachment_depth * 1.2 + door_width[1]),
                     height - d_height_ref)
    DataUtil.objects.append(obj)
    obj = build_wall((x_ref, y, z + depth * 0.4 + attachment_depth * 1.2 + door_width[1]),
                     (x_ref, y, z + depth * 0.95), height)
    DataUtil.objects.append(obj)
    # base block
    block_height = height / 10
    center_block_master = (x + width / 2, y + block_height / 2,
                           z + (depth * 0.4 + attachment_depth + depth) / 2)
    center_block_front = (x + tower_width + pillar_width_altar, y + block_height / 2,
                          z + depth * 0.4 + attachment_depth + pillar_width_altar / 4)
    center_block_sides = (x + tower_width + pillar_width_altar / 4, y + block_height / 2,
                          (z + depth * 0.4 + attachment_depth * 1.2 + door_width[1] + z + depth * 0.95) / 2)

    build_block(center_block_front, pillar_width_altar * 2, block_height, pillar_width_altar / 2)
    center_block_front = (x + width - tower_width - pillar_width_altar, y + block_height / 2,
                          z + depth * 0.4 + attachment_depth + pillar_width_altar / 4)
    build_block(center_block_front, pillar_width_altar * 2, block_height, pillar_width_altar / 2)

    altar_depth = depth - depth * 0.4 - attachment_depth - pillar_width_altar
    altar_width = width - 2 * tower_width - pillar_width_altar
    build_block(center_block_master, altar_width, block_height, altar_depth)

    block_side_depth = z + depth * 0.95 - (z + depth * 0.4 + attachment_depth * 1.2 + door_width[1])
    build_block(center_block_sides, pillar_width_altar / 2, block_height, block_side_depth)
    center_block_sides = (x + width - tower_width - pillar_width_altar / 4, y + block_height / 2,
                          (z + depth * 0.4 + attachment_depth * 1.2 + door_width[1] + z + depth * 0.95) / 2)
    build_block(center_block_sides, pillar_width_altar / 2, block_height, block_side_depth)

    center_level_2 = (center_block_master[0], center_block_master[1] + block_height / 2 + block_height / 4,
                      center_block_master[2] + altar_depth / 4)
    build_block(center_level_2, altar_width * 0.7, block_height / 2, altar_depth / 4)
    delta_level = (altar_depth / 4) * 0.2
    center_level_3 = (center_block_master[0], center_block_master[1] + block_height + block_height / 4,
                      center_block_master[2] + altar_depth / 4 + delta_level / 2)
    build_block(center_level_3, altar_width * 0.6, (block_height / 2) * 0.8, altar_depth / 4 - delta_level)
    level_4 = (
        (8.979166666666668, -0.10000000000000009, 51.12500000000001),
        (18.020833333333332, -0.10000000000000009, 51.12500000000001),
        (9.625, -0.7050000000000001, 51.12500000000001),
        (17.375, -0.7050000000000001, 51.12500000000001)
    )

    len_side = 1.6

    base = (
        level_4[0],
        (level_4[0][0], level_4[0][1], level_4[0][2] + len_side),
        (level_4[0][0] - len_side, level_4[0][1], level_4[0][2] + len_side),
        (level_4[0][0] - len_side, level_4[0][1], level_4[0][2])
    )
    # back_depth = 53.95833333333334

    delta = height / 3

    obj = build_wall(base[0], base[1], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[1], base[2], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[2], base[3], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[0], base[3], delta)
    DataUtil.objects.append(obj)

    base = (
        level_4[1],
        (level_4[1][0], level_4[1][1], level_4[1][2] + len_side),
        (level_4[1][0] + len_side, level_4[1][1], level_4[1][2] + len_side),
        (level_4[1][0] + len_side, level_4[1][1], level_4[1][2])
    )

    obj = build_wall(base[0], base[1], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[1], base[2], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[2], base[3], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[0], base[3], delta)
    DataUtil.objects.append(obj)

    base = (
        level_4[1],
        (level_4[1][0], level_4[1][1], level_4[1][2] + len_side),
        (level_4[0][0], level_4[0][1], level_4[0][2] + len_side),
        level_4[0],
    )

    delta *= 0.8

    obj = build_wall(base[0], base[1], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[1], base[2], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[2], base[3], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[0], base[3], delta)
    DataUtil.objects.append(obj)

    base = (
        level_4[2],
        level_4[3],
        (level_4[3][0], level_4[3][1], level_4[3][2] - len_side),
        (level_4[2][0], level_4[2][1], level_4[2][2] - len_side),
    )

    delta *= 0.7

    obj = build_wall(base[0], base[1], delta)
    obj = DataUtil.objects.append(obj)
    obj = build_wall(base[1], base[2], delta)
    obj = DataUtil.objects.append(obj)
    obj = build_wall(base[2], base[3], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[0], base[3], delta)
    DataUtil.objects.append(obj)

    level_5_width = 7
    level_5_ref = mid(level_4[0], level_4[1])
    level_5 = (
        (level_5_ref[0] + level_5_width / 2, level_5_ref[1], level_5_ref[2] + 1.6),
        (level_5_ref[0] - level_5_width / 2, level_5_ref[1], level_5_ref[2] + 1.6)
    )
    delta = (height / 3) * 0.8
    len_side = 1.4
    level_5_y_ref = level_5_ref[1] + delta

    base = (
        (level_5[0][0], level_5_y_ref, level_5[0][2]),
        (level_5[1][0], level_5_y_ref, level_5[1][2]),
        (level_5[1][0], level_5_y_ref, level_5[1][2] - len_side),
        (level_5[0][0], level_5_y_ref, level_5[0][2] - len_side),
    )

    obj = build_wall(base[0], base[1], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[1], base[2], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[2], base[3], delta)
    DataUtil.objects.append(obj)
    obj = build_wall(base[0], base[3], delta)
    DataUtil.objects.append(obj)

    center_level_3 = list(center_level_3)

    center_level_3[1] += (block_height / 2) * 0.7 + block_height

    left_chair = (center_level_3[0] - 0.5, center_level_3[1], center_level_3[2])
    right_chair = (center_level_3[0] + 0.5, center_level_3[1], center_level_3[2])

    # obj1
    build_chair(left_chair, right_chair, delta)

    ref_ground_y = center_block_master[1] + block_height / 2
    ref_center_x = center_block_master[0]
    ref_table_z = center_block_master[2] * 0.9

    center_table = (ref_center_x, ref_ground_y, ref_table_z)

    # obj2
    build_main_table(center_table, altar_width * 0.4, altar_depth / 4, height / 5)

    # obj3
    ref_ground_y = center_table[1] + height / 5
    ref_center_x = center_table[0]
    ref_table_z = center_table[2]

    center_bible = (ref_center_x, ref_ground_y, ref_table_z)

    bible_plain = build_bible_support(center_bible, altar_width * 0.04, (altar_depth / 4) * 0.2, (height / 5) * 0.15)
    bible_dim = (altar_width * 0.04, (altar_depth / 4) * 0.2, (height / 5) * 0.15)

    # obj4
    build_bible(center_bible, bible_plain, bible_dim[0] * 0.8, bible_dim[1] * 0.8, bible_dim[2] * 0.3)
