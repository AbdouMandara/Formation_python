# A savoir

**Role des fonctions :** Alléger le code et le segmenter
**Nb :** En python on parlera toujours de fonction car même les procédures retournent quelque chose ; ce quelque chose est l’objet vide (**None**)

## Création de fonction

- ``def`` est le mot clé en python utilisé pour déclarer une fonction
- ``return`` est facultative. Elle ne s'utilise que lorsque la fonction est censée retourner un résultat

## Différence entre objet mutable et immuable

- Un ``objet immuable`` est un objet qui lorsqu’il est créé **ne peut plus être modifié**.
**Ex** : les tuples, les nombres en général (int, float, etc.), les chaines de caractères (str)

- Un ``objet mutable`` est un objet qui lorsqu’il est créé **peut par la suite être modifié**.

**Ex** : les listes, les dictionnaires, les set

## les fonctions Lambda

Les fonctions lambda sont tous simplement des fonctions qu’on déclare sur une seule ligne
**Syntaxe :** nomDeLaFonction = lambda paramètre1, paramètre2, …, paramètreN : resultat

### Utilisation des fonctions lambda avec d'autres fonctions

- map() sert à appliquer une fonction à chaque élément d'un itérable (liste, tuple, set, etc.).
**Syntaxe :** map(fonction_qu_on_va_appliquer, iterable)
**Nb :** Cette fonction map retourne un objet de type **map** qui est un itérateur. On peut donc voir ce que contient cet objet itérateur, soit en le transformant en liste, en tuple ou en set, ou encore en le parcourant par une boucle **for**

______________________________

- filter() permet filtrer les éléments d'un itérable d'un itérable (liste, tuple, set, etc.) en fonction d'un test qu'on a défini comme résultat dans la fonction lambda
**Syntaxe :** filter(fonction_qu_on_va_appliquer, iterable)

**Nb :** Cette fonction filter retourne un objet de type **filter** qui est un itérateur. On peut donc voir ce que contient cet
objet itérateur, soit en le transformant en liste, en tuple ou en set, ou encore en le parcourant par une boucle **for**
