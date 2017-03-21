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
    """La chaine de caractère est split est mis dans un tableau"""
    tabChar = []
    for char in string:
        if char != " ":
            tabChar.append(char.upper())
    return tabChar


def charTabtoString(tabChar):
    """On prend un tableau de caractère et on en fait un string"""
    string = ""
    for char in tabChar:
        string += char.upper()
    return string


def chiffrement(message):
    """Chiffre le message"""
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
    """
    Prend une chaine de caractère représentant des chiffres
    Split la chaine et insère cea dans un tableau
    """
    tab2Nb = []
    for i in range(len(string)):
        if i % 2 == 0:
            tab2Nb.append(string[i])
        else:
            tab2Nb[len(tab2Nb) - 1] += string[i]
    return tab2Nb


def dechiffrement(message):
    """Déchiffre le message"""
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
    """Permet à l'utilisateur de créer son propre carré de Polybe"""
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


FREQUENCE_APPARITION_LETTRES_FR = [
    ['E', 0.173], ['A', 0.084], ['S', 0.081], ['I', 0.073], ['N', 0.071], ['T', 0.071],
    ['R', 0.066], ['L', 0.06], ['U', 0.057], ['O', 0.053], ['D', 0.042], ['C', 0.03],
    ['M', 0.03], ['P', 0.03], ['G', 0.013], ['V', 0.013], ['B', 0.011], ['F', 0.011],
    ['Q', 0.01], ['H', 0.009], ['X', 0.004], ['J', 0.003], ['Y', 0.003], ['K', 0.001],
    ['W', 0.001], ['Z', 0.001]
]


def casseCode(message):
    """
    Système permettant de casser le chiffrement
    On compte pour cela la fréquence d'apparition de chaque lettres puis on compare la fréquence avec la fréquence
    d'apparition des lettres de l'alphabet français
    """
    tab_message = stringToTab2Nb(message)
    tab_char = []
    tab_count = []
    for char in tab_message:
        present = False
        for i in range(len(tab_char)):
            if char == tab_char[i]:
                tab_count[i] += 1
                present = True
                break
        if not present:
            tab_char.append(char)
            tab_count.append(1)
    tab_freq = []
    for nb in tab_count:
        tab_freq.append(nb / len(tab_message))
    messageDecoder = ""
    for char in tab_message:
        for i in range(len(tab_char)):
            if char == tab_char[i]:
                if tab_freq[i] >= FREQUENCE_APPARITION_LETTRES_FR[0][1]:
                    messageDecoder += FREQUENCE_APPARITION_LETTRES_FR[0][0]
                elif tab_freq[i] <= FREQUENCE_APPARITION_LETTRES_FR[len(FREQUENCE_APPARITION_LETTRES_FR) - 1][1]:
                    messageDecoder += FREQUENCE_APPARITION_LETTRES_FR[len(FREQUENCE_APPARITION_LETTRES_FR) - 1][0]
                else:
                    for j in range(len(FREQUENCE_APPARITION_LETTRES_FR)):
                        if tab_freq[i] <= FREQUENCE_APPARITION_LETTRES_FR[j][1]:
                            messageDecoder += FREQUENCE_APPARITION_LETTRES_FR[j][0]
    return messageDecoder

if __name__ == '__main__':
    print("phrase de départ : 'Bonjour tout le monde'")
    print("chiffrement :")
    print(chiffrement("Bonjour tout le monde"))
    print("dechiffrement :")
    print(dechiffrement("123534253551434535514532153335341415"))
    print("nouvelle grille :")
    newGrille()
    print("chiffrement et déchiffrement avec la nouvelle grille")
    ch = chiffrement("Bonjour tout le monde")
    print(ch)
    print(dechiffrement(ch))