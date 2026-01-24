"""
crivez un programme qui analyse un par un tous les éléments d’une liste de nombres (par exemple la liste t1 de l’exercice 
précédent) pour générer deux nouvelles listes. L’une contiendra seulement les nombres pairs de la liste initiale, et l’autre les 
nombres impairs (sans répétition). Par exemple, pour la liste t1, le programme devra construire une liste pairs qui 
contiendra [28, 30], et une liste impairs qui contiendra [31]. 
"""
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
liste_nbre_pairs=[]
liste_nbre_impairs=[]
for i in t1 :
    if i%2 == 0 :
        liste_nbre_pairs.append(i)
    else :
        liste_nbre_impairs.append(i)
        
print(f"Liste des nombres impairs : {liste_nbre_impairs}")
print(f"Liste des nombres pairs : {liste_nbre_pairs}")