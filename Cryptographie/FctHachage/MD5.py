"""
Auteur: Anthony MACABREY S4A1
"""

import math
from Cryptographie.FctHachage.LinkedList import LinkedList, Node


class MD5:
    def __init__(self, arg=None):
        """Initialisation pour l'implementation MD5"""
        self.H0 = 0x67452301
        self.H1 = 0xEFCDAB89
        self.H2 = 0x98BADCFE
        self.H3 = 0x10325476
        self.K = [int(math.floor(abs(math.sin(i + 1)) * pow(2, 32))) for i in range(64)]
        self.R = [
            7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
            5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 4,
            11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6,
            10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
        ]
        self.digestSize = 16
        self.list = LinkedList(None)
        if arg:
            self.list.add(Node(arg, None))
            self.traiteBlock(self.list.toString())
        else:
            self.traiteBlock(self.list.toString())

    def add0(self, message):
        """Ajoute des 0 tant qu'il le faut"""
        message += '\x00' * ((56 - len(message) % 64) % 64)
        return message

    def add1(self, message):
        """Ajoute un 1 """
        message += bin(1)
        return message

    def rotationLeft(self, n, x):
        """Rotation binaire par la gauche"""
        return (x << n) | (x >> (32 - n))

    def digest(self):
        res = b''
        buffers = [self.H0, self.H1, self.H2, self.H3]

        for buffer in buffers:
            bufferbytes = []
            b = bin(buffer).replace('b', '0')
            b = "0" * (34 - len(b)) + b

            bufferbytes.append(int(b[2:10], 2))
            bufferbytes.append(int(b[10:18], 2))
            bufferbytes.append(int(b[18:26], 2))
            bufferbytes.append(int(b[26:34], 2))

            res += bytes([bufferbytes[3]])
            res += bytes([bufferbytes[2]])
            res += bytes([bufferbytes[1]])
            res += bytes([bufferbytes[0]])

            return res

    def hexdigest(self):
        return ''.join(["{:02x}".format(byte) for byte in bytearray(self.digest())])

    def F(self, x, y, z):
        """XY v not(X) Z"""
        return (x & y) | ((~x) & z)

    def G(self, x, y, z):
        """XZ v Y not(Z)"""
        return (x & z) | (y & (~z))

    def H(self, x, y, z):
        """X xor Y xor Z"""
        return x ^ y ^ z

    def I(self, x, y, z):
        """Y xor (X v not(Z))"""
        return y ^ (x | (~z))

    def splitToBlock(self, message, n):
        """Création de blocs de 512 bits du message subdivisé en 16 mots de 32 bits"""
        return [message[i:i + n] for i in range(0, len(message), n)]

    def traiteBlock(self, blocks):
        """Gère les block"""

        for block in blocks:
            a = self.H0
            b = self.H1
            c = self.H2
            d = self.H3
            (e, f, g, h) = (0, 0, 0, 0)

            for i in range(63):
                if i >= 0 and i <= 15:
                    f = self.F(b, c, d)
                    g = i
                elif i >= 16 and i <= 31:
                    f = self.F(d, b, c)
                    g = (5 * i + 1) % 16
                elif i >= 32 and i <= 47:
                    f = self.H(b, c, d)
                    g = (3 * i + 5) % 16
                elif i >= 48 and i <= 63:
                    f = self.I(c, b, d)
                    g = (7 * i) % 16
                temp = d
                d = c
                c = b
                print(f)
                b = self.rotationLeft((int(a) + int(f) + int(self.K[i]) + int(block[g])), self.R[i] + b)
                a = temp

            self.H0 += a
            self.H1 += b
            self.H2 += c
            self.H3 += d

        return self.H0 + self.H1 + self.H2 + self.H3


if __name__ == '__main__':
    import hashlib

    content = "Wikipedia, l'encyclopedie libre et gratuite"
    c = ''
    print("La phrase qui va être hach : " + content)
    print("Avec la méthode de python : " + str(hashlib.md5(content.encode()).hexdigest()))
    for char in content:
        c += bin(ord(char))
    m = MD5(c)
    print("Avec ma méthode : " + str(m.hexdigest()))
