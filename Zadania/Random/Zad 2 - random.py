# Zadanie 2
# Wypisz tylko liczby: dodatnie

import random

liczby = [random.randint(-20, 20) for _ in range(15)]
print(liczby)

for element in liczby:
    if element > 0:
        print(element, end=" ")
      
