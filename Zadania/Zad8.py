# Zadanie 8
# Policz ile w liście jest: liczb parzystych, liczb nieparzystych

import random

lista = []
par = 0
niepar = 0

for i in range(6):
    lista += [random.randint(0,15)]

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par += 1
    else:
        niepar += 1
        
print(lista)
print("par: ", par, " niepar: ", niepar)
