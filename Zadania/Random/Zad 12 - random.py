# Zadanie 12
# Utwórz listę: liczb parzystych

import random

liczby = [random.randint(-5, 5) for _ in range(15)]
print(liczby)

print(list(filter(lambda x: x > 0,liczby)))
