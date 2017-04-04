"""
Auteur: Anthony MACABREY S4A1
"""

from Cryptographie.EnfanceDeLArt.Le_carre_de_25 import stringToCharTab, FREQUENCE_APPARITION_LETTRES_FR


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
    return int(input("Choisissez la permutation pour le code de césar : ")) % 26


def cptOccurence(text):
    """Compte le nombre de fois qu'une lettre soit présente dans le texte"""
    tabCptOccurence = []
    for lettre in ALPHABET:
        count = text.count(lettre)
        if count != 0:
            tabCptOccurence.append([lettre, count])
    return tabCptOccurence


def frequence(text):
    """Va analyser le nombre d'occurence d'une lettre dans le texte et va tenter de casser le code"""
    crackCode = ""
    nbrOccurence = cptOccurence(text)
    tabStat = []
    for occu in nbrOccurence:
        tabStat.append([occu[0], round(occu[1] / len(text), 3)])
    print("Nombre de fois qu'apparaisse les lettres dans le texte : ", nbrOccurence)
    print("Frequence d'apparition des lettres dans le texte : ", tabStat)
    for stat in tabStat:
        for lettre in FREQUENCE_APPARITION_LETTRES_FR:
            if stat[1] == lettre[1]:
                crackCode += lettre[0]
    return crackCode


ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

if __name__ == '__main__':
    text = "Il remarqua que la frequence des lettres d une langue pour un long texte est souvent la meme par " \
           "consequent pour dechiffrer une substitution monoalphabetique AlKindi propose de calculer les frequences " \
           "des lettres du texte chiffre afin de les comparer aux frequences constatees dans la langue qui a servi a " \
           "l ecrire un journaliste americain Michael Drosnin a publie un livre devenu best-seller La Bible " \
           "le code secret Il y affirme l existence d’un code secret dans La Bible annonçant de manière irréfutable " \
           "l assassinat d Anouar El Sadate d Ystak Rabin la Shoah la guerre en Irak et autres evenements de cet " \
           "ordre Brendan Mac Kay, professeur de mathematique à l’Universite Nationale d Australie releva le gant " \
           "En utilisant la même methode il decouvra dans le texte de Melville pas moins de neuf assassinats d un " \
           "premier ministre et meme la mort de Lady Di de son amant et de son chauffeur En prenant au hasard une " \
           "suite infinie de symboles typographiques on y trouvera tous les textes possibles et imaginables Par " \
           "exemple le livre de Drosnin la Bible l intégralité des oeuvres de Sade du Comte de Lautreamont et de " \
           "Rimbaud "
    print("Test choisit : {0}".format(text))
    cesar = codeCesar(text, permutationVoulu())
    print("Code :  {0}".format(cesar))
    print(frequence(cesar))
