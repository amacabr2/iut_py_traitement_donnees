from Cryptographie.Le_carre_de_25 import stringToCharTab


def codeCesar(phrase):
    tab = stringToCharTab(phrase)
    crypted = ""
    key = 3
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


ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(codeCesar("Anthony"))