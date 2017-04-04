"""
Auteur: Anthony MACABREY S4A1
"""

from random import randint


def xor(caractere, entier):
    """Mise en place le chiffrement de Vernam, pour des textes binaires"""
    if caractere == str(entier):
        return "0"
    else:
        return "1"


if __name__ == '__main__':
    message = input("Quel texte chiffrer ? ")
    key = [randint(0, 1) for k in range(len(message))]
    print("Clé :", key)
    crypto = ''.join([xor(message[k], key[k]) for k in range(len(message))])
    print("Cryptogramme :", crypto)
    decypher = ''.join([xor(crypto[k], key[k]) for k in range(len(message))])
    print("Déchiffrement :", decypher)
