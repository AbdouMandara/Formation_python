"""
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 
'Décembre']
Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir des tuples contenant un élément de t2 et 
un élément de t1 de même indice ; de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant :
[('Janvier',31), ('Février',28), ('Mars',31), etc...].
"""
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = []
j = 0
for i in t2 :
    tuples = (i, t1[j])
    t3.append(tuples)
    j+=1
print(t3)