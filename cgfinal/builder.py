from cgfinal.constants import *
from cgfinal.support import *


def build_front(x_origin, y_origin, z_origin):
    front_vertices = ((x_origin, y_origin, z_origin),
                      (x_origin, y_origin + height + tower_height, z_origin),
                      (x_origin + tower_width, y_origin + height + tower_height, z_origin),
                      (x_origin + tower_width, y_origin + height, z_origin),
                      (x_origin + tower_width + (width - 2 * tower_width), y_origin + height, z_origin),
                      (x_origin + tower_width + (width - 2 * tower_width), y_origin + height + tower_height, z_origin),
                      (x_origin + tower_width * 2 + (width - 2 * tower_width), y_origin + height + tower_height,
                       z_origin),
                      (x_origin + width, y_origin, z_origin),
                      # porta menor direita
                      (x_origin + width - (tower_width / 3), y_origin, z_origin),
                      (x_origin + width - (tower_width / 3), y_origin + door_height[0], z_origin),
                      (x_origin + width - (tower_width / 3) - door_width[0], y_origin + door_height[0], z_origin),
                      (x_origin + width - (tower_width / 3) - door_width[0], y_origin, z_origin),
                      # porta meio direita
                      (x_origin + width - 4 * (tower_width / 3), y_origin, z_origin),
                      (x_origin + width - 4 * (tower_width / 3), y_origin + door_height[1], z_origin),
                      (x_origin + width - 4 * (tower_width / 3) - door_width[1], y_origin + door_height[1], z_origin),
                      (x_origin + width - 4 * (tower_width / 3) - door_width[1], y_origin, z_origin),
                      # porta meio
                      (x_origin + width / 2 + door_width[2] / 2, y_origin, z_origin),
                      (x_origin + width / 2 + door_width[2] / 2, y_origin + door_height[2], z_origin),
                      (x_origin + width / 2 - door_width[2] / 2, y_origin + door_height[2], z_origin),
                      (x_origin + width / 2 - door_width[2] / 2, y_origin, z_origin),
                      # porta meio esquerda
                      (x_origin + 4 * (tower_width / 3) + door_width[1], y_origin, z_origin),
                      (x_origin + 4 * (tower_width / 3) + door_width[1], y_origin + door_height[1], z_origin),
                      (x_origin + 4 * (tower_width / 3), y_origin + door_height[1], z_origin),
                      (x_origin + 4 * (tower_width / 3), y_origin, z_origin),
                      # porta menor esquerda
                      (x_origin + (tower_width / 3) + door_width[0], y_origin, z_origin),
                      (x_origin + (tower_width / 3) + door_width[0], y_origin + door_height[0], z_origin),
                      (x_origin + (tower_width / 3), y_origin + door_height[0], z_origin),
                      (x_origin + (tower_width / 3), y_origin, z_origin)

                      )

    DataUtil.edges += make_edges(front_vertices, len(DataUtil.vertices))
    DataUtil.vertices += front_vertices

    front_vertices = (
        (x_origin + tower_width, y_origin + height, z_origin),
        (x_origin + tower_width, y_origin + height + tower_height, z_origin),
        (x_origin + tower_width, y_origin + height + tower_height, z_origin + tower_width),
        (x_origin + tower_width, y_origin + height, z_origin + tower_width),

    )

    DataUtil.edges += make_edges(front_vertices, len(DataUtil.vertices))
    DataUtil.vertices += front_vertices

    front_vertices = (
        (x_origin + tower_width, y_origin + height, z_origin + tower_width),
        (x_origin + tower_width, y_origin + height + tower_height, z_origin + tower_width),
        (x_origin, y_origin + height + tower_height, z_origin + tower_width),
        (x_origin, y_origin + height, z_origin + tower_width),

    )
    DataUtil.edges += make_edges(front_vertices, len(DataUtil.vertices))
    DataUtil.vertices += front_vertices

    front_vertices = (
        (x_origin + tower_width + (width - 2 * tower_width), y_origin + height, z_origin),
        (x_origin + tower_width + (width - 2 * tower_width), y_origin + height + tower_height, z_origin),
        (x_origin + tower_width + (width - 2 * tower_width), y_origin + height + tower_height, z_origin + tower_width),
        (x_origin + tower_width + (width - 2 * tower_width), y_origin + height, z_origin + tower_width),

    )

    DataUtil.edges += make_edges(front_vertices, len(DataUtil.vertices))
    DataUtil.vertices += front_vertices

    front_vertices = (
        (x_origin + tower_width + (width - 2 * tower_width), y_origin + height, z_origin + tower_width),
        (x_origin + tower_width + (width - 2 * tower_width), y_origin + height + tower_height, z_origin + tower_width),
        (x_origin + width, y_origin + height + tower_height, z_origin + tower_width),
        (x_origin + width, y_origin + height, z_origin + tower_width),

    )
    DataUtil.edges += make_edges(front_vertices, len(DataUtil.vertices))
    DataUtil.vertices += front_vertices

    valid_points(DataUtil.vertices, 3, 'front')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'front')


def build_right(x_origin, y_origin, z_origin):
    right_vertices = ((x_origin + width, y_origin, z_origin),
                      (x_origin + width, y_origin + height + tower_height, z_origin),
                      (x_origin + width, y_origin + height + tower_height, z_origin + tower_width),
                      (x_origin + width, y_origin + height, z_origin + tower_width),
                      (x_origin + width, y_origin + height, z_origin + depth),
                      (x_origin + width, y_origin, z_origin + depth),
                      # porta lateral mais fundo
                      (x_origin + width, y_origin, z_origin + depth - 2 * door_width[0]),
                      (x_origin + width, y_origin + door_height[0], z_origin + depth - 2 * door_width[0]),
                      (x_origin + width, y_origin + door_height[0], z_origin + depth - 3 * door_width[0]),
                      (x_origin + width, y_origin, z_origin + depth - 3 * door_width[0]),
                      # porta lateral meio
                      (x_origin + width, y_origin, z_origin + 2 * depth / 3),
                      (x_origin + width, y_origin + door_height[0], z_origin + 2 * depth / 3),
                      (x_origin + width, y_origin + door_height[0], z_origin + 2 * depth / 3 - door_width[0]),
                      (x_origin + width, y_origin, z_origin + 2 * depth / 3 - door_width[0]),
                      # porta lateral frente
                      (x_origin + width, y_origin, z_origin + depth / 3),
                      (x_origin + width, y_origin + door_height[0], z_origin + depth / 3),
                      (x_origin + width, y_origin + door_height[0], z_origin + depth / 3 - door_width[0]),
                      (x_origin + width, y_origin, z_origin + depth / 3 - door_width[0])

                      )
    DataUtil.edges += make_edges(right_vertices, len(DataUtil.vertices))
    DataUtil.vertices += right_vertices

    valid_points(DataUtil.vertices, 3, 'right')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'right')


def build_back(x_origin, y_origin, z_origin):
    back_vertices = (
        (x_origin + width, y_origin, z_origin + depth),
        (x_origin + width, y_origin + height, z_origin + depth),
        (x_origin, y_origin + height, z_origin + depth),
        (x_origin, y_origin, z_origin + depth),
    )

    DataUtil.edges += make_edges(back_vertices, len(DataUtil.vertices))
    DataUtil.vertices += back_vertices

    valid_points(DataUtil.vertices, 3, 'back')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'back')


def build_left(x_origin, y_origin, z_origin):
    left_vertices = (
        (x_origin, y_origin, z_origin),
        (x_origin, y_origin + height + tower_height, z_origin),
        (x_origin, y_origin + height + tower_height, z_origin + tower_width),
        (x_origin, y_origin + height, z_origin + tower_width),
        (x_origin, y_origin + height, z_origin + depth * 0.4),
        (x_origin - attachment_width, y_origin + height, z_origin + depth * 0.4),
        (x_origin - attachment_width, y_origin + height, z_origin + depth * 0.4 + attachment_depth),
        (x_origin, y_origin + height, z_origin + depth * 0.4 + attachment_depth),
        (x_origin, y_origin + height, z_origin + depth),
        (x_origin, y_origin, z_origin + depth),
        # porta
        (x_origin, y_origin, z_origin + depth * (2 / 3)),
        (x_origin, y_origin + door_height[0], z_origin + depth * (2 / 3)),
        (x_origin, y_origin + door_height[0], z_origin + depth * (2 / 3) - door_width[0]),
        (x_origin, y_origin, z_origin + depth * (2 / 3) - door_width[0]),
        #
        (x_origin, y_origin, z_origin + depth * 0.4 + attachment_depth),
        (x_origin - attachment_width, y_origin, z_origin + depth * 0.4 + attachment_depth),
        (x_origin - attachment_width, y_origin, z_origin + depth * 0.4),
        (x_origin, y_origin, z_origin + depth * 0.4),

    )
    DataUtil.edges += make_edges(left_vertices, len(DataUtil.vertices))
    DataUtil.vertices += left_vertices

    left_vertices = (
        (x_origin - attachment_width, y_origin + height, z_origin + depth * 0.4),
        (x_origin - attachment_width, y_origin + height, z_origin + depth * 0.4 + attachment_depth),
        (x_origin - attachment_width, y_origin, z_origin + depth * 0.4 + attachment_depth),
        (x_origin - attachment_width, y_origin, z_origin + depth * 0.4),
    )
    DataUtil.edges += make_edges(left_vertices, len(DataUtil.vertices))
    DataUtil.vertices += left_vertices

    left_vertices = (
        (x_origin, y_origin + height, z_origin + depth * 0.4),
        (x_origin, y_origin, z_origin + depth * 0.4),
    )

    DataUtil.edges += make_edges(left_vertices, len(DataUtil.vertices))
    DataUtil.vertices += left_vertices

    left_vertices = (
        (x_origin, y_origin + height, z_origin + depth * 0.4 + attachment_depth),
        (x_origin, y_origin, z_origin + depth * 0.4 + attachment_depth),
    )

    DataUtil.edges += make_edges(left_vertices, len(DataUtil.vertices))
    DataUtil.vertices += left_vertices

    valid_points(DataUtil.vertices, 3, 'back')
    valid_edges(DataUtil.edges, DataUtil.vertices, 'back')
