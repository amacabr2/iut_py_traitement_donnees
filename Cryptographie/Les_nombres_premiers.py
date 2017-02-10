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