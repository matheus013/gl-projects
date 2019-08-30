from cg_final.door.door import Door

width = 25
height = -11
depth = width * 2.2

center_point = (width / 2, height / 2, depth / 2)

tower_height = height * 0.8
tower_width = width * 0.2

door_width = [tower_width / 3, tower_width * 0.5, tower_width * 0.8]
door_height = [tower_height * 0.3, tower_height * 0.4, tower_height * 0.5]

attachment_depth = depth * 0.15
attachment_width = tower_width

ground = True

limit_door = (0.0, 90.0)

delta_rotate = 1

door_conf = {
    'front': [
        Door(door_height[0], door_width[0], (), (), 0, False, True),
        Door(door_height[1], door_width[1], (), (), 0, False, True),
        Door(door_height[2], door_width[2], (), (), 0, False, True),
        Door(door_height[1], door_width[1], (), (), 0, False, True),
        Door(door_height[0], door_width[0], (), (), 0, False, True)],
    'left': [
        Door(door_height[0], door_width[0], (), (), 0, False, True)],
    'right': [
        Door(door_height[0], door_width[0], (), (), 0, False, True),
        Door(door_height[0], door_width[0], (), (), 0, False, True),
        Door(door_height[0], door_width[0], (), (), 0, False, True)],

}


class DataUtil(object):
    vertices = ()
    edges = ()
    surfaces = ()
    textures_id = {}
    path_textures = {
        "wall": "/home/matheus.inacio@laccan.net/PycharmProjects/gl-projects/cg_final/textures/source/wall-0.png",
        "ground0": "/home/matheus.inacio@laccan.net/PycharmProjects/gl-projects/cg_final/textures/source/piso-1.png",

    }
    colors = (
        (0.9, 0, 0),  # red
        (0, 1, 0),  # green
        (0.75, 0.38, 0),  # orange
        (0, 0, 1),  # blue
        (1, 1, 0),  # yellow

    )
    face_view = False
    door = False
