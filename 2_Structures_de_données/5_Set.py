# Déclaration de set 

## Methode de déclaration 1
# ensemble = set()

## Methode de déclaration 2
# ensemble = set("elt1", "elt2")

## Methode de déclaration 3
# ensemble = set(["elt1", "elt2"])

## Methode de déclaration 4
# ensemble = set(("elt1", "elt2"))

## Methode de déclaration 5
ensemble_elt = {"elt1", "elt2"}

# Méthodes sur set

## Connaître le nombre d’éléments dans un ensemble
# print(len(ensemble_elt))
## Ajouter une clé à un ensemble
ensemble_elt.add("elt4") # ça donne {'elt4', 'elt2', 'elt1'}

## Ajouter plusieurs clés à un ensemble je passe ces élements sous forme de liste ou tuple
ensemble_elt.update(("elt4", "elt6", "hu")) # ça donne{'elt1', 'hu', 'elt4', 'elt6', 'elt2'} car les clés doivent etre uniques

## Supprimer une clé 
#ensemble_elt.remove("e")  ça renvoie KeyError: 'e' car j'ai utilisé remove et cette clé n'est pas dans mon set
ensemble_elt.discard("hu")
# print(ensemble_elt)

# Les opérations (de proba) propres aux ensembles en python
## Union
A = {1, 2, 3, 4, 5, 7, 'Talla'}
B = {5, 7, 8, 13, 22, 'MAPOU'}
union = A | B 
print(union) # ça retourne {1, 2, 3, 4, 5, 'Talla', 7, 8, 'MAPOU', 13, 22}
intersection = A & B
print(intersection) # ça retourne {5, 7}
difference = A - B
print(difference) # {1, 2, 3, 4, 'Talla'}