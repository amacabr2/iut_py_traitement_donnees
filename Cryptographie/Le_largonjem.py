from Cryptographie.Le_carre_de_25 import stringToCharTab, charTabtoString

CONSONNES = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']


def largonjem(message):
    tab_message = stringToCharTab(message)
    tab_message.reverse()
    consonne = tab_message.pop()
    tab_message.append("L")
    tab_message.reverse()
    tab_message.append(consonne + "EM")
    return charTabtoString(tab_message)