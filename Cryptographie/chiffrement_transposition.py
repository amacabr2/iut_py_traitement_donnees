from Cryptographie.Le_carre_de_25 import stringToCharTab, charTabtoString
import random


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
    print("tabChar : " + str(len(tabChar)) + ", tabNewChar: " + str(len(tabNewChar)))
    for i in range(len(tabChar)):
        num = i + 5
        print("Ancienne position : " + str(i) + ", nouvelle position : " + str(num))
        if num >= len(tabChar):
            print("num : " + str(num))
            num -= len(tabChar)
        tabNewChar[num] = tabChar[i]
    return charTabtoString(tabNewChar)


phrase = "Bonjour tout le monde"
# print(transposition_random())
print(transposition_fixe(5))