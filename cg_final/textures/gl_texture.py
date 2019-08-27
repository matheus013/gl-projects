import array
import random

import numpy
from PIL import Image


class Texture(object):
    """Texture either loaded from a file or initialised with random colors."""

    def __init__(self):
        self.width, self.height = 0, 0
        self.raw_reference = None


class RandomTexture(Texture):
    """Image with random RGB values."""

    def __init__(self, xSizeP, ySizeP):
        self.xSize, self.ySize = xSizeP, ySizeP
        tmpList = [random.randint(0, 255) \
                   for i in range(3 * self.xSize * self.ySize)]
        self.texture_array = array.array('B', tmpList)
        self.raw_reference = self.texture_array.tostring()


class FileTexture(Texture):
    """Texture loaded from a file."""

    def __init__(self, fileName):
        img = Image.open(fileName, 'r').transpose(Image.FLIP_TOP_BOTTOM)
        self.width, self.height = img.size

        self.raw_reference = numpy.array(list(img.getdata()), numpy.uint8)
