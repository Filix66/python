# Zadanie 11
# Sprawdź: czy w liście występuje liczba 5

import random

liczby = [random.randint(-5, 5) for _ in range(15)]
print(liczby)

if liczby.count(5) > 0:
    print("Tak znajdują się")
