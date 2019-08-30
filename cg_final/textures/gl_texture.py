import random
import sys

import array

import numpy
from PIL import Image

from OpenGL.GLUT import *

from OpenGL.GL import *

from OpenGL.GLU import *


class Texture(object):
    """Texture either loaded from a file or initialised with random colors."""

    def __init__(self):
        self.width, self.height = 0, 0
        self.raw_reference = None


class RandomTexture(Texture):
    """Image with random RGB values."""

    def __init__(self, xSizeP, ySizeP):
        self.width, self.height = xSizeP, ySizeP
        tmpList = [random.randint(0, 255) \
                   for i in range(3 * self.width * self.height)]
        self.texture_array = array.array('B', tmpList)
        self.raw_reference = self.texture_array.tostring()


class FileTexture(Texture):
    """Texture loaded from a file."""

    def __init__(self, fileName):
        img = Image.open(fileName, 'r').transpose(Image.FLIP_TOP_BOTTOM)
        self.width, self.height = img.size

        self.raw_reference = numpy.array(list(img.getdata()), numpy.uint8)

    def read_texture(self):
        texture_id = glGenTextures(1)  # return 1 texture name

        glBindTexture(GL_TEXTURE_2D, texture_id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)  # pname, param

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)  # repeat in s when done, if needed
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT)  # repeat in t when done, if needed
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)  # how to upsample?
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)  # how to upsample?

        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                     self.width, self.height, 0,
                     GL_RGB, GL_UNSIGNED_BYTE, self.raw_reference)

        glGenerateMipmap(GL_TEXTURE_2D)

        return texture_id

# def display():
#     """Glut display function."""
#
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#
#     glColor3f(1, 1, 1)
#
#     glBegin(GL_QUADS)
#
#     glTexCoord2f(0, 1)
#
#     glVertex3f(-0.5, 0.5, 0)
#
#     glTexCoord2f(0, 0)
#
#     glVertex3f(-0.5, -0.5, 0)
#
#     glTexCoord2f(1, 0)
#
#     glVertex3f(0.5, -0.5, 0)
#
#     glTexCoord2f(1, 1)
#
#     glVertex3f(0.5, 0.5, 0)
#
#     glEnd()
#
#     glutSwapBuffers()
#
#
# def init(fileName):
#     """Glut init function."""
#
#     try:
#
#         texture = FileTexture(fileName)
#
#     except:
#         print('could not open ', fileName, '; using random texture')
#         texture = RandomTexture(256, 256)
#
#     glClearColor(0, 0, 0, 0)
#
#     glShadeModel(GL_SMOOTH)
#
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
#
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
#
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
#
#     glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
#
#     print(texture.raw_reference)
#     glTexImage2D(GL_TEXTURE_2D, 0, 3, texture.width, texture.height, 0,
#                  GL_RGB, GL_UNSIGNED_BYTE, texture.raw_reference)
#
#     glEnable(GL_TEXTURE_2D)
#
#
# glutInit(sys.argv)
#
# glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
#
# glutInitWindowSize(250, 250)
#
# glutInitWindowPosition(100, 100)
#
# glutCreateWindow(sys.argv[0])
#
# print(sys.argv)
# import os
#
# os.getcwd()
# sys.argv.append('/home/matheus.inacio@laccan.net/PycharmProjects/gl-projects/cg_final/textures/source/wall-0.png')
# if len(sys.argv) > 1:
#     print('aqui')
#     init(sys.argv[1])
#
# else:
#
#     init(None)
#
# glutDisplayFunc(display)
#
# glutMainLoop()
