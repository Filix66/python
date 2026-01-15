# Zadanie 1
# Wypisz wszystkie liczby z listy.

import random as r

liczby = [r.randint(-20, 20) for _ in range(15)]
print(liczby)

for element in liczby:
    print(element, end=" ")
      
