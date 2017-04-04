"""
Auteur: Anthony MACABREY S4A1
"""

class SHA1:

    def __init__(self):
        """Initialise H"""
        self.H = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0
        ]

    def padding(self, content):
        """
        Prépare le message
        Il faut ajouter des 0 tant que le content n'a pas la bonne taille
        """
        l = len(content)  # Bytes
        hl = [int((hex(l * 8)[2:]).rjust(16, '0')[i:i + 2], 16)
              for i in range(0, 16, 2)]

        l0 = (56 - l) % 64
        if not l0:
            l0 = 64

        if isinstance(content, str):
            content += chr(0b10000000)
            content += chr(0) * (l0 - 1)
            for a in hl:
                content += chr(a)
        elif isinstance(content, bytes):
            content += bytes([0b10000000])
            content += bytes(l0 - 1)
            content += bytes(hl)

        return content

    def rotationLeft(self, n, x, w=32):
        """Rotation binaire par la gauche"""
        return (x << n) | (x >> w - n)

    def gereM(self, content):
        """Création du tableau M"""
        M = []
        content = bytearray(content)

        # Il faut 64 bits par blocks
        for i in range(len(content) // 64):
            m = []
            # 16 mots par blocks
            for j in range(16):
                n = 0
                for k in range(4):
                    n <<= 8
                    n += content[i * 64 + j * 4 + k]
                m.append(n)
            M.append(m[:])

        return M

    def hachageInter(self, a, b, c, d, e, mask):
        """Calcul de hachage intermédiaire"""
        self.H[0] = (a + self.H[0]) & mask
        self.H[1] = (b + self.H[1]) & mask
        self.H[2] = (c + self.H[2]) & mask
        self.H[3] = (d + self.H[3]) & mask
        self.H[4] = (e + self.H[4]) & mask

    def traiteBlock(self, block):
        """Gère les blocks"""
        mask = pow(2, 32) - 1

        # On remplit le tableau W
        W = block[:]
        # D'après wikipedia on remplit ainsi le tableau ainsi pour 16 <= t <= 79
        for t in range(16, 80):
            W.append(self.rotationLeft(1, (W[t - 3] ^ W[t - 8] ^ W[t - 14] ^ W[t - 16]))
                     & mask)

        # a,b,c,d,e prennent les valeurs de H1, H2, H3, H4, H5
        a, b, c, d, e = self.H[:]

        for t in range(80):
            if t <= 19:
                K = 0x5a827999
                f = (b & c) ^ (~b & d)
            elif t <= 39:
                K = 0x6ed9eba1
                f = b ^ c ^ d
            elif t <= 59:
                K = 0x8f1bbcdc
                f = (b & c) ^ (b & d) ^ (c & d)
            else:
                K = 0xca62c1d6
                f = b ^ c ^ d

            T = ((self.rotationLeft(5, a) + f + e + K + W[t]) & mask)
            e = d
            d = c
            c = self.rotationLeft(30, b) & mask
            b = a
            a = T

            self.hachageInter(a, b, c, d, e, mask)

    def update(self, content):
        """Fonction intermédiaire"""
        content = self.padding(content)
        print(content)
        content = self.gereM(content)

        for block in content:
            self.traiteBlock(block)

    def hexdigest(self):
        """Ajoute des 0 tant qu'il le faut"""
        s = ''
        for h in self.H:
            s += (hex(h)[2:]).rjust(8, '0')
        return s

    def sha1(self, content):
        """Fonction pricipale"""
        content = self.padding(content.encode())
        content = self.gereM(content)

        for block in content:
            self.traiteBlock(block)

        h = self.hexdigest()
        return h

import hashlib

if __name__ == '__main__':
    content = "Wikipédia, l'encyclopédie libre et gratuite"
    print("La phrase qui va être hach : " + content)
    print("Avec la méthode de python : " + str(hashlib.sha1(content.encode()).hexdigest()))
    s = SHA1()
    print("Avec ma méthode : " + str(s.sha1(content)))