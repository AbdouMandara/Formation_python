# Pour créer ou ouvrir un fichier , on l'ouvre en lecture donc w+ c'est le mode d'ouverture
# open("./4_Manipulation_de_base_sur_les_fichiers/fichier_nouveau.txt", "w+")

# Pour pouvoir écrire du texte dans mon fichier j'allais faire ainsi
"""
file = open("./4_Manipulation_de_base_sur_les_fichiers/fichier_nouveau.txt", "w+")
# Pour écrire dans le fichier
file.write("1 - Abdou \n")
file.write("2 - Mandara \n")
file.write("3 - Lol \n")
# Pour fermer le fichier quand on a finit de travailler
file.close()
"""
"""
students_list = ["Abdou", "Muhammad", "zaza", "Musa", "Pipi"]
# On aurait auussi pu faire
with open("./4_Manipulation_de_base_sur_les_fichiers/fichier_nouveau.txt", "a+") as file :
    for student in students_list :
        file.write(student + "\n")
    file.close()
"""
"""
import os
import random

if os.path.exists("./4_Manipulation_de_base_sur_les_fichiers/repas.txt") :
    with open("./4_Manipulation_de_base_sur_les_fichiers/repas.txt", "r+") as file :
        # print( file.readlines())
        # Pour afficher un repas au hasard doncça prend au hasard un repas dans la liste 
        liste_des_repas = file.readlines()
        choix_repas_au_hasard = random.choice(liste_des_repas)
        print("Je vous propose aujourd'hui", choix_repas_au_hasard)
        file.close
else :
    print("Le chemin passé n'existe pas , sorry ! ")
"""
    
# Pour déplacer des fichiers 
import os
import shutil #ça sert à faire un copier-coller
fichier_a_deplacer = "./4_Manipulation_de_base_sur_les_fichiers/repas.txt"
dossier_visé = "./4_Manipulation_de_base_sur_les_fichiers/Brouillons/repas.txt"

# C'st pour déplacer un fichier dans un autre dossier
shutil.copy(fichier_a_deplacer, dossier_visé)
os.remove(fichier_a_deplacer)
