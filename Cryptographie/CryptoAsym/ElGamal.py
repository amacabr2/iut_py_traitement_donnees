from random import randint

import Cryptographie.NombrePremier.largeprime as lg


def facteur(n):
    if n == 1:
        return set([])
    else:
        for k in range(2, n + 1):
            if n % k == 0:
                L = facteur(n / k)
                return L.union([k])


def pg():
    p = lg.genererUnNombrePremier(100)
    g = None
    phiP = p - 1
    facteurs = list(facteur(phiP))
    racinePrimitive = True
    for m in facteurs:
        for i in facteurs:
            if pow(m, phiP / i, p) == 1:
                racinePrimitive = False
                break
        if racinePrimitive:
            g = m
            break
    return (p, g)


def calculA(p, g):
    return pow(g, randint(0, p - 2), p)


def clefPublique():
    p, g = pg()
    return (p, g, calculA(p, g))