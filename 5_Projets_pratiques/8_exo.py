"""
À la fin d’un match de basketball, les équipes «Tirex » et «Tetranosaurus», ont respectivement obtenus pour chaque quart 
temps, les scores suivants : (25, 27, 30, 18) et (29, 28, 17, 21). Il vous ai demander de :
▪ Stocker ces résultats dans un dictionnaire dont les clés correspondront aux noms de chaque équipe et les valeurs, les 
tuples contenant leurs scores pour chaque quart temps. 
▪ Afficher les résultats de chaque équipe pour chaque quart temps
▪ Calculer les scores finaux de chaque équipe à la fin du quatrième quart temps et donner le nom de l’équipe gagnante 
"""

Tirex = (25, 27, 30, 18)
Tetranosaurus = (29, 28, 17, 21)

resultats = {}
resultats["Tirex"] = (25, 27, 30, 18)
resultats["Tetranosaurus"] = (29, 28, 17, 21)
if sum(resultats["Tirex"]) > sum(resultats["Tetranosaurus"]) :
    print("Tirex a gagné 🦃")
else : 
    print("Tetranosaurus a gagné 😒")
    