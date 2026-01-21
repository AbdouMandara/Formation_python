# a -  Déclaration des variables
nom = "Abdou"
age=18
moyenne = 15.75
es_tu_vivant = True
vide = None

# b - Type de données des variables à travers type()
print(type(nom)) #str
print(type(age)) #int
print(type(moyenne)) #float
print(type(es_tu_vivant)) #bool
print(type(vide)) #NoneType

# c - Changement du type d'une variable grace au Garbage Collector
x = 10 
x = "Papapiya"
print(type(x))