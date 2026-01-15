# Zadanie 9
# Dana lista: a = [1, 2, 3, 4, 5], Utwórz nową listę, w której:
# każda liczba jest pomnożona przez 3

a = [1, 2, 3, 4, 5]


#lista = map(lambda x: x * 3, a)
#print(list(lista))
# TO SAMO CO WYŻEJ TYLKO W JEDNEJ LINI

print(list(map(lambda x: x * 3, a)))
