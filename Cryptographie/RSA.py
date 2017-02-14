from random import random


def bezout(a, b):
    if b == 0:
        return (a, 1, 0)

    q = a // b
    r = a % b
    (g, u, v) = bezout(b, r)
    return (g, v, u - q * v)


def clef(P1, P2):
    n = P1 * P2
    c = int(random())
    (r, u, v) = bezout(c, (P1 - 1) * (P2 - 1))
    while r != 1:
        c += 1
        (r, u, v) = bezout(c, (P1 - 1) * (P2 - 1))
    return [(n, c), u]


print(clef(5, 7))