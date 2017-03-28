from Cryptographie.NombrePremier.largeprime import genererUnNombrePremier, estPremier
from math import sqrt
import random


def getP(n):
    """Va déterminer un grand nombre premier"""
    return genererUnNombrePremier(n)


def getG(p):
    """Détermine une racine prémitive modulo p"""
    for i in range(1000, p):
        if estPremier(i):
            return i


def getAouB(p):
    """On choisit 'a' ou 'b' au hasard entre 1 et p-1"""
    return random.randint(1, p - 1)


def calculAouB(g, ab, p):
    """Calcule A=g^a%p ou B=g^b%p"""
    return pow(g, ab, p)


def calculA(b, A):
    """Bob connaît b, et a reçu A, elle aura donc A^b=g^(ab)"""



def calculB(a, B):
    """Alice connaît a, et a reçu B, elle aura donc B^a=g^(ab)"""


if __name__ == '__main__':
    p = getP(10)
    g = getG(p)
    a = getAouB(p)
    A = calculAouB(g, a, p)
    b = getAouB(p)
    B = calculAouB(g, b, p)
    calculA(b, A)
    calculB(a, B)
