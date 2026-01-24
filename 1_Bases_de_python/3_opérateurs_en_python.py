# 1 - Opérateurs arithmétiques
a = 15
b = 5

addition = a+b
soustraction = a-b
multiplication = a*b
division = a/b if (a != 0 and b !=0 ) else print("Un nombre est égal à 0, donc division impossible")
division = int(division)
"""
print(addition)
print(soustraction)
print(multiplication)
"""
print(division) 

# 2 - Opérateurs logiques
x = 5
print(x > 2 and x<10) #ça retoourne True

if(x>5 or x <10):
    print("x est entre 5 et 10")
    
if(not(x>5)) :
    print("{} est inférieur à 5".format(x))