import random
import math
import sys

PREMIERNBRPREMIER = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        , 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179
        , 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269
        , 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367
        , 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461
        , 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571
        , 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661
        , 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773
        , 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883
        , 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def rabinMiller(n):
    s = n - 1
    t = 0
    while s and 1 == 0:
        s /= 2
        t += 1
    k = 0
    while k < 128:
        a = random.randrange(2, n - 1)
        v = pow(a, s, n)
        if v != 1:
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i += 1
                    v = (v ** 2) % n
        k += 2
    return True


def estPremier(n):
    if n >= 3:
        if n & 1 != 0:
            for p in PREMIERNBRPREMIER:
                if n == p:
                    return True
                if n % p == 0:
                    return False
            return rabinMiller(n)
    return False


def genlargenb(n):
    a = 1
    for i in range(1, n):
        a *= 10
    b = a * 10
    g = random.randint(a, b)
    ld = g % 10
    while (ld == 2 or ld == 5 or ld == 6 or ld == 8 or ld == 4 or ld == 0):
        g -= 1
        ld = g % 10

    return g


def genererUnNombrePremier(n):
    # k est le nombre de chiffre
    nbEssai = 100 * (math.log(n, 2) + 1)  # nombre maximum d essai
    r_ = nbEssai
    while nbEssai > 0:
        nb = genlargenb(n)
        nbEssai -= 1
        if estPremier(nb) == True:
            return nb
    return "Echec apres " + repr(r_)


def pgcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def genererClefsPublic(n, phi):
    e = genlargenb(30)
    while (e < 1 or e > phi):
        e = genlargenb(30)
    g = pgcd(e, phi)
    while g != 1:
        e = genlargenb(30)
        while (e < 1 or e > phi):
            e = genlargenb(30)
        g = pgcd(e, phi)
    return e


def bezout(a, b):
    if b == 0:
        return [1, 0]
    else:
        uv = bezout(b, a % b)
    return [uv[1], uv[0] - uv[1] * (a / b)]


def calculD(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = bezout(e, d)[0]
        y = bezout(e, d)[1]

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def chiffrer(d, n, plaintext):
    return math.pow(plaintext, e, n)

if __name__ == '__main__':

    p = genererUnNombrePremier(100)
    q = genererUnNombrePremier(100)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = genererClefsPublic(n, phi)

    d = calculD(e, phi)
    msgChif = chiffrer(d, n, 3402752281514000316845)
    print(msgChif)
