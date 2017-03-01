def pgcd(a, b):
    if a % b == 0:
        return b
    else:
        return pgcd(b, a % b)


if __name__ == '__main__':
    a = int(input("Donner une valeur a : "))
    b = int(input("Donner une valeur b : "))
    print("Le pgcd de {0} et {1} est : {2}".format(a, b, pgcd(a, b)))