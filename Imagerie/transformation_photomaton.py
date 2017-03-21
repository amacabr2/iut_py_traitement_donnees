import numpy as np
import pylab as P
from PIL import Image, ImageDraw


def setup():
    """
    Enregistre les pixels de l'image
    :return: listPixel
    """
    listPixel = []
    (largeur, hauteur) = im.size
    for x in range(largeur):
        for y in range(hauteur):
            listPixel.append(im.getpixel((x, y)))
    return [listPixel, largeur, hauteur]


def transforme():
    newImage = Image.new("L", (largeur, hauteur))
    for x in range(largeur):
        for y in range(hauteur):
            p = im.getpixel((x, y))
            q0 = p[0]
            q1 = p[1]
            q2 = p[2]
            newImage.putpixel((x, y), (q0, q1, q2))
    newImage.show()

if __name__ == '__main__':
    im = Image.open('img/joconde.jpg')
    im.show()
    tabPixel = setup()[0]
    largeur = setup()[1]
    hauteur = setup()[2]
    transforme()