width = 25
height = 11

tower_height = height * 0.8
tower_width = width * 0.2

door_width = [tower_width / 3, tower_width * 0.5, tower_width * 0.8]
door_height = [tower_height * 0.3, tower_height * 0.4, tower_height * 0.5]

depth = width * 2.2

attachment_depth = depth * 0.15
attachment_width = tower_width


class DataUtil(object):
    vertices = ()
    edges = ()
