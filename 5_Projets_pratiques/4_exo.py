import random
print("Choissis un niveau : \n1 - Facile (entre 0 et 10) : 5 tentatives\n2 - Moyen (entre 0 et 100): 10 tentatives\n3 - Difficile (entre 0 et 1000): 20 tentatives\n4- Super Star Wesh (entre 0 et 10000): 25")
choix_user = int(input("Je choisis : "))
match choix_user :
    # Niveau Facile
    case 1 :
        print("Niveau - Facile : 5 tentatives")
        nbre_random = random.randint(0, 10)
        nbre_tentatives = 5
        veux_tu_jouer = "O"
        while veux_tu_jouer =="O":
            
            for i in range(nbre_tentatives) :
             print(nbre_random)
             print("Tentatives restantes : {}".format(nbre_tentatives-i))
             nbre_user = int(input("Je dis que c'est : "))
             if(nbre_user == nbre_random) :
                print("Bravo !")
                veux_tu_jouer = input("Veux-tu encore jouer ? O(oui)/ N(non) : ").upper()
                nbre_random = random.randint(0, 10)
                break
             elif(i+1==nbre_tentatives):
                veux_tu_jouer = input("Veux-tu encore jouer ? O(oui)/ N(non) : ").upper()
                print("Perdu")
             elif (nbre_user>nbre_random) :
                print("Trop grand")
                continue
             elif (nbre_user<nbre_random) :
                print("Trop petit")
                continue
            
        # Niveau Moyen
    case 2:
        print("Niveau - Moyen : 10 tentatives")
        nbre_random = random.randint(0, 100)
        nbre_tentatives = 10
        veux_tu_jouer = "O"
        
        while veux_tu_jouer =="O":
            
            for i in range(nbre_tentatives) :
             print(nbre_random)
             print("Tentatives restantes : {}".format(nbre_tentatives-i))
             nbre_user = int(input("Je dis que c'est : "))
             if(nbre_user == nbre_random) :
                print("Bravo !")
                veux_tu_jouer = input("Veux-tu encore jouer ? O(oui)/ N(non) : ").upper()
                nbre_random = random.randint(0, 100)
                break
             elif(i+1==nbre_tentatives):
                veux_tu_jouer = input("Veux-tu encore jouer ? O(oui)/ N(non) : ").upper()
                print("Perdu")
             elif (nbre_user>nbre_random) :
                print("Trop grand")
                continue
             elif (nbre_user<nbre_random) :
                print("Trop petit")
                continue
        # Niveau Difficile
    case 3:
        print("Niveau - Difficile : 20 tentatives")
        nbre_random = random.randint(0, 1000)
        nbre_tentatives = 20
        veux_tu_jouer = "O"
        
        while veux_tu_jouer =="O":
            
            for i in range(nbre_tentatives) :
             print(nbre_random)
             print("Tentatives restantes : {}".format(nbre_tentatives-i))
             nbre_user = int(input("Je dis que c'est : "))
             if(nbre_user == nbre_random) :
                print("Bravo !")
                veux_tu_jouer = input("Veux-tu encore jouer ? O(oui)/ N(non) : ").upper()
                nbre_random = random.randint(0, 1000)
                break
             elif(i+1==nbre_tentatives):
                veux_tu_jouer = input("Veux-tu encore jouer ? O(oui)/ N(non) : ").upper()
                print("Perdu")
             elif (nbre_user>nbre_random) :
                print("Trop grand")
                continue
             elif (nbre_user<nbre_random) :
                print("Trop petit")
                continue
        # Niveau  Super Star Wesh
    case 4:
        print("Niveau - Super Star Wesh : 25 tentatives")
        nbre_random = random.randint(0, 10000)
        nbre_tentatives = 25
        veux_tu_jouer = "O"
        
        while veux_tu_jouer =="O":
            
            for i in range(nbre_tentatives) :
             print(nbre_random)
             print("Tentatives restantes : {}".format(nbre_tentatives-i))
             nbre_user = int(input("Je dis que c'est : "))
             if(nbre_user == nbre_random) :
                print("Bravo !")
                veux_tu_jouer = input("Veux-tu encore jouer ? O(oui)/ N(non) : ").upper()
                nbre_random = random.randint(0, 10000)
                break
             elif(i+1==nbre_tentatives):
                veux_tu_jouer = input("Veux-tu encore jouer ? O(oui)/ N(non) : ").upper()
                print("Perdu")
             elif (nbre_user>nbre_random) :
                print("Trop grand")
                continue
             elif (nbre_user<nbre_random) :
                print("Trop petit")
                continue
            