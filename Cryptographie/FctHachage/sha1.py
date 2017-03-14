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


if __name__ == '__main__':
    x = '0110000101100010011000110110010001100101'
    tailleOriginalX = len(x)
    x = add1(x)
    x = add0(x)
    x = binaireHexa(x)
    x = normalisation(x, tailleOriginalX)
    x.replace('0x', '')
    print(x)
