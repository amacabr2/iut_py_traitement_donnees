from Cryptographie.Le_carre_de_25 import stringToCharTab


def codeCesar(phrase, key):
    """
    Code de césar
    :param phrase:
    :param key:
    :return:
    """
    tab = stringToCharTab(phrase)
    crypted = ""
    for car in tab:
        if car in ALPHABET:
            num = ALPHABET.index(car)
            num += key
            if num >= len(ALPHABET):
                num -= len(ALPHABET)
            crypted += ALPHABET[num]
        else:
            crypted += car
    return crypted


def permutationVoulu():
    """
    Permet de choisirla permutation pour le code de césar
    :return: int
    """
    return int(input("Choisissez la permutation pour le code de césar ouvre tp : ")) % 26


ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(codeCesar("Angeline", permutationVoulu()))