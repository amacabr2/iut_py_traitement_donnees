def pgcd(a, b):
    """Calcul lePGCD"""
    if a % b == 0:
        return b
    else:
        return pgcd(b, a % b)


def ppcm(n):
    """Détermine le PPCM des nombres compris entre 2 et N"""
    if n < 2:
        raise ValueError("Le nombre doit être supérieur ou égale à deux.")
    nombres = list(range(2, n + 1))
    print(nombres)
    for i in range(2, n + 1):
        for nb in nombres:
            if nb % i == 0 and nb != i:
                nombres[i] = pgcd(nombres[i], i)
    return nombres

if __name__ == '__main__':
    try:
        print("Vous avez le choix entre le calcul du PGCD (1) ou du PPCM (2)")
        choix = int(input("Faite votre choix : "))
        if choix == 1:
            a = int(input("Donner une valeur a : "))
            b = int(input("Donner une valeur b : "))
            print("Le pgcd de {0} et {1} est : {2}".format(a, b, pgcd(a, b)))
        elif choix == 2:
            n = int(input("Donner un nombre N pour obtenir le PPCM des nombres compris entres 2 et N : "))
            print(ppcm(n))
        else:
            print("Il faut faire un choix entre 1 et 2")
    except ValueError:
        print("Il faut un nombre")