"""
Exercice 3 : Créer un programme python qui choisit aléatoirement un nombre secret compris entre 1 et 10 puis 
demande à l’utilisateur de le prédire, et donne l’un des verdicts suivants :
▪ «Bravo» (si le nombre a été bien prédit)
▪ «Pas correcte» : Si le nombre entré par l’utilisateur est très loin du nombre à deviner
▪ Donnez une seconde et dernière chance à l’utilisateur, si le nombre qu’il a prédit est juste en dessous 
ou au dessus du nombre à deviner et de là, afficher :
• «Bon travail» si l’utilisateur le devine cette fois-ci
• «Massah même avec une seconde chance» (si l’utilisateur ne le trouve pas)
"""
import random, time
nombre_random = random.randint(1, 10)

print("Bienvenue sur le Jeu - Devine le Nombre - ")
print("_________________________________________________")
nbre_user = int(input("Entres ton nombre : "))
if(nbre_user == nombre_random) :
    print("Bravo")
elif (nbre_user> nombre_random or nbre_user<nombre_random) :
    print("Pas correcte")
    time.sleep(1)
    nbre_user = input("Re-entres ton nombre : ")
    if(nbre_user == nombre_random) :
        print("Bon travail")
    else :
        print("Massah même avec une seconde chance")
    
    