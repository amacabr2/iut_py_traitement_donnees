from PIL import Image
import os, sys


def fctDeBAse():
    im = Image.open('img/dark_vador.jpg')
    im = im.rotate(180)
    im.save('img/dark_vador.png', 'PNG')
    im.show(command='eog')
    print(im.format, "%dx%d" % im.size, im.mode)


def manipPixel():
    toto = Image.new('1', (256, 256), color=255)
    print(toto.getpixel((15, 34)))
    toto.putpixel((128, 128), 0)
    toto.save('img/letoto.jpg', 'JPEG')


def symetrieImg():
    im = Image.open('img/graphe.png')
    im.show()
    box = (0, 0, 96, 85)
    region = im.crop(box)
    region.show()
    region = region.transpose(Image.ROTATE_180)
    region.show()
    im.paste(region, box)
    im.show()


def createVignette(fichier):
    for fichierEntree in fichier:
        fichierSortie = os.path.splitext(fichierEntree)[0] + ".thumbnail"
        if fichierEntree != fichierSortie:
            try:
                im = Image.open(fichierEntree)
                im.thumbnail((128, 128))
                im.save(fichierSortie, "JPEG")
            except IOError:
                print("Ne peut creer une imagette pour ", fichierEntree)


fctDeBAse()
manipPixel()
symetrieImg()
createVignette(['img/dark_vador.png'])