"""
min() : pour trouver le minimum, elle ne fonctionne que si la collection (list ou tuple)
a uniquement des élements de type (int ou float ou str)
"""
liste_nombres = [3, 5, 9,0.0, 22]
print(min(liste_nombres)) #0.0
tuples = ("abdou", "baby", "a", "Popo")
print(min(tuples)) #c'est Popo car il a un "P" majuscule
"""
max() : pour trouver le maximum, elle ne fonctionne que si la collection (list ou tuple)
a uniquement des élements de type (int ou float ou str)
"""

print(max(liste_nombres)) #22
print(max(tuples)) #c'est baby

"""
sum() : pour trouver la somme des élements, elle ne fonctionne que si la collection (list ou tuple)
a uniquement des élements de type (int ou float )
"""
print(sum(liste_nombres)) #39.0
