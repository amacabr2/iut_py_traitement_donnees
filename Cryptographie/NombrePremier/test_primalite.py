from Cryptographie.NombrePremier.Les_nombres_premiers import cribleDEratosthene


def test1AvecCribleEratosthene(n):
    """trouve les facteurs du nombre n avec les nombres premiers inférieurs à n"""
    crible = cribleDEratosthene(n)
    facteurs = []
    for c in crible:
        if n % c == 0:
            facteurs.append(c)
    return facteurs


def test1SansCribleEratosthene(n):
    """Trouveles facteurs du nombre n en testant seulement la divisibilité par 2 puis par les nombres imapirs"""
    facteurs = []
    if n % 2 == 0:
        facteurs.append(2)
    for i in range(n):
        if i % 2 != 0:
            if n % i == 0:
                facteurs.append(i)
    return facteurs


if __name__ == '__main__':
    n = int(input("Choisissez un nombre et on va calculer ces facteurs : "))
    print("Les facteurs (avec grille eratosthene) de {0} sont : {1}".format(n, test1AvecCribleEratosthene(n)))
    print("Les facteurs (sans grille eratosthene) de {0} sont : {1}".format(n, test1SansCribleEratosthene(n)))
