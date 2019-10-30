import math
import os
import random


def is_casino_number(number, minn=0, maxx=49):
    if is_convertible_to_int(number):
        number = int(number)
        if minn <= number <= maxx:
            return True
    return False


def is_odd(number):
    if number % 2 != 0:
        return True
    return False


def compute_new_balance(oldbalance, profit, bet):
    if profit == 0:
        return (oldbalance - bet)
    return (oldbalance + profit)


def is_convertible_to_int(mystr):
    try:
        mystr = int(mystr)
        return True
    except:
        return False


def main_menu():
    is_correct = False
    choix = 3
    while not is_correct:
        print("\nBienvenue dans zCasiiiiinooooo\n\n")
        print("1- Jouer")
        print("2- Aide")
        print("3- Quitter")
        choix = input("Choississez une option\n_> ")
        if is_casino_number(choix, 1, 3):
            choix = int(choix)
            is_correct = True;
        else:
            print("Faite un choix dans la liste ...")
    return choix


def play_casino(initialbalance, minAmount=1000, maxAmount=2000000, miseMin=50):
    solde_joueur = 0
    can_play = True;

    #  Initialize the Player's Balance
    if initialbalance >= 50:
        solde_joueur = initialbalance
    else:
        print("Pour commencer, vous devez recharger votre compte\n")
        solde_joueur = input("Entrez le montant dont vous disposer : ")
        if is_casino_number(solde_joueur, minAmount, maxAmount):
            solde_joueur = int(solde_joueur)
            solde_joueur += initialbalance
        else:
            can_play = False
            print("Vous devez avoir au moins ", minAmount, " ou au plus ", maxAmount)

    #  Start Playing The Game
    if can_play:
        casino_is_stoped = False
        while not casino_is_stoped:
            mise_joueur = input("Entrez votre mise [ " + str(miseMin) + " , "
                                + str(solde_joueur)+" ] \nOu # pour sortir \n_>  ")
            if mise_joueur == '#':
                casino_is_stoped = True
            elif is_casino_number(mise_joueur, int(miseMin), int(solde_joueur)):
                numero_joueur = input("Choisissez un numero : ")
                if is_casino_number(numero_joueur):
                    mise_joueur = int(mise_joueur)
                    numero_joueur = int(numero_joueur)
                    numero_gagnant = random.randrange(50);
                    if numero_gagnant == numero_joueur:
                        gain = (mise_joueur * 3)
                    elif (is_odd(numero_joueur) and is_odd(numero_gagnant)) or (
                            not is_odd(numero_joueur) and not is_odd(numero_gagnant)):
                        gain = math.ceil(mise_joueur / 2)
                    else:
                        gain = 0
                    if gain > 0:
                        print("\nVous avez gagné!!")
                    else:
                        print("\nVous avez perdu!")
                    print("\n    DETAILS")
                    print("Votre solde initial est : ", solde_joueur)
                    print("Votre avez misé: ", mise_joueur)
                    print("Vous avez choisi le numero : ", numero_joueur)
                    print("Le numero gagnant est : ", numero_gagnant)
                    print("Votre gain est : ", gain)
                    solde_joueur = compute_new_balance(solde_joueur, gain, mise_joueur)
                    print("Votre nouveau solde est : ", solde_joueur, "\n")
                    os.system("pause")
                else:
                    print("Votre le numero doit etre compris entre ~0~ et ~49~")
            else:
                print("Votre mise doit etre dans  ==> [ " + str(miseMin) + " , " + str(solde_joueur) + " ] ")
    return solde_joueur


def help_casino():
    print("\n1 - Le joueur recharge son compte pour commencer.\n")
    print("2 - Le joueur mise sur un numéro compris entre dans un intervalle\n"
          "(Ex: 0,49 soit 50 numéros en tout). En choisissant son numéro, il y\n"
          "dépose la somme qu'il souhaite miser.\n")
    print("3 - La roulette est constituée de 50 cases allant naturellement de\n"
          "0 à 49. Les numéros pairs sont de couleur noire, les numéros impairs\n"
          "sont de couleur rouge. Le croupier lance la roulette, lâche la bille\n"
          "et quand la roulette s'arrête, relève le numéro de la case dans\n"
          "laquelle la bille s'est arrêtée. Dans notre programme, nous ne\n"
          "reprendrons pas tous ces détails « matériels » . Le numéro sur lequel\n"
          "s'est arrêtée la bille est, naturellement, le numéro gagnant.\n");
    print("4 - Si le numéro gagnant est celui sur lequel le joueur a misé\n"
          "(probabilité de 1/50, plutôt faible), le croupier lui remet 3 fois la\n"
          "somme misée.\n")
    print("5 - Sinon, le croupier regarde si le numéro misé par le joueur est\n"
          "de la même couleur que le numéro gagnant (s'ils sont tous les deux\n"
          "pairs ou tous les deux impairs). Si c'est le cas, le croupier lui remet\n"
          "50 % de la somme misée. Si ce n'est pas le cas, le joueur perd sa mise.\n")
    os.system("pause")
