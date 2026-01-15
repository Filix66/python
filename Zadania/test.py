# Zadanie 1
#Wypisz wszysstkie liczby z listy

lista = [1,3,4,5,8]

for i in range(len(lista)):
    print(lista[i], end=" ")

print(map(lambda x: lista[x]))
