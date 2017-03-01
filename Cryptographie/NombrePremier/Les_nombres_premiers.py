from math import sqrt


def cribleDEratosthene(n):
    if n < 2:
        raise ValueError("Le nombre doit être supérieur ou égale à deux.")

    nombres = list(range(2, n))
    for i in range(2, int(sqrt(n))):
        for nb in nombres:
            if nb % i == 0 and nb != i:
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


COLORS = ["\033[1;41m", "\033[31m", "\033[1;42m", "\033[1;32m", "\033[1;43m", "\033[1;33m", "\033[1;44m", "\033[1;34m",
          "\033[1;45m", "\033[1;35m", "\033[1;46m", "\033[1;36m", "\033[1;47m", "\033[1;37m"]
RESET = "\033[0m"


def colorArith(nbPremiers):
    tabStringPremiers = []
    rangColor = 0
    i = 0
    j = 1
    for k in range(2, len(nbPremiers)):
        arithm = False
        if nbPremiers[j] - nbPremiers[i] == nbPremiers[k] - nbPremiers[j]:
            tabStringPremiers.append(COLORS[rangColor])
            arithm = True
        if nbPremiers[i] not in tabStringPremiers:
            tabStringPremiers.append(nbPremiers[i])
        if nbPremiers[j] not in tabStringPremiers:
            tabStringPremiers.append(nbPremiers[j])
        if nbPremiers[k] not in tabStringPremiers:
            tabStringPremiers.append(nbPremiers[k])
        if arithm:
            tabStringPremiers += RESET
            rangColor += 1
            if rangColor == len(COLORS):
                rangColor = 0
        i += 1
        j += 1

    string = ""
    for stringPremier in tabStringPremiers:
        if str(stringPremier).isdigit():
            string += str(stringPremier) + " ; "
        else:
            string += stringPremier + " "
    print(string)

if __name__ == '__main__':
    colorArith(cribleDEratosthene(100))