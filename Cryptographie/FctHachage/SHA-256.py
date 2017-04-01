import struct


class SHA256(object):
    def __init__(self, m):
        """Initialisation"""
        #  utiisation de 64 constantes de 32 bits
        self.K = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
            0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
            0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
            0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
            0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
            0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
            0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
            0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
            0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]
        # état initial du système de 8 mots de 32 bits
        self.H = [
            0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
        ]
        if m is not None:
            l = len(m)
            if type(m) is not str:
                raise TypeError('%s() argument 1 must be string, not %s' % (self.__class__.__name__, type(m).__name__))
            c = self.update(m)
            c = self.add1(c)
            c = self.add0(c, l)
            c = self.addTailleL(c, l)
            self.gereBlock(c)

    def rotationRigth(self, x, y):
        """l'opération qui consiste à faire une permutation circulaire vers la droite, et qui décale de n positions
        les bits de x """
        return ((x >> y) | (x << (32 - y))) & 0xFFFFFFFF

    def rotationLeft(self, x, y):
        """l'opération qui consiste à faire une permutation circulaire vers la gauche, et qui décale de n positions
        les bits de x """
        return (x << y) | (x >> (32 - y)) & 0xFFFFFFFF

    def update(self, m):
        """Transforme le message pour qu'il soit utilisable par le code"""
        buffer = ''
        for char in m:
            buffer += bin(ord(char))
        buffer = buffer.replace('0b', '')
        return buffer

    def add1(self, message):
        """Ajoute un 1 en binaire à la fin du message"""
        message += bin(1)
        message = message.replace('0b', '')
        return message

    def add0(self, message, l):
        """Ajoute des 0 tant qu'il le faut"""
        k = (448 - l - 1) % 512
        i = 0
        while i < k:
            message += '0'
            i += 1
        message = message.replace('0b', '')
        return message

    def addTailleL(self, message, l):
        """Ajoute 64 bits représentant l'écriture du nombre l en binaire
        l est la taille de base du mmessage"""
        taille = bin(l)
        taille = taille.replace('0b', '')
        message += taille
        return message

    def gereBlock(self, c):
        """Algorithme"""
        print(c)
        w = [0] * 64
        w[0:16] = struct.unpack('!16L', c)

        for i in range(16, 64):
            s0 = self.rotationRigth(w[i - 15], 7) ^ self.rotationRigth(w[i - 15], 18) ^ (w[i - 15] >> 3)
            s1 = self.rotationRigth(w[i - 2], 17) ^ self.rotationRigth(w[i - 2], 19) ^ (w[i - 2] >> 10)
            w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & 0xFFFFFFFF

        a, b, c, d, e, f, g, h = self.H

        for i in range(64):
            s0 = self.rotationRigth(a, 2) ^ self.rotationRigth(a, 13) ^ self.rotationRigth(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            t2 = s0 + maj
            s1 = self.rotationRigth(e, 6) ^ self.rotationRigth(e, 11) ^ self.rotationRigth(e, 25)
            ch = (e & f) ^ ((~e) & g)
            t1 = h + s1 + ch + self.K[i] + w[i]

            h = g
            g = f
            f = e
            e = (d + t1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (t1 + t2) & 0xFFFFFFFF

        self.H = [(x + y) & 0xFFFFFFFF for x, y in zip(self.H, [a, b, c, d, e, f, g, h])]
        print(self.H)

if __name__ == '__main__':
    s = SHA256("azerty")