######################################
# Projet Pierre Feuille Papier Ciseaux
######################################
import random
#On importe le module "random"
NomJoueur=input("Entrez votre nom :D (Il serra en securité)")
#l'utilisateur choisi son nom
print("Voila ton magnifique nom:",NomJoueur)
#on affiche le nom de l'utilisateur
PlayerVictoires=0
OrdinateurVictoires=0
MatchNuls=0
#on initialise les variables

while True:
    CoupDuJoueur=input("Entrer votre coup: p (Pierre) f (Feuille) c (Ciseaux) q (Quitter)")
#On demande au joueur de selectionner son coup
    if CoupDuJoueur=="q" :
#si le joueur selectionne "q" il quitte la matrice (programme) et affiche le score totale
        print("Vous etes en train de quitter le programme")
        print("Player Victoires",PlayerVictoires)
        print("Ordinateur Victoires",OrdinateurVictoires)
        print("Match Nuls",MatchNuls)
        print("Sortie de la matrice")
        print(3)
        print(2)
        print(1)
        print("Retour a la vie reel")
        break
    if CoupDuJoueur!="p" and CoupDuJoueur!= "f" and CoupDuJoueur!= "c" :
        continue
#Si le joueur selectionne "p" "f" ou "c" il continue/reste dans le programme

    if CoupDuJoueur == "p" :
        print("PIERRE contre ...",end=" ")
    elif CoupDuJoueur =="f" :
        print("FEUILLE contre ...",end=" ")
    else :
        print("CISEAUX contre ...",end=" ")
#Si le joueur selectionne un coup, on affiche le coup
    NombreRandom = random.randint(1,3)
    if NombreRandom == 1 :
        coupPC = "p"
        print("PIERRE")
    elif NombreRandom == 2 :
        coupPC = "f"
        print("FEUILLE")
    else:
        coupPC = "c"
        print("CISEAUX")
#On creer les variables de l'ordinateur, et, on fait en sorte qu'il les affiches de fassons aleatoire
    if CoupDuJoueur == coupPC :
        print ("Match nul !!!")
        MatchNuls = MatchNuls + 1
#Si le coup du joueur est egal au coup de l'ordinateur, alors on affiche, "match nul" et on donne +1 a la variable MatchNuls
    elif CoupDuJoueur == "p" and coupPC=="c" :
        print("Vous avez gagné ! :)")
        PlayerVictoires = PlayerVictoires + 1
    elif CoupDuJoueur == "f" and coupPC=="p" :
        print("Vous avez gagné ! :)")
        PlayerVictoires = PlayerVictoires + 1
    elif CoupDuJoueur == "c" and coupPC=="f" :
        print("Vous avez gagné ! :)")
        PlayerVictoires = PlayerVictoires + 1
#On verifie que le toutes les variables entrées par le joueur, peut gagner contre l'ordinateur, et on ajoute +1 a la variable PlayerVictoires
    elif CoupDuJoueur == "p" and coupPC=="f" :
        print("Vous avez perdu ! :(")
        OrdinateurVictoires = OrdinateurVictoires + 1
    elif CoupDuJoueur == "f" and coupPC=="c" :
        print("Vous avez perdu ! :(")
        OrdinateurVictoires = OrdinateurVictoires + 1
    elif CoupDuJoueur == "c" and coupPC=="p" :
        print("Vous avez perdu ! :(")
        OrdinateurVictoires = OrdinateurVictoires + 1
#On verifie que le toutes les variables entrées par l'ordinateur, peut gagner contre le joueur, et on ajoute +1 a la variable OrdinateurVictoires
    print("Player Victoires",PlayerVictoires)
    print("Ordinateur Victoires",OrdinateurVictoires)
    print("Match Nuls",MatchNuls)
#A chaque fin de tour, on affiche les resultats et on recommence la boucle
