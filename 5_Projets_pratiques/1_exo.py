# exercice 1 : Créer un programme qui lit une moyenne comprise entre 0 et 20, et affiche la mention correspondante

moyenne = float(input("Entres ta moyenne stp :"))
if (moyenne>0 and moyenne <=5) :
    print("Nul")
elif (moyenne >5 and moyenne <10 ) :
    print("Médiocre")
elif (moyenne >= 10 and moyenne <12) :
    print("Passable")
elif (moyenne >= 12 and moyenne <14) :
    print("Assez-bien")
elif (moyenne >= 14 and moyenne <16) :
    print("Bien")
elif (moyenne >= 16 and moyenne <18) :
    print("Très-bien")
elif (moyenne >= 18 and moyenne <20) :
    print("Excellent")