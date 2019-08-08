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
    config_door((x_origin + width / 2 + door_width[2] / 2, y_origin, z_origin),
                (x_origin + width / 2 - door_width[2] / 2, y_origin, z_origin), 'front', 2)

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
    config_door((x_origin + width - (tower_width / 3), y_origin, z_origin),
                (x_origin + width - (tower_width / 3) - door_width[0], y_origin, z_origin), 'front', 4)

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

    build_wall((x_origin + width, y_origin, z_origin + depth / 3),
               (x_origin + width, y_origin, z_origin + 2 * depth / 3 - door_width[0]), height)

    # porta lateral meio
    build_wall((x_origin + width, y_origin + door_height[0], z_origin + 2 * depth / 3 - door_width[0]),
               (x_origin + width, y_origin + door_height[0], z_origin + 2 * depth / 3),
               height - door_height[0])

    build_wall((x_origin + width, y_origin, z_origin + 2 * depth / 3),
               (x_origin + width, y_origin, z_origin + depth - 3 * door_width[0]), height)

    # porta lateral mais fundo
    build_wall((x_origin + width, y_origin + door_height[0], z_origin + depth - 3 * door_width[0]),
               (x_origin + width, y_origin + door_height[0], z_origin + depth - 3 * door_width[0] + door_width[0]),
               height - door_height[0])

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
    print(center, origin, delta)

    base = (
        (origin[0] - delta, origin[1], origin[2] - delta),
        (origin[0] - delta, origin[1], origin[2] + delta + 2 * center[2]),
        (origin[0] + delta + 2 * center[0], origin[1], origin[2] + delta + 2 * center[2]),
        (origin[0] + 2 * center[0] + delta, origin[1], origin[2] - delta),
    )
    print(base)
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

    glTranslate(-config.base_left[0], -config.base_left[1], -config.base_left[2])
    glRotatef(config.alpha, 0, 1, 0)
    glTranslate(config.base_left[0], config.base_left[1], config.base_left[2])

    build(left_edges, left_vertices, left_surfaces)

    if config.run:
        print(config.alpha)
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

    glTranslate(-config.base_right[0], -config.base_right[1], -config.base_right[2])
    glRotatef(-config.alpha, 0, 1, 0)
    glTranslate(config.base_right[0], config.base_right[1], config.base_right[2])

    build(right_edges, right_vertices, right_surfaces)
    glPopMatrix()


def build_block(center, l, h, d):
    pass


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
