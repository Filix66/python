# Zadanie 5
# Policz, ile jest: liczb dodatnich, liczb ujemnych, zer

import random

liczby = [random.randint(-2, 2) for _ in range(15)]
print(liczby)

dodatnie = 0
ujemne = 0
zerowe = 0

for element in liczby:
    if element > 0.0:
        dodatnie += 1
    elif element < 0.0:
        ujemne += 1
    else:
        zerowe += 1

print("Dodatnie: ", dodatnie, " Ujemne: ", ujemne, " Zerowe: ", zerowe)
      
