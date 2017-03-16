def add1(x):
    """Ajoute un 1 à la fin de x"""
    return x + '1'


def add0(x):
    """Ajoute autant de 0 qu'il faut pour que la longueur de la suite binaire soit 512 - 64"""
    for i in range(512 - len(x) - 64):
        x += '0'
    return x


def binaireHexa(x):
    """Transforme a valeur binaire en valeur hexadecimal"""
    return hex(int(x, 2))


def normalisation(x, tailleOriginalX):
    """Transforme la longueur original de x  en base 2 comme un nombre de 64 bits : en représentation hexadécimale"""
    h = hex(tailleOriginalX)
    h = h.replace('0x', '')
    for i in range(16 - len(h)):
        h = '0' + h
    return x + h


def f(B, C, D, t):
    """Définit f(B, C, D) par rapport à t"""
    if t >= 0 and t <= 19:
        return (B & C) | (~B & D)
    if t >= 20 and t <= 39:
        return B ^ C ^ D
    if t >= 40 and t <= 59:
        return (B & C) | (B & D) | (C & D)
    if t >= 60 and t <= 79:
        return B ^ C ^ D


def rotLeft(n, x):
    """opération de rotation binaire par la gauche où x est un mot de 32 bits et 0 ≤ n ≤ 32 """
    return ((x << n) | (x >> n - 32)) & 0xffffffff


def constK(t):
    """Donne une valeur à K par rapport à t"""
    if t >= 0 and t <= 19:
        return '5A827999'
    if t >= 20 and t <= 39:
        return '6ED9EBA1'
    if t >= 40 and t <= 59:
        return '8F1BBCDC'
    if t >= 60 and t <= 79:
        return 'CA62C1D6'


def remplirM():
    """Remplir le tableau M"""
    k = 0
    cpt = 0
    while k < 16:
        l = 0
        M.append([])
        while l < 8:
            M[k].append(x[cpt])
            l += 1
            cpt += 1
        k += 1


def traiteBloc(n):
    """On traite successivement les N blocs de M"""
    for i in range(1, n):

        # On remplit le tableau W
        for t in range(16):
            W[t] = M[t][i]
        for t in range(16, 80):
            W[t] = rotLeft(1, W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16])

        # On initialise a, b, c, d et e avec les valeurs de hachage du tour précédent
        A = H0[i - 1]
        B = H1[i - 1]
        C = H2[i - 1]
        D = H3[i - 1]
        E = H4[i - 1]
        for t in range(79):
            T = rotLeft(5, A) + f(B, C, D, t) + E + constK(t) + W[t]
            E = D
            D = C
            C = rotLeft(30, B)
            B = A
            A = T

        # Calcul des valeurs de hachage intermédiaires
        H0[i] = A + H0[i - 1]
        H1[i] = B + H1[i - 1]
        H2[i] = C + H2[i - 1]
        H3[i] = D + H3[i - 1]
        H4[i] = E + H0[i - 1]

    return H0 + H1 + H2 + H3 + H4


H0 = '67452301'
H1 = 'EFCDAB89'
H2 = '98BADCFE'
H3 = '10325476'
H4 = 'C3D2E1F0'

A = '67452301'
B = 'EFCDAB89'
C = '98BAD89'
D = '10325476'
E = 'C3D2E1F0'

if __name__ == '__main__':
    W = [0] * 80
    M = []
    x = '0110000101100010011000110110010001100101'
    tailleOriginalX = len(x)
    x = add1(x)
    x = add0(x)
    x = binaireHexa(x)
    x = normalisation(x, tailleOriginalX)
    x = x.replace('0x', '')
    remplirM()
    print(traiteBloc(len(x)))
