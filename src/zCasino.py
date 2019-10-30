from package.zcasifuncs import *

casino_end = False
balance = 0

while not casino_end:
    choix = main_menu()
    if choix == 1:
        print("Solde Initial : ", balance)
        balance = play_casino(balance)
    elif choix == 2:
        help_casino()
    elif choix == 3:
        casino_end = True
os.system("pause")
os.system("exit")
