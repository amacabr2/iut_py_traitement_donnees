from PIL import Image
import pylab as P


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
    P.xlim(0, 35)
    P.ylim(0, 40)
    X = range(10, 26)
    Y1 = [10 for x in X]
    Y2 = [30 for x in X]
    P.plot(X, Y1)
    P.plot(X, Y2)
    P.bar(10, 20, bottom=10, width=0.2, color='red')
    P.bar(25, 20, bottom=10, width=0.2, color='blue')
    P.show()

#premierDessin()
#deuxiemeDessin()
troisiemeDessin()