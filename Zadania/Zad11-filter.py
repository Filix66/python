# Zadanie 11
# Z listy: c = [1, 2, 3, 4, 5, 6, 7, 8]
# Wybierz: tylko liczby nieparzyste

c = [1, 2, 3, 4, 5, 6, 7, 8,13,16]

print(list(filter(lambda x: x % 2 != 0, c)))
