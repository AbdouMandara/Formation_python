#print("Bonjour \n Tinitionnf")
"""
Cest un commentaire
"""
#poupou
"""
chaine = 'test'
print(chaine.upper())
"""
#entiers
entier1 = entier2 = entier3  = 565
#Float
Dec1  = 56.5
# Nbre complexes
z1 , z2 = 3+1j, 4-3j
#Listes
liste_pays = ["Cameroun", "Paris", "Inde"]
#chaine
chaine1 = 'Je n\'aime pas ça'
chaine2 = """Patate brule"""
#Tuples
tuple = {"CMR", "CIV"}
#dictionnaires
dictionnaire = {
    "CMR" : 237,
    "CIV" : 227
}
#Set ou ensembles
set = {1, 2, "janvier", 45}
print(type( z1))
print(type( liste_pays))
print(type(chaine1))
print(type(tuple))
print(type(dictionnaire))
#utilisation de fstring pour faire apparaitre les valeurs des variables dans print()
# print(f"___________ \n { dictionnaire, set, entier1, Dec1} \n ____________________\n ")
#Pour afficher les valeurs des variables on peut aussi faire
nom = "Abdou"
# print("Bonjour ", nom)

note1, note2, note3 = 13, 4, 15
moyenne_etudiant = (note1 + note2 + note3)/3
# print(f"Moyenne {int(moyenne_etudiant)}")

#Structure conditionnelle
age_utilisateur = int(input("Entre ton age stp : "))
if age_utilisateur < 18 :
    print("Mineur")
else : 
    print("Majeur")

couleur = input("Choisis ta couleur : ")