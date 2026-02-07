# def afficher():
#     userMessage = input("Ton message : ")
#     print("Ton message est "+ userMessage)

# afficher()

def somme(a,b) :
    return a+b
print("La somme est : {}".format(somme(4,5)))
print(somme('bon', 'jour'))
print(somme([1, 3, 'azerty'], [2]))

def estPair(a) :
    if a%2 ==0 :
        return True
    else :
        return False

if(estPair(1)) :
        print("Nombre pair")
else : 
        print("Nombre impair")


print("-----IMC-----")
def IMC(nom, masse, taille):
  imc = masse/taille**2
  if 0 < imc <= 18.5:
    print(f"{nom}, vous etes en situtation de maigreur")
  elif 18.5 < imc <= 25:
    print(f"{nom}, vous avez une masse normale")
  elif 25 < imc <= 30:
    print(f"{nom}, desole vous etes en surpoids")
  elif 30 < imc <= 40:
    print(f"{nom}, vous etes en situtation d'obesite modere")
    print(f"Faites du sport, et mettez vous au regime")
  elif imc > 40:
    print(f"{nom}, vous etes en situtation d'obesite severe")
    print(f"Faites beaucoup de sport, et mettez vous au regime")
    
nomUtilisateur = input("Quel est votre nom SVP ? ")
masseUtilisateur = float(input("Combien de Kg faites-vous ? "))
tailleUtilisateur = float(input("Quelles est votre taille en m ? "))
IMC(nomUtilisateur, masseUtilisateur, tailleUtilisateur)


mon_nombre = 9
def plus_2 (nombre) :
    nombre = nombre +2 # En dehors du programme la valeur de ma variable n'a pas changé car les int sont des objets immuables
    return nombre
print(plus_2(mon_nombre))

def addIfIsNotInList(liste, objet):
    if objet not in liste:
        liste.append(objet)
        
maListe = [1, 2, 3, 4]
addIfIsNotInList(maListe, 3) 
addIfIsNotInList(maListe, 5)  
print("Voyons si elle a ete modifiee")
print(maListe) #On se rend bien compte ici que la fonction a bel et bien modifiée notre liste de départ car les listes sont des objets mutables

# Fonction somme sous forme de fonction lambda
somme = lambda a,b : a+b
som = somme(8,0)
print(som)
# uTILIsation de la fonction map
carré_des_nombres = map(lambda x: x**2, range(5)) # type <class 'map'>
tuple_carré = tuple(carré_des_nombres)
print(tuple_carré)

# Utilisation de la fonction filter
liste = [22, 4, 5, 9, 10, 0]
nbres_pairs = filter(lambda x: x%2==0,liste)
liste_nbres_pairs = list(nbres_pairs)
print(liste_nbres_pairs)