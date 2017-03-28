import math


class MD5:
    def __init__(self):
        """Initialisation pour l'implementation MD5"""
        self.A = 0x67452301
        self.B = 0xEFCDAB89
        self.C = 0x98BADCFE
        self.D = 0x10325476
        self.K = [int(math.floor(abs(math.sin(i + 1)) * pow(2, 32))) for i in range(64)]
        self.R = [
            7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
            5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 4,
            11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6,
            10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
        ]
        self.digestSize = 16

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
