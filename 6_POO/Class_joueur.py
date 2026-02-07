class Joueur:
    
    # Attributs de ma classe
    """
    pseudo = "Abdou"
    health = 20
    point_attaque = 3
    """
    
    # Definition du constructeur
    def __init__(self, pseudo, health, point_attaque) -> None:
       # self sert à dire les attributs de ma classe et affecte à ces attributs ce qui est recuperé à travers les paramètres
        # self est comme le this des autres langages
        self.pseudo = pseudo
        self.health = health
        self.point_attaque = point_attaque
        self.arme = None
        print("Bienvenue au joueur {} / Points de vie : {} / Attaque : {}".format(self.pseudo, self.health, self.point_attaque))

    # Definition des méthodes
    # 1 - Les getters (Accesseurs)
            
    def get_pseudo(self) :
        return self.pseudo
    def get_health(self) :
        return self.health
    def get_attack(self) :
        return self.point_attaque
        
    # 2 - Les setters (Mutateurs)
    def degats(self, degats) :
        self.health -= degats
        print("Aie .. Vous venez de subir {} dégats ! ".format(degats))
        
    def attaque_autre_joueur(self, autreJoueur) :
        autreJoueur.health -= self.point_attaque
        # ou
        # autreJoueur.degats(self.point_attaque)
        print("Point de vie de l'adversaire : {}".format(autreJoueur.health))
        