# Déclaration des listes
liste = [2, 3, "Papa"]
pièces_de_la_maison = ["Cuisine", "Salon","Douche", "Jardin"]

# Accéder à un élement d'une liste à travers son indice
# print("{} est mon père ".format(liste[2])) # papa

# Modification d'un élement d'une liste à travers son indice
liste[2] = "Mandara"
# print("{} est mon père ".format(liste[2])) # papa

# Modification des  élements d'une liste en utilisant le slicing donc à travers l'indice de départ où on va commencer la modif jusqu'à l'indice de fin
pièces_de_la_maison[0:2] = ["Salle de bain", "Chambre"] #['Salle de bain', 'Douche', 'Jardin']

# Ajouter des élements dans une liste
# 1- Append() : pour ajouter un élement à la fin d'une liste
pièces_de_la_maison.append("mama")

# 2 - insert() : pour ajouter un élement à une position(indice) dans une liste
pièces_de_la_maison.insert(2, "Véranda")
print(pièces_de_la_maison)

# 3 - extend (): pour ajouter le contenu d'une liste à une autre donc concatener
pièces_de_la_maison.extend(liste)

# Suppression des élements  d'une liste
# 1 - remove() : pour supprimer un élement dans une liste elle supprime la première occurence de cet élement
p = pièces_de_la_maison.remove(3)

#print(p) # J'ai None car j'ai utilisé remove()

#2- pop() : supprime un élement en fonction de son indice et le retourne ce qui nous donne la possibilité de pouvoir le stocker
p = pièces_de_la_maison.pop(6)
#print(p) # J'ai 2 , l'élement que je voulais supprimer car j'ai utilisé pop()
print(pièces_de_la_maison)

# 3 - clear() : pour supprimer tous les élements d'une liste
liste.clear()

# Connaitre la taille (nbre d'élements d'une liste)
print(len(pièces_de_la_maison))

# Connaitre le nombre d'occurence d'un élement dans une liste
print(pièces_de_la_maison.count("mama"))

# Connaitre l'indice ou position d'un élement dans une liste
print(pièces_de_la_maison.index("mama"))

# Tri des élements dans une liste
# 1 - sort() : trier dans l'ordre en modifiant la liste
# 1 - sort() : trier dans l'ordre en modifiant la liste
nombres = [11, 2, 90, 00, 5, ]
# print(nombres.sort()) #J'ai None car elle ne retourne rien mais la liste a été classé
nombres.sort(reverse=True) # ça va classer dans l'ordre décroissant
print(nombres)

# 2 - sorted() : trier dans l'ordre en travaillant sur une copie de la liste et retourne un nouvel objet
nombres_classés = sorted(nombres)
nombre_en_désordre= sorted(nombres, reverse=True) #trier dans l'ordre décroissant
print(nombres_classés, nombre_en_désordre)

# reverse() : pour inverser l'ordre des élements d'une liste en travaillant sur cete liste, elle ne retourne aucun résultat
liste_personne = ["manège", "papa", "abdou"]
liste_personne.reverse()
print(liste_personne) #['abdou', 'papa', 'manège']

# Transformer une liste en chaine de caractère lorsque les élements de cette liste sont de type <str>
chaine_personne = "-".join(liste_personne)
print(chaine_personne) #abdou-papa-manège

# Créer une liste à partir d’une chaîne de caractères 
liste_personne = chaine_personne.split("-")
print(liste_personne) #['abdou', 'papa', 'manège']

# Créer une liste contenant une suite d'entier
chiffres = list(range(0, 20, 2))
print(chiffres)