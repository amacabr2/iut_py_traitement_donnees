"""
Auteur: Anthony MACABREY S4A1
"""

from PIL import Image, ImageOps
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


def mise_en_val_color(x):
    """Permet de mettre en valeur soi la couleur verte, soi la couleur roue soi la couleur bleu"""
    return x + 100


def gris():
    """Met l'image en noir et blanc"""
    return ImageOps.grayscale(im)


def choix():
    """Demande à l'utilisateur de faire un choix"""
    while True:
        print("Tu as le choix en entre")
        print("\t - vision originale (0)")
        print("\t - vision négative (1)")
        print("\t - assombrissement (2)")
        print("\t - écraircissement (3)")
        print("\t - diminution contraste (4)")
        print("\t - augmentation contraste (5)")
        print("\t - mise en valeur du rouge (6)")
        print("\t - mise en valeur du vert (7)")
        print("\t - mise en valeur du bleu (8)")
        print("\t - noir et blanc (9)")
        choix = int(input("Alors ton choix : "))
        if choix >= 0 and choix <= 9:
            return choix


"""====================================================Main=========================================================="""
if __name__ == '__main__':

    im = Image.open('img/joconde.jpg', 'r')
    choix = choix()

    for k in range(im.size[0]):
        for l in range(im.size[1]):
            X = im.getpixel((k, l))
            if choix == 0:
                break
            elif choix == 1:
                im.putpixel((k, l), (negat(X[0]), negat(X[1]), negat(X[2])))
            elif choix == 2:
                im.putpixel((k, l), (assombrissement(X[0]), assombrissement(X[1]), assombrissement(X[2])))
            elif choix == 3:
                im.putpixel((k, l), (eclaircissement(X[0]), eclaircissement(X[1]), eclaircissement(X[2])))
            elif choix == 4:
                im.putpixel((k, l), (diminution_contraste(X[0]), diminution_contraste(X[1]), diminution_contraste(X[2])))
            elif choix == 5:
                im.putpixel((k, l), (augmentation_contraste(X[0]), augmentation_contraste(X[1]), augmentation_contraste(X[2])))
            elif choix == 6:
                im.putpixel((k, l), (mise_en_val_color(X[0]), X[1], X[2]))
            elif choix == 7:
                im.putpixel((k, l), (X[0], mise_en_val_color(X[1]), X[2]))
            elif choix == 8:
                im.putpixel((k, l), (X[0], X[1], mise_en_val_color(X[2])))
            elif choix == 9:
                im = gris()

    im.show()
