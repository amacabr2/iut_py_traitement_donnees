from PIL import Image
import os, sys


def fctDeBase():
    """
     Ouvre une image, la retourne à 180°, l'enregistre en changeant son extension et l'affiche
    """
    im = Image.open('img/dark_vador.jpg')
    im = im.rotate(180)
    im.save('img/dark_vador.png', 'PNG')
    im.show(command='eog')
    print(im.format, "%dx%d" % im.size, im.mode)


def manipPixel():
    """
    Manipule des pixels et créer une image
    """
    toto = Image.new('1', (256, 256), color=255)
    print(toto.getpixel((15, 34)))
    toto.putpixel((128, 128), 0)
    toto.save('img/letoto.jpg', 'JPEG')


def symetrieImg():
    """
    faire une symétrie à une partie d'une image
    """
    im = Image.open('img/graphe.png')
    im.show()
    #  on sélectionne une boîte (entre les pixels de coordonnées (0 ;0) et ceux de coordonnées (96 ;85))
    box = (0, 0, 96, 85)
    # on met dans region la partie d'image corespondant à cette boîte
    region = im.crop(box)
    region.show()
    #  on remplace la region considérée par sa rotation de 180 degré
    region = region.transpose(Image.ROTATE_180)
    region.show()
    # on recole cette région dans notre image, à la position souhaitée
    im.paste(region, box)
    im.show()


def createVignette(fichier):
    """
    Le but est d'obtenir des imagettes (128x128 pixels) de l'ensemble
     des images passées en argument du programme toto (saisi dans un éditeur de texte)
    :param fichier:
    """
    for fichierEntree in fichier:
        fichierSortie = os.path.splitext(fichierEntree)[0] + ".thumbnail"
        if fichierEntree != fichierSortie:
            try:
                im = Image.open(fichierEntree)
                im.thumbnail((128, 128))
                im.save(fichierSortie, "JPEG")
            except IOError:
                print("Ne peut creer une imagette pour ", fichierEntree)


"""Main"""
fctDeBase()
manipPixel()
symetrieImg()
createVignette(['img/dark_vador.png'])