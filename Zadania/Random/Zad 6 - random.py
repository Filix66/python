# Zadanie 6
# Utwórz nową listę, w której:
# każda liczba zostaje podniesiona do kwadratu

import random

liczby = [random.randint(-20, 20) for _ in range(15)]
print(liczby)

print(list(map(lambda x: x * x, liczby)))
      
