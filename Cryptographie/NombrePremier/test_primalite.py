from Cryptographie.NombrePremier.Les_nombres_premiers import cribleDEratosthene
import time


def test1AvecCribleEratosthene(n):
    """trouve les facteurs du nombre n avec les nombres premiers inférieurs à n"""
    crible = cribleDEratosthene(n)
    print(crible)
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


def fact(n):
    """Calcul de factorielle"""
    x = 1
    for i in range(2, n + 1):
        x *= i
    print(x)
    return x


def testWilson(n):
    """Effectue le test de Wilson pour savoir si un nombre est premier"""
    if (fact(n - 1) + 1) % n == 0:
        return True
    return False


def testChinois(n):
    """Effectue le test chinois pour savoir si un nombre est premier"""
    if (pow(2, n) - 2) % n == 0:
        return True
    return False


def testPetitThFermat(n):
    """Effectue le test du petit théorème de Fermat pour savir si le nombre est pseudo-premier"""
    listA = [2, 3, 5, 7]
    pseudoPremierEnA = []
    for a in listA:
        if (pow(a, n) - a) % n == 0:
            pseudoPremierEnA.append(a)
    return pseudoPremierEnA


def getNbrPremierEntreNetDoubleN(n):
    """Cherche le 1er nombre premier entre n et 2n"""
    for i in range(n, 2 * n + 1):
        listA = [2, 3, 5, 7]
        pseudoPremierEnA = []
        for a in listA:
            if i == a:
                return i
            if (pow(a, i) - a) % i == 0:
                pseudoPremierEnA.append(a)
                if len(pseudoPremierEnA) == 4:
                    return i


if __name__ == '__main__':
    try:

        print(
            "Vous avez le choix entre le calcul de facteur avec un test de primalite (1), \n"
            "savoir si un nombre est premier avec le test de Wilson puis le test chinois (2)\n "
            "le test avec le petit théorème de Fermat (3)\n"
            "ou chercher un nombre premier entre un nombre que vous aurez choisit et son double (4)\n"
        )
        choix = int(input("Faite votre choix : "))

        if choix == 1:
            n = int(input("Choisissez un nombre, on va calculer ces facteurs : "))
            print("Les facteurs (avec grille eratosthene) de {0} sont : {1}".format(n, test1AvecCribleEratosthene(n)))
            print("Les facteurs (sans grille eratosthene) de {0} sont : {1}".format(n, test1SansCribleEratosthene(n)))

        elif choix == 2:

            n = int(input("Choisissez un nombre est on verra s'il est premier : "))

            t = time.time()
            if testWilson(n):
                print("{0} est un nombre premier selon le test de Wilson".format(n))
            else:
                print("{0} n'est pas un nombre premier selon le test de Wilson".format(n))
            print("Tps  éxécution de la fct testWilson : ", time.time() - t)

            t = time.time()
            if testChinois(n):
                print("{0} est un nombre premier selon le test chinoit".format(n))
            else:
                print("{0} n'est pas un nombre premier selon le test chinoit".format(n))
            print("Tps  éxécution de la fct testChinois : ", time.time() - t)

        elif choix == 3:
            n = int(input("Choisissez un nombre est on verra avec quoi il est pseudo premier : "))
            print("{0} est pseudo-premier avec a = {1}".format(n, testPetitThFermat(n)))

        elif choix == 4:
            n = int(input("Donner un nombre on va chercher un nombre premier entre ce nombre et son double : "))
            print("Entre {0} et {1} nous avons comme premier nombre premier {2}"
                  .format(n, n * 2, getNbrPremierEntreNetDoubleN(n)))

        else:
            print("Il faut faire un choix entre 1, 2, 3, 4")

    except ValueError:
        print("Il faut un nombre")
