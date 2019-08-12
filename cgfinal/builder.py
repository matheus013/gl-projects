import copy

from cgfinal.constants import *
from cgfinal.support import *
import math
from cgfinal.door import *


def config_door(base_left, base_right, ref, id):
    door_conf[ref][id].base_left = base_left
    door_conf[ref][id].base_right = base_right


def build_front(x_origin, y_origin, z_origin):
    build_wall((x_origin, y_origin, z_origin), (x_origin + (tower_width / 3), y_origin, z_origin),
               height)
    # door 1
    build_wall((x_origin + tower_width / 3, y_origin + door_height[0], z_origin),
               (x_origin + tower_width / 3 + door_width[0], y_origin + door_height[0], z_origin),
               height - door_height[0])
    config_door((x_origin + tower_width / 3, y_origin, z_origin),
                (x_origin + tower_width / 3 + door_width[0], y_origin, z_origin), 'front', 0)

    build_wall((x_origin + (tower_width / 3) + door_width[0], y_origin, z_origin),
               (x_origin + 4 * (tower_width / 3), y_origin, z_origin), height)
    # door 2
    build_wall((x_origin + 4 * (tower_width / 3), y_origin + door_height[1], z_origin),
               (x_origin + 4 * (tower_width / 3) + door_width[1], y_origin + door_height[1], z_origin),
               height - door_height[1])
    config_door((x_origin + 4 * (tower_width / 3), y_origin, z_origin),
                (x_origin + 4 * (tower_width / 3) + door_width[1], y_origin, z_origin), 'front', 1)

    build_wall((x_origin + 4 * (tower_width / 3) + door_width[1], y_origin, z_origin),
               (x_origin + width / 2 - door_width[2] / 2, y_origin, z_origin),
               height)
    # door 3
    build_wall((x_origin + width / 2 + door_width[2] / 2, y_origin + door_height[2], z_origin),
               (x_origin + width / 2 - door_width[2] / 2, y_origin + door_height[2], z_origin), height - door_height[2])
    config_door((x_origin + width / 2 - door_width[2] / 2, y_origin, z_origin),
                (x_origin + width / 2 + door_width[2] / 2, y_origin, z_origin),
                'front', 2)

    build_wall((x_origin + width / 2 + door_width[2] / 2, y_origin, z_origin),
               (x_origin + width - 4 * (tower_width / 3) - door_width[1], y_origin, z_origin), height)
    # door 2
    build_wall((x_origin + width - 4 * (tower_width / 3) - door_width[1], y_origin + door_height[1], z_origin),
               (x_origin + width - 4 * (tower_width / 3), y_origin + door_height[1], z_origin),
               height - door_height[1])
    config_door((x_origin + width - 4 * (tower_width / 3) - door_width[1], y_origin, z_origin),
                (x_origin + width - 4 * (tower_width / 3), y_origin, z_origin), 'front', 3)

    build_wall((x_origin + width - 4 * (tower_width / 3), y_origin, z_origin),
               (x_origin + width - (tower_width / 3) - door_width[0], y_origin, z_origin),
               height)
    # door 1
    build_wall((x_origin + width - (tower_width / 3), y_origin + door_height[0], z_origin),
               (x_origin + width - (tower_width / 3) - door_width[0], y_origin + door_height[0], z_origin),
               height - door_height[0])
    config_door((x_origin + width - (tower_width / 3) - door_width[0], y_origin, z_origin),
                (x_origin + width - (tower_width / 3), y_origin, z_origin),
                'front', 4)

    build_wall((x_origin + width - (tower_width / 3), y_origin, z_origin),
               (x_origin + width, y_origin, z_origin),
               height)


def build_tower(x_origin, y_origin, z_origin):
    # left
    build_wall((x_origin, y_origin + height, z_origin), (x_origin + tower_width, y_origin + height, z_origin),
               tower_height)

    build_wall((x_origin, y_origin + height, z_origin), (x_origin, y_origin + height, z_origin + tower_width),
               tower_height)

    build_wall((x_origin + tower_width, y_origin + height, z_origin),
               (x_origin + tower_width, y_origin + height, z_origin + tower_width),
               tower_height)

    build_wall((x_origin, y_origin + height, z_origin + tower_width),
               (x_origin + tower_width, y_origin + height, z_origin + tower_width),
               tower_height)

    # right
    build_wall((x_origin + width, y_origin + height, z_origin),
               (x_origin + width - tower_width, y_origin + height, z_origin),
               tower_height)

    build_wall((x_origin + width, y_origin + height, z_origin),
               (x_origin + width, y_origin + height, z_origin + tower_width),
               tower_height)

    build_wall((x_origin + width - tower_width, y_origin + height, z_origin),
               (x_origin + width - tower_width, y_origin + height, z_origin + tower_width),
               tower_height)

    build_wall((x_origin + width, y_origin + height, z_origin + tower_width),
               (x_origin + width - tower_width, y_origin + height, z_origin + tower_width),
               tower_height)


def build_right(x_origin, y_origin, z_origin):
    build_wall((x_origin + width, y_origin, z_origin),
               (x_origin + width, y_origin, z_origin + depth / 3 - door_width[0]), height)
    # porta lateral frente
    build_wall((x_origin + width, y_origin + door_height[0], z_origin + depth / 3),
               (x_origin + width, y_origin + door_height[0], z_origin + depth / 3 - door_width[0]),
               height - door_height[0])
    config_door((x_origin + width, y_origin, z_origin + depth / 3 - door_width[0]),
                (x_origin + width, y_origin, z_origin + depth / 3), 'right', 0)

    build_wall((x_origin + width, y_origin, z_origin + depth / 3),
               (x_origin + width, y_origin, z_origin + 2 * depth / 3 - door_width[0]), height)

    # porta lateral meio
    build_wall((x_origin + width, y_origin + door_height[0], z_origin + 2 * depth / 3 - door_width[0]),
               (x_origin + width, y_origin + door_height[0], z_origin + 2 * depth / 3),
               height - door_height[0])
    config_door((x_origin + width, y_origin, z_origin + 2 * depth / 3 - door_width[0]),
                (x_origin + width, y_origin, z_origin + 2 * depth / 3), 'right', 1)

    build_wall((x_origin + width, y_origin, z_origin + 2 * depth / 3),
               (x_origin + width, y_origin, z_origin + depth - 3 * door_width[0]), height)

    # porta lateral mais fundo
    build_wall((x_origin + width, y_origin + door_height[0], z_origin + depth - 3 * door_width[0]),
               (x_origin + width, y_origin + door_height[0], z_origin + depth - 3 * door_width[0] + door_width[0]),
               height - door_height[0])
    config_door((x_origin + width, y_origin, z_origin + depth - 3 * door_width[0]),
                (x_origin + width, y_origin, z_origin + depth - 3 * door_width[0] + door_width[0]),
                'right', 2)

    build_wall((x_origin + width, y_origin, z_origin + depth - 3 * door_width[0] + door_width[0]),
               (x_origin + width, y_origin, z_origin + depth), height)


def build_back(x_origin, y_origin, z_origin):
    build_wall((x_origin, y_origin, z_origin + depth), (x_origin + width, y_origin, z_origin + depth), height)


def build_left(x_origin, y_origin, z_origin):
    build_wall((x_origin, y_origin, z_origin), (x_origin, y_origin, z_origin + depth * 0.4), height)

    # attachment begin
    build_wall((x_origin, y_origin, z_origin + depth * 0.4),
               (x_origin - attachment_width, y_origin, z_origin + depth * 0.4), height)

    build_wall((x_origin - attachment_width, y_origin, z_origin + depth * 0.4), (
        x_origin - attachment_width, y_origin, z_origin + depth * 0.4 + attachment_depth), height)

    build_wall((x_origin - attachment_width, y_origin, z_origin + depth * 0.4 + attachment_depth),
               (x_origin, y_origin, z_origin + depth * 0.4 + attachment_depth), height)
    # attachment end
    build_wall((x_origin, y_origin, z_origin + depth * 0.4 + attachment_depth),
               (x_origin, y_origin, z_origin + depth * (2 / 3) - door_width[0]), height)

    # door
    build_wall((x_origin, y_origin + door_height[0], z_origin + depth * (2 / 3)),
               (x_origin, y_origin + door_height[0], z_origin + depth * (2 / 3) - door_width[0]),
               height - door_height[0])
    config_door((x_origin, y_origin, z_origin + depth * (2 / 3)),
                (x_origin, y_origin, z_origin + depth * (2 / 3) - door_width[0]), 'left', 0)

    build_wall((x_origin, y_origin, z_origin + depth * (2 / 3)), (x_origin, y_origin, z_origin + depth), height)

    attachment_origin = (x_origin - attachment_width, y_origin, z_origin + depth * 0.4)
    attachment_center = (math.fabs(attachment_width / 2), math.fabs(y_origin), math.fabs(attachment_depth / 2))
    if ground:
        build_ground(attachment_center, attachment_origin, 3)


def build_top(x_origin, y_origin, z_origin):
    vertices = (
        (x_origin + width / 2, y_origin + height + tower_height * 0.2, z_origin),
        (x_origin + width / 2, y_origin + height + tower_height * 0.2, z_origin + depth),
        (x_origin + width, y_origin + height, z_origin + depth),
        (x_origin + width, y_origin + height, z_origin),
    )
    DataUtil.edges += make_edges(vertices, len(DataUtil.vertices))
    DataUtil.vertices += vertices

    vertices = (
        (x_origin + width / 2, y_origin + height + tower_height * 0.2, z_origin),
        (x_origin + width / 2, y_origin + height + tower_height * 0.2, z_origin + depth),
        (x_origin, y_origin + height, z_origin + depth),
        (x_origin, y_origin + height, z_origin),
    )
    DataUtil.edges += make_edges(vertices, len(DataUtil.vertices))
    DataUtil.vertices += vertices

    valid_points(DataUtil.vertices, 3, 'top')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'top')


def build_pillar(x_center, y_center, z_center, h, d):
    vertices = (
        # base
        (x_center - d / 2, y_center, z_center + d / 2),
        (x_center + d / 2, y_center, z_center + d / 2),
        (x_center + d / 2, y_center, z_center - d / 2),
        (x_center - d / 2, y_center, z_center - d / 2),

    )
    build_wall(vertices[0], vertices[1], h)
    build_wall(vertices[1], vertices[2], h)
    build_wall(vertices[2], vertices[3], h)
    build_wall(vertices[0], vertices[3], h)


def build_wall(origin, end, h):
    vertices = quad(origin, end, h)

    DataUtil.edges += make_edges(vertices, len(DataUtil.vertices))
    DataUtil.surfaces += make_surface(vertices, len(DataUtil.vertices))
    DataUtil.vertices += vertices

    valid_points(DataUtil.vertices, 3, 'wall')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'wall')


def build_plain(origin, end, d):
    vertices = (
        origin,
        (origin[0], origin[1], origin[2] + d),
        (end[0], end[1], end[2] + d),
        end,
    )

    DataUtil.edges += make_edges(vertices, len(DataUtil.vertices))
    DataUtil.surfaces += make_surface(vertices, len(DataUtil.vertices))
    DataUtil.vertices += vertices

    valid_points(DataUtil.vertices, 3, 'plain')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'plain')


def build_arc_wall(arc_center, top_origin, top_end, radius, x_or_z):
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

    DataUtil.edges += make_edges(vertices, len(DataUtil.vertices))
    DataUtil.surfaces += make_surface(vertices, len(DataUtil.vertices))
    DataUtil.vertices += vertices


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


def build_ground(center, origin, delta):
    base = (
        (origin[0] - delta, origin[1], origin[2] - delta),
        (origin[0] - delta, origin[1], origin[2] + delta + 2 * center[2]),
        (origin[0] + delta + 2 * center[0], origin[1], origin[2] + delta + 2 * center[2]),
        (origin[0] + 2 * center[0] + delta, origin[1], origin[2] - delta),
    )
    build_wall(base[0], base[1], delta)
    build_wall(base[1], base[2], delta)
    build_wall(base[2], base[3], delta)
    build_wall(base[0], base[3], delta)

    build_plain(base[0], base[3], 2 * (center[2] + delta))
    pass


def build_door(config, key):
    center = mid(config.base_left, config.base_right)

    # left
    glPushMatrix()

    left_vertices = quad(config.base_left, center, config.height)
    left_edges = make_edges(left_vertices, 0)
    left_surfaces = make_surface(left_vertices, 0)

    glTranslate(config.base_left[0], config.base_left[1], config.base_left[2])
    glRotatef(config.alpha, 0, 1, 0)
    glTranslate(-config.base_left[0], -config.base_left[1], -config.base_left[2])

    build(left_edges, left_vertices, left_surfaces)

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
    right_edges = make_edges(right_vertices, 0)
    right_surfaces = make_surface(right_vertices, 0)

    glTranslate(config.base_right[0], config.base_right[1], config.base_right[2])
    glRotatef(-config.alpha, 0, 1, 0)
    glTranslate(-config.base_right[0], -config.base_right[1], -config.base_right[2])

    build(right_edges, right_vertices, right_surfaces)
    glPopMatrix()


def build_block(center, l, h, d):
    # base plain
    c = list(center)
    c[1] = c[1] - h / 2
    base = build_block_plain(c, l, d)
    # top plain
    c = list(center)
    c[1] = c[1] + h / 2
    build_block_plain(c, l, d)

    build_wall(base[0], base[1], h)
    build_wall(base[1], base[2], h)
    build_wall(base[2], base[3], h)
    build_wall(base[0], base[3], h)

    pass


def build_block_plain(center, l, d):
    vertices = (
        (center[0] - l / 2, center[1], center[2] - d / 2),
        (center[0] - l / 2, center[1], center[2] + d / 2),
        (center[0] + l / 2, center[1], center[2] + d / 2),
        (center[0] + l / 2, center[1], center[2] - d / 2),
    )

    DataUtil.edges += make_edges(vertices, len(DataUtil.vertices))
    DataUtil.surfaces += make_surface(vertices, len(DataUtil.vertices))
    DataUtil.vertices += vertices

    valid_points(DataUtil.vertices, 3, 'plain')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'plain')
    return vertices


def build_bench(center, l, h, d):
    pass


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


def build_internal(x, y, z):
    build_pillar(x + tower_width, y, z + depth * (2 / 15), height, width / 20)
    build_pillar(x + tower_width, y, z + depth * (4 / 15), height, width / 20)
    build_pillar(x + tower_width, y, z + depth * (6 / 15), height, width / 20)

    build_pillar(x + width - tower_width, y, z + depth * (2 / 15), height, width / 20)
    build_pillar(x + width - tower_width, y, z + depth * (4 / 15), height, width / 20)
    build_pillar(x + width - tower_width, y, z + depth * (6 / 15), height, width / 20)

    build_wall((x, y, z + depth * 0.4 + attachment_depth), (x + tower_width, y, z + depth * 0.4 + attachment_depth),
               height)
    pillar_width_altar = width / 12
    # front pillar
    build_pillar(x + tower_width, y, z + depth * 0.4 + attachment_depth, height, pillar_width_altar)
    build_pillar(x + width - tower_width, y, z + depth * 0.4 + attachment_depth, height, pillar_width_altar)

    build_wall((x + width - tower_width, y, z + depth * 0.4 + attachment_depth),
               (x + width, y, z + depth * 0.4 + attachment_depth),
               height)

    build_wall((x + tower_width * 1.5, y, z + depth * 0.4 + attachment_depth),
               (x + tower_width, y, z + depth * 0.4 + attachment_depth),
               height)

    build_wall((x + width - tower_width * 1.5, y, z + depth * 0.4 + attachment_depth),
               (x + width, y, z + depth * 0.4 + attachment_depth),
               height)
    # internal wall under tower
    # ->right
    build_wall((x + width - tower_width, y, z),
               (x + width - tower_width, y, z + depth * (2 / 15)), height)
    # ->left
    build_wall((x + tower_width * 0.7, y, z),
               (x + tower_width * 0.7, y, z + depth * (2 / 15)), height)
    build_wall((x + tower_width * 0.7, y, z + depth * (2 / 15)),
               (x + tower_width, y, z + depth * (2 / 15)), height)
    build_wall((x + tower_width, y, z + depth * (2 / 15)),
               (x + tower_width, y, z + depth * (4 / 45)), height)
    build_wall((x + tower_width, y, z + depth * (4 / 45)),
               (x + tower_width - tower_width * 0.25, y, z + depth * (4 / 45)), height)
    build_wall((x + tower_width - tower_width * 0.25, y, z + depth * (4 / 45)),
               (x + tower_width - tower_width * 0.25, y, z + depth * (2 / 45)), height)
    build_wall((x + tower_width - tower_width * 0.25, y, z + depth * (2 / 45)),
               (x + tower_width, y, z + depth * (2 / 45)), height)
    build_wall((x + tower_width, y, z + depth * (2 / 45)),
               (x + tower_width, y, z), height)
    # altar
    # altar side wall(left)
    x_ref = x + tower_width
    d_height_ref = height * 0.6
    build_wall((x_ref, y, z + depth * 0.4 + attachment_depth),
               (x_ref, y, z + depth * 0.4 + attachment_depth * 1.2), height)

    build_wall((x_ref, y + d_height_ref, z + depth * 0.4 + attachment_depth * 1.2),
               (x_ref, y + d_height_ref, z + depth * 0.4 + attachment_depth * 1.2 + door_width[1]),
               height - d_height_ref)
    build_wall((x_ref, y, z + depth * 0.4 + attachment_depth * 1.2 + door_width[1]),
               (x_ref, y, z + depth * 0.95), height)
    # altar side wall(right)
    x_ref = x + width - tower_width
    build_wall((x_ref, y, z + depth * 0.4 + attachment_depth),
               (x_ref, y, z + depth * 0.4 + attachment_depth * 1.2), height)

    build_wall((x_ref, y + d_height_ref, z + depth * 0.4 + attachment_depth * 1.2),
               (x_ref, y + d_height_ref, z + depth * 0.4 + attachment_depth * 1.2 + door_width[1]),
               height - d_height_ref)
    build_wall((x_ref, y, z + depth * 0.4 + attachment_depth * 1.2 + door_width[1]),
               (x_ref, y, z + depth * 0.95), height)
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

    center_level_3 = ((center_block_master[0], center_block_master[1] + block_height + block_height / 4,
                       center_block_master[2] + altar_depth / 4))
    build_block(center_level_3, altar_width * 0.6, (block_height / 2) * 0.8, altar_depth / 4)
    center_level_4 = ()
