from math import sqrt


def lireFichier(file):
    """Lit le texte dans le fichier passé en paramètre"""
    fichier = open(file)
    texte = fichier.readlines()
    return texte[0]


def recupLettreValable(text):
    """Retire les espaces et les carctères tel que '.', ',', ':' etc """
    for t in text:
        if t != " " and t != "," and t != "'" and t != "-" and t != "." and t != ":" and t != ";" and t != "’":
            lettreValable.append(t.upper())


def creerMatrice():
    """Créer la matrice avec les lettres"""
    taille = int(sqrt(len(lettreValable) / ecartLettre)) + 1
    cpt = 1
    for i in range(taille):
        matrice.append([])
        j = 0
        while j < taille:
            if cpt % ecartLettre == 0:
                try:
                    matrice[i].append(lettreValable[cpt - 1])
                    j += 1
                except IndexError:
                    return matrice
            cpt += 1
    return matrice


def rechercheMotDansMatrice():
    """Demande le mot que l'on veut rechercher et regarde si c'est dans la matrice"""
    mot = input("Quel est le mot que vous voulez rechercher dans la matrice ? ")
    if rechercheHorizontale(mot):
        print("Le mot '", mot, "' se trouve dans la matrice à l'horizontale")
    elif rechercheVerticale(mot):
        print("Le mot '", mot, "' se trouve dans la matrice à la verticale")
    else:
        print("Le mot '", mot, "' ne se trouve pas dans la matrice")


def rechercheHorizontale(mot):
    """Fait la recherche du mot en horizontale"""
    for i in range(len(matrice)):
        motAConstruire = ""
        for j in range(len(matrice[i])):
            motAConstruire += matrice[i][j]
            if mot.upper() in motAConstruire:
                return True
    return False


def rechercheVerticale(mot):
    """Fait la recherche à la verticale"""
    i, j = 0, 0
    motAConstruire = ""
    while j < len(matrice):
        if i + 1 < len(matrice):
            motAConstruire += matrice[i][j]
            if mot.upper() in motAConstruire:
                return True
            i += 1
        else:
            i = 0
            j += 1
    return False


lettreValable = []
matrice = []

if __name__ == '__main__':
    t = lireFichier('./bible.txt')
    print(t)
    ecartLettre = 1
    try:
        ecartLettre = int(input("Qu'elle écart entre chaque lettre ? "))
        if ecartLettre == 0:
            print("Non")
        else:
            recupLettreValable(t)
            matrice = creerMatrice()
            print(matrice)
            rechercheMotDansMatrice()
    except ValueError:
        print("Il faut un entier")
