from math import sqrt, log
from Cryptographie.NombrePremier.largeprime import estPremier, PREMIERNBRPREMIER
from Cryptographie.NombrePremier.testProbabilite import testPrimaliteFermat, testPrimaliteMillerRabin
import time


def nbrFermat(n):
    """Génère une liste avec les nombres de Fermat jusqu'a N"""
    tabNbrFermat = []
    for i in range(n):
        tabNbrFermat.append(pow(2, pow(2, i)) + 1)
    return tabNbrFermat


def isPremierFermat(tab):
    """Va déterminer si les nombres de Fermat de la liste sont premiers"""
    tabIsPremier = []
    t = 100
    for nbr in tab:
        # recherche dans un tableau contenant les 100 premiers nombres premiers
        if nbr in PREMIERNBRPREMIER:
            tabIsPremier.append(True)
        elif testPrimaliteFermat(nbr, t) and testPrimaliteMillerRabin(nbr, t):
            tabIsPremier.append(True)
        else:
            tabIsPremier.append(False)
    return tabIsPremier


def mersenne(n):
    """Calcul un nombre de mersenne"""
    return pow(2, n) - 1


def isPremierMersenneDirect(n):
    """Va déterminé si le nombre de Mersenne est premier avec la méthode direct"""
    l = len(bin(n))
    print("l = " + str(l))
    if estPremier(l - 2):
        return True
    return False


def isPremierEdouardLucas(n):
    """Va déterminer si le nombre de Mersenne est premier avec la technique d'Edouaed Lucas"""
    if m in PREMIERNBRPREMIER:
        return True
    elif getS(n - 2, mersenne(n)) % mersenne(n) == 0:
        return True
    return False


def getS(n, m):
    """Calcule la suite Sn nécéssaire pour savoir si un nombre de mersenne est premier"""
    S, k = 4, 0
    while k < n:
        S = (pow(S, 2) - 2) % m
        k += 1
    return S


if __name__ == '__main__':
    try:
        n = int(input(
            "Donner un nombre et on va en déduire la liste des nombres de Fermat (le nombre peut très vite grandir, "
            "n'exagérez pas): "))
        print("Voici la liste des nombres de Fermat pour {0} : {1}".format(n, nbrFermat(n)))
        print("Voici un tableau qui indique si les nombres de la liste sont premier : ", str(isPremierFermat(nbrFermat(n))))
        n = int(input(
            "Maintenant donnez un nombre n pour calculer le nombre de Mersenne Mn = 2^n - 1: "))
        m = mersenne(n)
        print("On va maintenant calculer le nombre de mersenne avec {0} : {1}".format(n, m))
        print("{0} est-il un nombre premier d'après la méthode direct: {1}".format(m, isPremierMersenneDirect(m)))
        print("{0} est-il un nombre premier d'après la méthode d'Edouard Lucas : {1}".format(m, isPremierEdouardLucas(n)))
    except ValueError:
        print("Il faut un nombre")
