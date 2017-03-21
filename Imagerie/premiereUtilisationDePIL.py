from PIL import Image, ImageDraw
import pylab as P
import numpy as np
from math import sqrt


def f1(x):
    return x


def f2(x):
    return -x + 255


def premierDessin():
    """Faire une croix (X)"""
    X = range(256)
    Y1 = [f1(x) for x in X]
    Y2 = [f2(x) for x in X]
    P.plot(X, Y1)
    P.plot(X, Y2)
    P.show()


def deuxiemeDessin():
    """Faire une croix (+)"""
    X = range(256)
    Y = [125 for x in X]
    P.bar(125, 250, width = 1.5, color = 'red')
    P.plot(X, Y)
    P.show()


def troisiemeDessin():
    """faire un carrée"""
    P.axis("equal")
    P.xlim(-1, 2)
    P.ylim(-1, 2)
    x = np.array([0, 1, 1, 0, 0])
    y = np.array([0, 0, 1, 1, 0])
    P.plot(x, y)
    P.show()


def ptCercle(a, b, r, x):
    """
    Retourne la position d'un point du cercle
    :param a:
    :param b:
    :param r:
    :param x:
    :return: y0
    """
    if pow(r, 2) > pow((x - a), 2):
        return b - sqrt(pow(r, 2) - pow(x - a, 2))
    else:
        return b + sqrt(pow(r, 2) - pow(x - a, 2))


def quartCercle():
    """
    Dessine un quart de cercle
    """
    X = range(1, 20)
    Y = [ptCercle(0, 20, 20, x) for x in X]
    P.plot(X, Y)
    P.show()


def cercle():
    """
    Dessine un cercle avec le module PIL
    """
    i = Image.new('L', (500, 500))
    draw = ImageDraw.Draw(i)
    draw.arc((150, 150, 350, 350), 0, 360, fill=128)
    i.show(command='eog')


def fourCercle():
    """
    Dessine 4 cercles chacun dans un quart du plan avec le modul PIL
    """
    i = Image.new('L', (500, 500))
    draw = ImageDraw.Draw(i)
    draw.line(((0, 250), (500, 250)), fill=128)
    draw.line(((250, 0), (250, 500)), fill=128)
    draw.arc((0, 0, 250, 250), 0, 360, fill=300)
    draw.arc((250, 0, 500, 250), 0, 360, fill=300)
    draw.arc((0, 250, 250, 500), 0, 360, fill=300)
    draw.arc((250, 250, 500, 500), 0, 360, fill=300)
    i.show(command='eog')

if __name__ == '__main__':
    premierDessin()
    deuxiemeDessin()
    troisiemeDessin()
    quartCercle()
    cercle()
    fourCercle()