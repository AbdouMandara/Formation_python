class Arme :
    def __init__(self, nom, degats) :
        self.nom = nom
        self.degats = degats
        
    def get_nom_arme(self):
        return self.nom
    def get_degats_arme(self):
        return self.degats