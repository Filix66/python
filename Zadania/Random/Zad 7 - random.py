# Zadanie 7
# Utwórz nową listę, w której:
# każda liczba parzysta jest pomnożona przez 2
# każda nieparzysta pozostaje bez zmian

import random

liczby = [random.randint(-20, 20) for _ in range(15)]
print(liczby)

print(list(map(lambda x: x * 2 if x % 2 == 0 else x, liczby)))
      
