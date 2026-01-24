""""
Vous venez d'être nommé(e) responsable de la gestion des contacts pour l'organisation d'un festival de musique. 
Votre mission est de créer une application de gestion de contacts pour gérer les artistes, les organisateurs et les 
sponsors du festival.
Pour chaque contact, vous devez stocker les informations suivantes : nom, prénom, numéro de téléphone, 
adresse e-mail.
Vous devez utiliser des variables pour stocker les informations de chaque contact, des listes pour stocker 
l'ensemble des contacts, et des dictionnaires pour stocker les informations spécifiques à chaque contact.
"""
infos_contact = {}
contact = []
liste_contact = []

infos_contact["nom"] = "Abdou"
infos_contact["prenom"] = "Mandara"
infos_contact["mail"] = "a_manda@gmail.com"

contact.append(infos_contact)
liste_contact.append(contact)

print(liste_contact)

nom = input("Le nom : ")
prenom = input("Le prenom : ")
email = input("L' adresse e-mail : ")

infos_contact["nom"] = nom
infos_contact["prenom"] =prenom
infos_contact["mail"] =email

contact.append(infos_contact)
liste_contact.append(contact)
print(liste_contact)