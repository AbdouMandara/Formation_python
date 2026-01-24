# Exercice 2 : Créer un programme qui permette de calculer l’indice de masse corporelle d’un individu, et affiche son état.
poids = int(input("Entrez votre poids en KG : "))
taille =  float(input("Entrez votre taille en M : "))

IMC = poids / taille**2
if(IMC>0 and IMC < 18.5) :
    print("Maigre")
elif (IMC >= 18.5 and IMC <21) :
    print("Normal")
elif (IMC >= 21 and IMC <30) :
    print("Surpoids")
else :
    print("Obèse")

print("Ton IMC : {IMC}")
