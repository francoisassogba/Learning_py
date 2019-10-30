# -*-coding:Latin-1 -*
def tablemultipli(nombre, taille=10):
    """
    Fonction affichant la table de multiplication par 'nombre'
    de 1*nombre à taille*nombre (taille >= 0)
    :param nombre:
    :param taille:
    :return:
    """
    i = 0
    while i <= taille:
        print(str(nombre) + " X " + str(i) + " = " + str(i * nombre))
        i += 1


def isLeap(year = 2000):
    """
    Programme testant si une année, est bissextile ou non
    :param year:
    :return:
    """
    try:
        year = int(year)
        if year < 0 or year > 9999:
            print("The number you've entered must be a valid year.")
        elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print(year, " is leap.")
        else:
            print(year, " is not leap.")
    except:
        print("The number you've entered must be a valid year.")
