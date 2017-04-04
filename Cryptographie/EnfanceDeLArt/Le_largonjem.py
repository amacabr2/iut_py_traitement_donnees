"""
Auteur: Florent MARTIN S4A1
"""

from Cryptographie.AgeClassique.chiffrement_subtitution import ALPHABET
from Cryptographie.EnfanceDeLArt.Le_carre_de_25 import stringToCharTab, charTabtoString

CONSONNES = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']


def largonjem(message):
    """
    Ajoute 'L' devant chaque consonne
    Ajoute 'EM' après chaque consonne
    """
    tab_message = stringToCharTab(message)
    tab_message.reverse()
    consonne = tab_message.pop()
    tab_message.append("L")
    tab_message.reverse()
    tab_message.append(consonne + "EM")
    return charTabtoString(tab_message)


def isLargonjemisable(mot):
    """Regarde si la lettre est une consonne"""
    if mot[0].upper() in CONSONNES:
        return True
    return False


def transformeTexteToLargonjem(text):
    """Applique la transformation de Largonjem sur tout un texte"""
    tab_text = text.split(' ')
    text_crypte = ""
    for mot in tab_text:
        # On regarde si le caractère est une lettre de l'alphabet
        if mot[0].upper() in ALPHABET:
            if isLargonjemisable(mot):
                text_crypte += largonjem(mot)
            else:
                text_crypte += mot.upper()
        else:
            text_crypte += mot
        text_crypte += " "
    return text_crypte

if __name__ == '__main__':
    print(transformeTexteToLargonjem("bonjour à tous je suis enchanté"))
