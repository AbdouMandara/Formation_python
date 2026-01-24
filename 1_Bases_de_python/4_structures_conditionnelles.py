"""

age_user = int(input("Entres ton age, stp : "))
if(age_user<= 0 or age_user >= 200) : 
    print("Erreur sur ton age")

elif (age_user>21 ):
    print(f"t'es majeur petit, car t'as {age_user}")
else : 
    print(f"t'es mineur petit, car t'as {age_user}")
    
couleur_pref = input("Devines ma couleur pref : ")
couleur_pref = couleur_pref.lower()

if couleur_pref != 'bleu' : 
    print("Tu ne connais pas ma bonne couleur \n t'es nul ")
else : 
    print("Tu connais ma bonne couleur")
"""

# Utilisation de "Match...case"
"""
print("Quel est ton langage de Programmation préferé ?")
print("__________________________________")
print("1 - JavaScript (le roi du Web) \n2 - Python (le roi de l'IA) \n3 - Rust (Le roi du Desktop) \n4 - C (le père des nouvelles technos)")
choix_user = int(input("Tu choisis quoi : "))
print("__________________________________")

match choix_user :
    case 1 :
        print("T'es un JavaScriptien oko , le gars de TypeScript")
    case 2 :
        print("Donc t'as pas peur du serpent hein ? En tout cas c'est quoi un LLM ???")
    case 3 : 
        print("Donc t'as pas peur du crabe hein ? Tu veux la perf !?")
    case 4 :
        print("Okoh ! T'es un papi :) Tu veux créer quoi petit ?")
"""
        
# Utilisation de structure "Ternaire"
ton_pays = input("Quel est ton pays : ")
ton_pays = ton_pays.lower()
print("Tu es du pays , brotha ;)") if (ton_pays=='cameroun') else print("T'es pas du pays :| stp PARS !")