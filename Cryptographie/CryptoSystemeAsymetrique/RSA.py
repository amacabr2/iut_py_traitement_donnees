from random import random
import Cryptographie.NombrePremier.largeprime as largeprime


def bezout(a, b):
    coeff = largeprime.bezout(a, b)
    return [largeprime.pgcd(a, b), coeff[0], coeff[1]]


def clef(P1, P2):
    n = P1 * P2
    c = int(random())
    r, u, v = bezout(c, (P1 - 1) * (P2 - 1))
    while r != 1:
        c += 1
        r, u, v = bezout(c, (P1 - 1) * (P2 - 1))
    return [(n, c), u]


if __name__ == '__main__':
    print(clef(73, 97))