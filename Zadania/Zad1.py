# Zadanie 2
# Wypisz tylko liczby parzyste

lista = [1,3,4,5,8]

for i in range(len(lista)):
    if lista[i] % 2 == 0:
        print(lista[i], end=",")
      
