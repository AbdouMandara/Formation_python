from tkinter import *
import string
from random import randint, choice


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    
    password = "".join( choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
# Créons la fenetre
window = Tk()
window.title("Génerateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("./5_Projets_pratiques/icon.ico")
window.minsize(480, 360)
window.config(background="#4065A4")
# Créer la frame principale
frame = Frame(window, bg='#4065A4')
# Création d'image
# width = 300
# height = 300
# image = PhotoImage(file="./5_Projets_pratiques/Abdou_Arc1.png").zoom(25).subsample(32)
# canvas = Canvas(frame, width=width, height=height, bg='#4065A4',bd=0, highlightthickness=0)
# canvas.create_image(width/2, height/2, image=image)
# canvas.grid(row=0, column=0, sticky=W)

# Créer une sous-boite
right_frame = Frame(frame, bg='#4065A4')
# On place la sous-boite (frame) à la droite de notre frame principale
right_frame.grid(row=0, column=1, sticky=W)


# Créer un titre 
label_title = Label(right_frame, text="Génerateur de mot de passe 🤫", font=("inter", 30), bg='#4065A4', fg='white' )
label_title.pack(pady=35)

# Créer un input/champ/entry
password_entry = Entry(right_frame, font=("poppins", 20), bg='#4065A4', fg='white' )
password_entry.pack(fill=X)

# Créer un bouton pour génerer le password
btn_generation = Button(right_frame, text="Génerer", font=("inter", 16), bg='white', fg='#4065A4', command=window.bell and generate_password )
btn_generation.pack(fill=X, pady=20)

frame.pack(expand=YES)

# Création d'une barre de menu
menu_bar = Menu(window)
# Créer un premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command= window.quit)
menu_bar.add_cascade(label="Options", menu=file_menu)
window.config(menu=menu_bar)

# Affichage de la fenetre
window.mainloop()