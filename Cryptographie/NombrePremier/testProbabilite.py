from random import *


def testPrimaliteFermat(n, t):
    testes = []
    j = 0
    ret = True
    while j < t and ret:
        # choix de a 
        a = randint(1, n - 1)
        while a in testes:
            a = randint(1, n - 1)
        # calcul de a^(n-1) [n]
        # if a**(n-1) % n != 1 :
        if pow(a, n - 1, n) != 1:
            ret = False
        else:
            j += 1
            testes += [a]
    return ret


def testPrimaliteMillerRabin(n, t):
    testes = []
    if n % 2 == 0:
        return False

    # ecrire  n-1 comme 2**s * d
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d /= 2
    j = 0
    ret = True
    while j < t and ret:
        # choix de a 
        a = randint(1, n - 1)
        while a in testes:
            a = randint(1, n - 1)
        # calcul de a^(d) [n]
        if pow(a, int(d), n) != 1:
            ret = False
            r = 0
            while r < s and not ret:
                if pow(a, 2 ** r * int(d), n) == n - 1:
                    ret = True
                else:
                    r += 1
        j += 1
        testes += [a]
    return ret


if __name__ == '__main__':

    n = 561
    print(n)
    print("probabilite d'etre premier (FERMAT)", testPrimaliteFermat(n, 500))
    print("probabilite d'etre premier (Miller Rabin)", testPrimaliteMillerRabin(n, 3))

    n = 39341
    print(n)
    print("probabilite d'etre premier (FERMAT)", testPrimaliteFermat(n, 500))
    print("probabilite d'etre premier (Miller Rabin)", testPrimaliteMillerRabin(n, 30))

    n = 651693055693681  # il ne l'est pas
    print(n)
    print("probabilite d'etre premier (FERMAT)", testPrimaliteFermat(n, 500))
    print("probabilite d'etre premier (Miller Rabin)", testPrimaliteMillerRabin(n, 500))

    n = 1000000000000037  # il est premier
    print(n)
    print("probabilite d'etre premier (FERMAT)", testPrimaliteFermat(n, 500))
    print("probabilite d'etre premier (Miller Rabin)", testPrimaliteMillerRabin(n, 500))
