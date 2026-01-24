"""
listeAuthentification = [("Takam", 2788), ("Admin", 1234), ("Takedoum", 7896), ("Bitacola", 1385)]
Cette liste est constituée de tuples comportant chacun deux éléments. Le premier étant le nom d’utilisateur et le second le mot de 
passe ; des différents employés d’une entreprise. 
Il vous ai demandé de concevoir une interface de connexion au site de l’entreprise, dans laquelle un utilisateur devra rentré son 
nom d’utilisateur et son mot de passe. Cet utilisateur ne peut se connecter au site, uniquement s’il est de l’entreprise ; en d’autres 
termes, son nom d’utilisateur et son mot de passe sont dans la base de données (bref dans notre liste d’en haut là 🙄). 
L’utilisateur peut cependant être un nouvel employé ; et son nom n’est pas encore dans la base de données. Dans ce cas, vous lui 
demanderez d’entrer un code de vérification, qui est celui donné à chaque nouveau employé. Si le code entré est "A052@IME2023", 
alors vous rajouterez cet employé dans la base de données.
Le nouvel utilisateur pourra lui – même définir son nom d’utilisateur pour la connexion, sauf que le mot de passe sera généré 
aléatoirement par vous le programmeur. Ce mot de passe devra contenir 4 chiffres et ne devra correspondre à aucun mot de passe 
déjà assigné à un utilisateur.
"""
import random
code_verification = "A052@IME2023"
listeAuthentification = [("Takam", 2788), ("Admin", 1234), ("Takedoum", 7896), ("Bitacola", 1385)]
print("Bienvenue sur la page de connexion")
choix_user = int(input("1 - Me connecter \n2 - Je suis nouveau\n=> "))
match choix_user :
    case 1 : 
        print("--------- Page de Connexion ---------\nVeuillez remplir les bonnes infomations pour vous connectez")
        nom_connexion_user =input("Nom : ") 
        password_connexion_user = int(input("Mot de passe : ")) 
        for i in listeAuthentification :
            # print(i[1], len(i))
            if nom_connexion_user == i[0] and password_connexion_user == i[1] :
                print(f"Bienvenue {i[0]}")
                break
            
        # print("Vous n'etes pas de l'entreprise")
        
    case 2 :
            print("--------- Page d'inscription ---------\nVeuillez remplir les bonnes infomations pour vous inscrire")
            code_verification_du_user = input("Code de vérification : ")
            if code_verification_du_user == code_verification_du_user :
                nom_inscription_user = input("Nom : ")
                password_inscription_user = random.randint(0, 9999)
                for i in listeAuthentification :
                    if password_inscription_user == i[1] :
                        password_inscription_user= random.randint(0, 9999)
                    else : 
                        password_inscription_user = password_inscription_user
                
                tuple_nouveau_user= (nom_inscription_user, password_inscription_user)
                listeAuthentification = listeAuthentification.append(tuple_nouveau_user)
                print("Inscription réussi ! \n🙈 Votre mot de passe : {}".format(password_inscription_user))
            else :
                print("Code de vérification incorrect")
                
                