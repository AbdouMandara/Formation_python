# On utilise Tkinter pour créer les interfaces en Python
# C'est pour tout importer de Tkinter
from tkinter import *
import webbrowser 

def open_video_tkinter_graven():
# C'"est pour ouvrir dans le browser le lien
    webbrowser.open_new("https://www.youtube.com/watch?v=-5zCCcGRrMw&list=PPSV")
# Créer une 1ère fenetre
window = Tk()
# Personnaliser ma fenetre
# a - Le titre de la fenetre
window.title("Mon application ")
# b - La dimension de la fenetre 
window.geometry("720x480") # ça sera une fenetre de dimension fixe donc 480p pour l'horizontal  à 360p pour la verticale
window.minsize(480, 360) # Pour définir une taille minimal
# c - Pour définir une icone à ma fenetre 
window.iconbitmap("./5_Projets_pratiques/icon.ico")
# d - Pour modifier l'apparence de  ma fenetre 
window.config(background='#1EC984')

# Créer ma frame (c'est comme une <div>)
frame = Frame(window,  bg='#1EC984') # Pour dire que la frame se pose sur notre fenetre
# Ajouter un 1er texte sur ma frame
label_title = Label(frame, font=("pacifico", 40),text="Bienvenue sur l'application", fg='white', bg='#1EC984')
label_title.pack() # Pour poser ce composant sur ma fenetre donc on l'empacte

# Ajouter un 2e texte sur ma fenetre
label_subtitle = Label(frame, font=("inter", 20),text="C'est Abdou qui a créé ça :)", fg='white', bg='#1EC984')
label_subtitle.pack() # Pour poser ce composant sur ma frame donc on l'empacte

# Ajouter un bouton
btn = Button(frame, text="Ouvrir Youtube pour voir la vidéo",  font=("Irish Grover", 15), bg='white', fg='#1EC984', command=open_video_tkinter_graven)
btn.pack(pady=25, fill=X)


frame.pack(expand=YES) # Pour empacter ma frame au centre
# Afficher ma fenetre
window.mainloop()
