import array
import random

import numpy
from OpenGL.GL import *
from PIL import Image


class Texture(object):
    """Texture either loaded from a file or initialised with random colors."""

    def __init__(self):
        self.width, self.height = 0, 0
        self.raw_reference = None


class RandomTexture(Texture):
    """Image with random RGB values."""

    def __init__(self, xSizeP, ySizeP):
        super().__init__()
        self.width, self.height = xSizeP, ySizeP
        tmpList = [random.randint(0, 255) for i in range(3 * self.width * self.height)]
        self.texture_array = array.array('B', tmpList)
        self.raw_reference = self.texture_array.tostring()


class FileTexture(Texture):
    """Texture loaded from a file."""

    def __init__(self, fileName):
        super().__init__()
        img = Image.open(fileName, 'r').transpose(Image.FLIP_TOP_BOTTOM)
        self.width, self.height = img.size

        self.raw_reference = numpy.array(list(img.getdata()), numpy.uint8)

    def read_texture(self, repeat=True):
        texture_id = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, texture_id)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)

        if repeat:
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        else:
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
            glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)

        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                     self.width, self.height, 0,
                     GL_RGB, GL_UNSIGNED_BYTE, self.raw_reference)

        glGenerateMipmap(GL_TEXTURE_2D)

        return texture_id


