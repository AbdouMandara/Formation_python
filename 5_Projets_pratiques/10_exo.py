"""
Créer une fonction qu'on appellera calculette celle – ci prendra 03 
paramètres : number1 , number2  et operator . 
▪ operator ne devra uniquement prendre les valeurs : +, -, *, / 
et % ; et en fonction de cette valeur, la fonction doit retourner le 
résultat de (number1 operator number2).

Exemple : calculette(4, 2, '-’) doit retourner le résultat de 
l’opération (4 – 2) soit 2.00
"""
def calculette(number1:int, number2:int, operator:str)->float :
    match operator :
        case '+' :
            print("{} {} {} soit {}".format(number1, operator, number2, number1 + number2)) 
        case '-' :
            print("{} {} {} soit {}".format(number1, operator, number2, number1 - number2)) 
        case '*' :
            print("{} {} {} soit {}".format(number1, operator, number2, number1 * number2)) 
        case '/' :
            print("{} {} {} soit {}".format(number1, operator, number2, number1 * number2)) if(number1 != 0 and number2 != 0) else ('Division par 0 impossible') 
            

nombre_1_du_user = int(input("Entrez le 1er nombre : "))
nombre_2_du_user = int(input("Entrez le 2ème nombre : "))
opérateur_user = input("Opérateurs dispo : +, -, *, / \nChoissisez : ")
calculette(nombre_1_du_user, nombre_2_du_user, opérateur_user)