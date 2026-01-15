# Zadanie 3
# Dla liczb podzielnych przez 3: pomnóż je przez 2 -> wypisz wynik

lista = [1,3,4,5,8,9]

for i in range(len(lista)):
    if lista[i] % 3 == 0:
        liczba = lista[i] * 2
        print(liczba, end=",")


