from math import sqrt


def cribleDEratosthene(n):
    if n < 2:
        raise ValueError("Le nombre doit être supérieur ou égale à deux.")

    nombres = list(range(2, n))
    for i in range(2, int(sqrt(n))):
        for nb in nombres:
            if nb % i == 0:
                nombres.remove(nb)

    return nombres


def nbPremiersJumeaux(nbPremiers):
    lNbPremiersJumeaux = []
    i = 0
    for j in range(1, len(nbPremiers)):
        if nbPremiers[i] + 2 == nbPremiers[j]:
            lNbPremiersJumeaux.append([nbPremiers[i], nbPremiers[j]])
        i += 1
    return lNbPremiersJumeaux