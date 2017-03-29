from random import randint

import Cryptographie.NombrePremier.largeprime as lg


def facteur(n):
    if n == 1:
        return set([])
    else:
        for k in range(2, int(n) + 1):
            if n % k == 0:
                L = facteur(n / k)
                return L.union([k])


def pg():
    p = lg.genererUnNombrePremier(2)
    g = 0
    phiP = p - 1
    facteurs = list(facteur(phiP))
    racinePrimitive = True
    for m in facteurs:
        for i in facteurs:
            if pow(m, int(phiP / i), p) == 1:
                racinePrimitive = False
                break
        if racinePrimitive:
            g = m
            break
    return p, g


def calculAouB(p, g):
    aoub = randint(0, p - 2)
    return (aoub, pow(g, aoub, p))


def cles(p, g, a):
    return ((p, g, pow(g, a, p)), a)


def chiffre(message, publique, b):
    (p, g, A) = publique
    return (pow(g, b, p), message * pow(A, b, p))


def dechiffre(cryptogramme, publique, prive):
    (p, g, A) = publique
    (B, c) = cryptogramme
    return (pow(B, (p - 1 - prive)) * c) % p


if __name__ == '__main__':
    (p, g) = pg()
    (a, A) = calculAouB(p, g)
    ((p, g, A), a) = cles(p, g, A)
    (b, B) = calculAouB(p, g)
    (B, c) = chiffre(42, (p, g, A), b)
    print(dechiffre((B, c), (p, g, A), a))