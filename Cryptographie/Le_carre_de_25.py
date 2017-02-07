import re


def initCarrePolybe():
    return [
        ['A', 'B', 'C', 'D', 'E'],
        ['F', 'G', 'H', 'I', 'J'],
        ['K', 'L', 'M', 'N', 'O'],
        ['P', 'Q', 'R', 'S', 'T'],
        ['U', 'V', 'X', 'Y', 'Z']
    ]


CARRE_POLYBE = initCarrePolybe()


def stringToCharTab(string):
    tabChar = []
    for char in string:
        if char != " ":
            tabChar.append(char.upper())
    return tabChar


def charTabtoString(tabChar):
    string = ""
    for char in tabChar:
        string += char
    return string


def chiffrement(message):
    tab_message = stringToCharTab(message)
    for k in range(len(tab_message)):
        if tab_message[k] == 'W':
            tab_message[k] = 'V'
            tab_message.insert(k + 1, 'V')

        for i in range(len(CARRE_POLYBE)):
            for j in range(len(CARRE_POLYBE)):
                if CARRE_POLYBE[i][j] == tab_message[k]:
                    tab_message[k] = str(i + 1) + str(j + 1)
    return charTabtoString(tab_message)


def stringToTab2Nb(string):
    tab2Nb = []
    for i in range(len(string)):
        if i % 2 == 0:
            tab2Nb.append(string[i])
        else:
            tab2Nb[len(tab2Nb) - 1] += string[i]
    return tab2Nb


def dechiffrement(message):
    tab_message = stringToTab2Nb(message)
    for k in range(len(tab_message)):
        for i in range(len(CARRE_POLYBE)):
            for j in range(len(CARRE_POLYBE)):
                if tab_message[k] == str(i + 1) + str(j + 1):
                    tab_message[k] = CARRE_POLYBE[i][j]

    for k in range(len(tab_message) - 1):
        if tab_message[k] == 'V' and tab_message[k + 1] == 'V':
            tab_message[k] = 'W'
            del tab_message[k + 1]

    return charTabtoString(tab_message)


def newGrille():
    print("Création de votre grille de chiffrement (grille de 5 x 5 sans W — W = VV).")
    alphabet = []
    for i in range(len(CARRE_POLYBE)):
        for j in range(len(CARRE_POLYBE[i])):
            while True:
                char = input("Ligne " + str(i) + ", colonne " + str(j) + " : ").upper()
                if len(char) != 1:
                    print("Veuillez entrer un unique caractère !")
                elif not char.isalpha():
                    print("Le caractère doit être une lettre !")
                elif char == 'W':
                    print("Le caractère ne doit pas être un « W » !")
                elif char in alphabet:
                    print("Le caractère " + str(char) + " est déjà présent dans la grille !")
                elif not re.match('[A-Z]', char):
                    print("Le caractère ne doit posséder de diactrique.")
                else:
                    CARRE_POLYBE[i][j] = char
                    alphabet.append(char)
                    break


newGrille()
print(dechiffrement(chiffrement('Anthony')))