from math import sin
import hashlib


def remplirK():
    """Remplit K"""
    # MD5 utilise des sinus d'entiers pour ses constantes
    for i in range(64):
        K.append(int(abs(sin(i + 1)) * pow(2, 32)))


def rotateLeft(x, n):
    """Fait une rotation de x par n"""
    return (x << n) | (x >> (32 - n))


def padding(message):
    """Préparation du message"""
    message += '1'
    k = 0
    t = len(message)
    while k != 448 % 512 - t:
        message += '0'
        k += 1
    message += codeEn64Bit(len(message))
    return message


def codeEn64Bit(n):
    """Retourne la valeur en 64 bits"""
    b = bin(n)
    b = b.replace('0b', '')
    k = 0
    t = len(b)
    while k < 64 - t:
        b = '0' + b
        k += 1
    return b


def codeStringEnBinaire(message):
    """Tranforme la chaine de caractère en format binaire"""
    binaire = ""
    for char in message:
        binaire += bin(ord(char))
    binaire = binaire.replace('0b', '')
    return binaire


def blocs(message):
    """Découpage en blocs de 512 bits"""
    tabBloc = []
    k = 0
    while k < len(message):
        bloc = ""
        l = 0
        while l < 512:
            bloc += message[k]
            l += 1
            k += 1
        tabBloc.append(bloc)
    print(tabBloc)
    return tabBloc


def myMd5(blocs):
    """Fonction principale"""
    global K, h0, h1, h2, h3
    (a, b, c, d, e, f, g) = (0, 0, 0, 0, 0, 0, 0)

    for i in range(len(blocs)):

        # Initialisation des valeurs de hachages
        a = h0
        b = h1
        c = h2
        d = h3

        # Boucle pricipal
        for i in range(64):
            if i >= i and i <= 15:
                f = (b & c) | (~b & d)
                g = i
            elif i >= 16 and i <= 31:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif i >= 32 and i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            elif i >= 48 and i <= 63:
                f = c ^ (b | ~d)
                g = (7 * i) % 16
            temp = d
            d = c
            c = b
            b = ((a + f + K[i] + blocs[g]) * rotateLeft(R[i], 0)) + b

        h0 = h0 + a
        h1 = h1 + b
        h2 = h2 + c
        h3 = h3 + d

    return (h0 + h1 + h2 + h3) & 0xffffffff


R = [
    [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22],
    [5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20],
    [4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23],
    [6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]
]

K = []

# Péparationdes variables
h0 = int(0x67452301)
h1 = int(0xefcdab89)
h2 = int(0x98badcfe)
h3 = int(0x10325476)

if __name__ == '__main__':
    remplirK()
    phrase = "Wikipedia, l'encyclopedie libre et gratuite"
    binaire = codeStringEnBinaire(phrase)
    p = padding(binaire)
    print("La phrase à crypter est : " + phrase)
    print("Avec haslib on obtient : " + str(hashlib.md5(phrase.encode()).hexdigest()))
    print("Avec mon code on obtient : " + str(myMd5(p)))
