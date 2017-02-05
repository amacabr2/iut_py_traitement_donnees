from PIL import Image
from math import *


def r3(x):
    """ Racine cubique """
    if x < 0:
        return -pow(-x, 1.0 / 3)
    else:
        return pow(x, 1.0 / 3)


def negat(x):
    """Image effet négatif"""
    return 255 - x


def assombrissement(x):
    """Assombrit l'image"""
    return int(255 * pow((x / 255), 2))


def eclaircissement(x):
    """Eclairci l'image"""
    return int(255 * sqrt(x / 255))


def diminution_contraste(x):
    """Diminiue le contraste de l'image"""
    return int(127 + 127 * pow(((x - 127) / 127), 3))


def augmentation_contraste(x):
    """Augmente le contraste de l'image"""
    return int(127 + 127 * r3((x - 127) / 127))


def choix():
    """Demande à l'utilisateur de faire un choix"""
    while True:
        print("Tu as le choix en entre")
        print("\t - vision négative (1)")
        print("\t - assombrissement (2)")
        print("\t - écraircissement (3)")
        print("\t - diminution contraste (4)")
        print("\t - augmentation contraste (5)")
        choix = int(input("Alors ton choix : "))
        if 5 >= choix >= 1:
            return choix


"""====================================================Main=========================================================="""

toto = Image.open('img/joconde.jpg', 'r')
choix = choix()

for k in range(toto.size[0]):
    for l in range(toto.size[1]):
        X = toto.getpixel((k, l))
        if choix == 1:
            toto.putpixel((k, l), (negat(X[0]), negat(X[1]), negat(X[2])))
        elif choix == 2:
            toto.putpixel((k, l), (assombrissement(X[0]), assombrissement(X[1]), assombrissement(X[2])))
        elif choix == 3:
            toto.putpixel((k, l), (eclaircissement(X[0]), eclaircissement(X[1]), eclaircissement(X[2])))
        elif choix == 4:
            toto.putpixel((k, l), (diminution_contraste(X[0]), diminution_contraste(X[1]), diminution_contraste(X[2])))
        elif choix == 5:
            toto.putpixel((k, l), (augmentation_contraste(X[0]), augmentation_contraste(X[1]), augmentation_contraste(X[2])))

toto.show()

