nom = ("elt1") # C'est un <class 'str'> et non tuple
prenom = ("Abdou",) # <class 'tuple'> car j'ai mis , après le 1er élement
print(len(prenom))

# Transformation d'une liste en tuple
liste_de_gens = ["Abdou", "Mama", "Juju"]
tuple_de_gens = (liste_de_gens, ) #<class 'tuple'>car j'ai mis la virgule sinon ça serait une list
print(type(tuple_de_gens), tuple_de_gens)

# Transformation d'un tuple en liste
maListe= list(tuple_de_gens)
print(type(maListe), maListe)