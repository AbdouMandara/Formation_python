chaine = "Ma liste de fruits"

 # Pour accéder à "a" dans la variable "chaine", je fais :
print(chaine[1])

# Opérations de slicing pour extraire une partie d'une séquence
print(chaine[0:7:2])

# Inversons une séquence
print(chaine[::-1])

# Extraction d'une partie d'une séquence en fonction de l'indice
print(chaine[3:9])

# Test d'appartenance
etudiants = "Abdou, Kegne, Dina, Ahmadou, Maurice, Mummy, Tenou"

print("Etudiant présent") if("Tenou" in etudiants) else print("Eleve non présent")