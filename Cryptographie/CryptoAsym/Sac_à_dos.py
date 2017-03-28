from Cryptographie.NombrePremier.largeprime import genlargenb
from Cryptographie.NombrePremier.outils_arithmethique import pgcd


def lu(p):
    l = 0
    for i in p:
        l += i
    l += 1
    u = genlargenb(5)
    while pgcd(l, u) != 1:
        u = genlargenb(5)
    return (l, u)


def calculV(u, l):
    v = genlargenb(5)
    while (u * v) % l != 1:
        v = genlargenb(5)
    return v


def clefChiffrement(p, u, l):
    b = []
    for i in p:
        b.append((u * i) % l)
    return b


def chiffre(m, b, n):
    c = 0
    bits = str(bin(m))
    bits = bits.replace('0b', '')
    while len(bits) <= n:
        bits = '0' + bits
    for i in range(0, n):
        c += int(bits[i]) * b[i]
    return c


def dechiffre(c, v, l):
    return (v * c) % l


if __name__ == '__main__':
    # Suite supercroissante choisie arbitrairement pour l'exemple.
    p = [2, 3, 6, 15, 40, 100, 215, 570]

    # Travail préliminaire d'Alice
    (l, u) = lu(p)
    v = calculV(u, l)
    b = clefChiffrement(p, u, l)
    # Chiffrement de Bob
    m = 42  # Message pour l'exemple
    c = chiffre(m, b, len(p))
    # Dechiffrement d'Alice
    print(dechiffre(c, v, l))