"""
Auteur: Anthony MACABREY S4A1
"""

import random

from Cryptographie.EnfanceDeLArt.Le_carre_de_25 import stringToCharTab, charTabtoString


def transposition_random():
    """chiffrement par transposition"""
    tabNewPosition = []  # Enregistre la nouvelle position de la lettre pour ne pas mettre une nouvelle lettre là où il y en a déjà
    tabChar = stringToCharTab(phrase) # Phrase transformé en tableau de caractères
    tabNewChar = [] # Nouvelle phrase
    # Donner la bonne taille au tableau
    for k in range(len(tabChar)):
        tabNewChar.append("A")
    i = 0
    # Transposer tous les caractères du tableau
    while i < len(tabChar):
        j = random.randint(0, len(tabChar) - 1)
        # La nouvelle position de la lettre doit être là où il n' y pas de nouvelle lettre
        if j in tabNewPosition:
            while j in tabNewPosition:
                j = random.randint(0, len(tabChar) - 1)
        else:
            # Changement de position
            tabNewChar[i] = tabChar[j]
            tabNewPosition.append(j)
            i += 1
    return charTabtoString(tabNewChar)


def transposition_fixe(decal):
    """Chiffrement par transposition selon le tp"""
    tabChar = stringToCharTab(phrase)
    tabNewChar = []  # Nouvelle phrase
    # Donner la bonne taille au tableau
    for k in range(len(tabChar)):
        tabNewChar.append("A")
    for i in range(len(tabChar)):
        num = i + 5
        if num >= len(tabChar):
            num -= len(tabChar)
        tabNewChar[num] = tabChar[i]
    return charTabtoString(tabNewChar)


def transposition_bloc():
    """Chiffrement par bloc: on déplace des blocs de lettres"""
    n = int(input("Quelle taille pour les blocs ? "))
    key = list(range(n))
    random.shuffle(key)
    print("La clé est :", key)
    message = input("Quel message chiffrer ? ")
    blocs = [message[n * k:n * (k + 1)] for k in range(int(len(message) / n))]
    crypto = [[blocs[k][u] for u in key] for k in range(len(blocs))]
    print("Cryptogramme :", ''.join(sum(crypto, [])))

if __name__ == '__main__':
    phrase = "Bonjour tout le monde"
    print("Transposition random ==========================================================================================")
    print(transposition_random())
    print("Transposition fixe ==========================================================================================")
    print(transposition_fixe(5))
    print("Transposition bloc ==========================================================================================")
    transposition_bloc()