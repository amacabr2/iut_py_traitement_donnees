import Cryptographie.NombrePremier.largeprime as lg
import Cryptographie.NombrePremier.outils_arithmethique as oa


def lu(p):
    l = 0
    for i in p:
        l += i
    l += 1
    u = lg.genlargenb(5)
    while oa.pgcd(l, u) != 1:
        u = lg.genlargenb(5)
    return (l, u)


if __name__ == '__main__':
    # Suite supercroissante choisie arbitrairement pour l'exemple.
    p = [2, 3, 6, 15, 40, 100, 215, 570]
    # Travail préliminaire d'Alice
    (l, u) = lu(p)