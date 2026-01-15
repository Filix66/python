# Zadanie 10
# Znajdź: największą liczbę w liście, najmniejszą liczbę w liście

import random

liczby = [random.randint(-20, 20) for _ in range(15)]
print(liczby)

maxElement = liczby[0]
minElement = liczby[0]

for element in liczby:
    if maxElement < element:
        maxElement = element
    if minElement > element:
        minElement = element 

print("maxElement -> ", maxElement," maxElement -> ", minElement)
