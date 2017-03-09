from math import sqrt

from Cryptographie.NombrePremier.largeprime import estPremier, PREMIERNBRPREMIER
from Cryptographie.NombrePremier.testProbabilite import testPrimaliteFermat, testPrimaliteMillerRabin


def nbrFermat(n):
    """Génère une liste avec les nombres de Fermat jusqu'a N"""
    tabNbrFermat = []
    for i in range(n):
        tabNbrFermat.append(pow(2, pow(2, i)) + 1)
    return tabNbrFermat


def isPremier(tab):
    """Va déterminer si les nombres de Fermat de la liste sont premiers"""
    tabIsPremier = []
    t = 100
    for nbr in tab:
        if nbr in PREMIERNBRPREMIER:
            tabIsPremier.append(True)
        elif testPrimaliteFermat(nbr, t) and testPrimaliteMillerRabin(nbr, t):
            tabIsPremier.append(True)
        else:
            tabIsPremier.append(False)
    return tabIsPremier


if __name__ == '__main__':
    try:
        n = int(input(
            "Donner un nombre et on va en déduire la liste des nombres de Fermat (le nombre peut très vite grandir, "
            "n'éxagéré pas): "))
        print("Voici la liste des nombres de Fermat pour {0} : {1}".format(n, nbrFermat(n)))
        print("Voici un tableau qui indique si les nombres de la liste sont premier : ", str(isPremier(nbrFermat(n))))
    except ValueError:
        print("Il faut un nombre")
