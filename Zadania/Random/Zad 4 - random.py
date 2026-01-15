# Zadanie 4
# Wypisz tylko liczby: równe zero

import random

liczby = [random.randint(-2, 2) for _ in range(15)]
print(liczby)

for element in liczby:
    if element == 0:
        print(element, end=" ")
      
