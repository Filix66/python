# Zadanie 13
# Utwórz listę: wartości bezwzględnych liczb

import random
import math

liczby = [random.randint(-5, 5) for _ in range(15)]
print(liczby)

print(list(map(lambda x: abs(x),liczby)))

