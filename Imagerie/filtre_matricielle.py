"""
Auteur: Anthony MACABREY S4A1
"""

from PIL import Image, ImageOps
import numpy as np


def pixel_image():
    """Récupère les pixels de l'image"""
    for x in range(hauteur):
        for y in range(largeur):
            pixel.append(joconde.getpixel((x, y)))


def flou_uniforme():
    print(pixel[0])
    for i in range(len(pixel)):
        tuple([0.2 * x for x in pixel[i]])
    print(pixel[0])

if __name__ == '__main__':

    joconde = Image.open('img/joconde.jpg')
    (hauteur, largeur) = joconde.size
    pixel = []
    pixel_image()
    flou_uniforme()
    joconde = Image.new(pixel, joconde.size)