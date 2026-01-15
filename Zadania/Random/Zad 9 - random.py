# Zadanie 9
# Wypisz liczby:
# większe od średniej arytmetycznej listy

import random

liczby = [random.randint(-20, 20) for _ in range(15)]
print(liczby)

srednia = 0

for element in liczby:
    srednia += element

srednia2 = srednia/len(liczby)
print("średnia przed int: ", srednia2)
print("średnia: ", int(srednia2))

print(list(map(lambda x: x,filter(lambda x: x > srednia2,liczby))))

