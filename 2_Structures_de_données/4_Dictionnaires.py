# Déclaration d'un dictionnaire
fruits = {} #ou new_dictionnaire=dict()
fruits= {'pomme' : 300, 'raisin' : 100} 

# Accéder aux élements d'un dictionnaire
print(fruits['pomme']) # 300 qui est sa valeur
print(fruits.get('papaye', 400)) # 400 car la clé 'papaye' n'existe pas dans fruit mais grace à .get() j'ai la valeur de la clé inconnue recherché

# Modifier un élement dans le dictionnaire
fruits['pomme'] = 100

#Ajouter un élement
fruits['orange'] = 400 #ça va ajouter car la clé 'orange' n'était pas présente

# Supprimer un élement dans le dictionnaire
del fruits['raisin'] # ou fruits.pop('raisin') mais ça retourne la valeur

# 1 - Accéder aux différents élements d'un dictionnaire
# a - pour avoir les clés du dictionnaire
print(fruits.keys())
# b - pour avoir les valeurs des clés du dictionnaire
print(fruits.values())
# b - pour avoir les valeurs et les clés donc le couple du dictionnaire
print(fruits.items())

# 2 - Parcourir les élements d'un dictionnaire

for k in fruits.keys() : # ou for k in fruits
    print(k) #la variable k, va également parcourir toutes les clés du dictionnaire
for v in fruits.values() :
    print(v)     #La variable v va parcourir toutes les valeurs du dictionnaire
for it in fruits.items() :
    print(it)     #La variable v va parcourir tous les tuples (cle, valeur) du dictionnaire