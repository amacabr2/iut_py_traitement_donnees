"""
Auteur: Anthony MACABREY S4A1
"""

from Cryptographie.EnfanceDeLArt.Le_carre_de_25 import stringToCharTab

CARRE_VIGENERE = [
    ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
    ["BCDEFGHIJKLMNOPQRSTUVWXYZA"],
    ["CDEFGHIJKLMNOPQRSTUVWXYZAB"],
    ["DEFGHIJKLMNOPQRSTUVWXYZABC"],
    ["EFGHIJKLMNOPQRSTUVWXYZABCD"],
    ["FGHIJKLMNOPQRSTUVWXYZABCDE"],
    ["GHIJKLMNOPQRSTUVWXYZABCDEF"],
    ["HIJKLMNOPQRSTUVWXYZABCDEFG"],
    ["IJKLMNOPQRSTUVWXYZABCDEFGH"],
    ["JKLMNOPQRSTUVWXYZABCDEFGHI"],
    ["KLMNOPQRSTUVWXYZABCDEFGHIJ"],
    ["LMNOPQRSTUVWXYZABCDEFGHIJK"],
    ["MNOPQRSTUVWXYZABCDEFGHIJKL"],
    ["NOPQRSTUVWXYZABCDEFGHIJKLM"],
    ["OPQRSTUVWXYZABCDEFGHIJKLMN"],
    ["PQRSTUVWXYZABCDEFGHIJKLMNO"],
    ["QRSTUVWXYZABCDEFGHIJKLMNOP"],
    ["RSTUVWXYZABCDEFGHIJKLMNOPQ"],
    ["STUVWXYZABCDEFGHIJKLMNOPQR"],
    ["TUVWXYZABCDEFGHIJKLMNOPQRS"],
    ["UVWXYZABCDEFGHIJKLMNOPQRST"],
    ["VWXYZABCDEFGHIJKLMNOPQRSTU"],
    ["WXYZABCDEFGHIJKLMNOPQRSTUV"],
    ["XYZABCDEFGHIJKLMNOPQRSTUVW"],
    ["YZABCDEFGHIJKLMNOPQRSTUVWX"],
    ["ZABCDEFGHIJKLMNOPQRSTUVWXY"]
]

if __name__ == '__main__':

    messageACrypter = input("Indiquer le message que vous voulez crypter : ")
    messagecrypter = ""

    tabMessageACrypter = stringToCharTab(messageACrypter)
    noAlphabet = 1

    # On crée une liste de liste selon le carre de vigenère
    for i in range(len(CARRE_VIGENERE)):
        CARRE_VIGENERE[i] = stringToCharTab(CARRE_VIGENERE[i][0])

    # Transformation
    for i in range(len(tabMessageACrypter)):
        for j in range(len(CARRE_VIGENERE[0])):
            print(j)
            if tabMessageACrypter[i] == CARRE_VIGENERE[0][j]:
                messagecrypter += CARRE_VIGENERE[noAlphabet][j]
                # On remet à 0 pour ne pas sortir du tableau
                if noAlphabet + 1 >= 26:
                    noAlphabet = 0
                noAlphabet += 1

    print(messagecrypter)
