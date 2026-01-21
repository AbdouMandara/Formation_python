"""
# 1 - Input
# a - Utilisation de input() 
name = input("Entres ton nom : ")

# b - Conversion de l'entrée du user en autres types
age = int(input("Entres ton age, stp : "))

# c - Affichage du type des données entrées par le user  
print(type(name))
print(type(age))

#___________________________________________
# 2 - output
# a - Utilisation de print(): syntaxe 1 
print("Tu es ", name, " tu as ", age, " ans ")

# b - Utilisation de print(): syntaxe 2 
print(f"Tu es {name}  tu as {age} ans ")

# c - Utilisation de print(): syntaxe 3 
print("Tu es {}  tu as {} ans ".format(name, age))
"""
# 3 - Petits exercices : Afficher la somme de 2 nombres entrés par le user
nombre1= int(input("Entrez le 1er nombre : "))
nombre2= int(input("Entrez le 2ème nombre : "))
somme = nombre1 + nombre2

print("La somme est : {} car {} + {} donne {}".format(somme, nombre1, nombre2, somme))
