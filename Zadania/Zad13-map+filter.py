# Zadanie 12
# Dana lista: d = [1, 2, 3, 4, 5, 6]
# wybierz liczby podzielne przez 3, każdą z nich pomnóż przez 2

d = [1, 2, 3, 4, 5, 6,66]

#wynik = filter(lambda x: x % 3 == 0, d)

#wynik2 = map(lambda y: y * 2, wynik)

#print(list(wynik2))

for i in d:
    if i % 3 == 0:
        x = i * 2
        print(x)

print(list(map(lambda x: x * 2,filter(lambda x: x % 3 == 0,d))))

