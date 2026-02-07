# A savoir

Pour donner une icone à mon app - interface graphique ça doit etre converti en fichier de type **.ico**

Pour ajouter un texte sur ma fenetre
je vais créer une variable à laquelle j'affecte Label()
**Label()** prend en 1er paramètre **le nom de la fenetre où je vais mettre ce composant**, en 2e paramètre **le texte que ce composant va contenir**. L'ordre peut etre en desordre **Label** prend en paramètre les détails de mon composant
font =() prend en 1er param, la **police**, 2e param **la taille**
fg=' ' c'est pour la couleur du texte
bg=' ' c'est pour le background-color du texte

**pack()** prend des params pour définir la position de l'élement sur la fenetre  :

- **expand=YES** : pour placer l'élement au milieu de la page
- **side=BOTTOM** :  pour placer l'élément en bas
- **side=TOP** : pour placer l'élément en haut

Pour pouvoir voir ma frame je peux lui donner les proprietés suivantes :

- bd = taille_bordure : pour assigner une bordure à ma frame
- relief = ' style_bordure': pour mettre en relief ma frame

Pour le **pack venant de Button()** tu peux assigner comme paramètre **pady** pour définir le **padding sur Y** et **fill** pour dire que ça prenne toute la largeur dispo en X

la proprieté **command** passé à **Button()** c'est pour dire la logique qui se passe quand je clique sur le bouton
