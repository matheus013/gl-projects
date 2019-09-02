from OpenGL.raw.GL.VERSION.GL_1_1 import GL_SMOOTH

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

ref_light = {
    'inc_factor': 0.01, 'inc_pl_y': 0, 'intensity': 0.3, 'model': GL_SMOOTH
}


class DataUtil(object):
    vertices = ()
    edges = ()
    surfaces = ()
    textures_id = {}
    objects = []
    path_textures = {
        'wall': './textures/source/wall.jpg',
        'chair': './textures/source/chair.jpg',
        'chair_back': './textures/source/chair_back.png',
        'chair_wood': './textures/source/wood_chair.jpg',
        'ground0': './textures/source/piso1.jpg',
        'ground1': './textures/source/piso2.jpg',
        'ground2': './textures/source/piso-1.png',
        'door': './textures/source/door.jpg',
        'sub_ground': './textures/source/sub.jpg',
        'top': './textures/source/telhado.jpg',
        'table': './textures/source/table.jpg',
        'top_table': './textures/source/top_table.jpg',
        'gold': './textures/source/gold.jpeg',
        'window':'./textures/source/window.jpg',
        'jesus': './textures/source/jesus-0.jpg',
        'over-jesus': './textures/source/over-jesus-0.jpg',
        'vitral1': './textures/source/vitral-0.jpg',
        'vitral2': './textures/source/vitral-1.jpg',
        'vitral3': './textures/source/vitral-2.jpg',
        'pillar': './textures/source/pillar-altar.jpg',
        'alt-main': './textures/source/altar-main.jpg',

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
