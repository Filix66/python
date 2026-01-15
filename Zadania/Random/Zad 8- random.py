# Zadanie 8
# Utwórz nową listę, w której:
# wszystkie liczby ujemne są zastąpione przez 0

import random

liczby = [random.randint(-20, 20) for _ in range(15)]
print(liczby)

print(list(map(lambda x: 0 if x < 0.0 else x,liczby)))  
