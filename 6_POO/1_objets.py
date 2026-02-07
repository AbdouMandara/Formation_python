# J'impôrte de mon fichier du nom "Class_joueur" ma classe joueur qu'on appelle module dans Python
from Class_joueur import Joueur
from Class_arme import Arme
# Instance de mes classes
Joueur1 = Joueur("Mama", 50, 2)
Joueur2 = Joueur("Abdou", 25, 9)
couteau = Arme("Couteau", 5)
# Joueur2.degats(8)
# print("Vous avez désormais: {}".format(Joueur2.get_health()))
Joueur2.attaque_autre_joueur(Joueur1)