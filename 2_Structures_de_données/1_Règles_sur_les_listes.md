# Savoir sur les listes

**la liste** est un objet **mutable** donc on peut la modifier, ajouter, supprimer des élements

## Méthodes d'ajout d'élements dans une liste

- append() : modifie réellement la liste , elle ne travaille pas sur une copie
- insert() : modifie réellement la liste , elle ne travaille pas sur une copie
**Nb :**  la méthode insert ne va pas remplacer l’élément qui se trouvait précédemment à l’indice pos, mais plutôt le décaler vers la
droite ; lui et tous les éléments qui le suivaient. Leur indice seront donc tous augmenté de 1
- extend() : modifie réellement la liste , elle ne travaille pas sur une copie

## Méthodes de suppression d'élements dans une liste

- clear () : supprime définitivement tout le contenu d'une liste sans demander la permission

## Méthodes pour trier les élements d'une liste

- sort() : trie la liste dans l’ordre et la modifie directement.
**NB :** Avec ````sort()``` les élements doivent etre de meme nature ou ~type~

## Créer une liste contenant une suite d’entier

on utilise list() pour créer un élement de type <"list">
range(x, y, z ) : pour créer un objet itérateur donc un objet constitué d' **entier**
````Détails sur les paramètres de range : ``` x -> nbre de début de cette liste
y -> nbre final de cette liste
z -> le pas de comptage donc l'écart entre les entiers de cet objet
**Exemple :** list(range(X, Y, pas))
