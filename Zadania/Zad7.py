# Zadanie 7
# Znajdź: największą, najmniejszą liczbę w liście



#liczby = [1, 2, 3, 4, 5, 6]
liczby = [3, 4, 1, 5, 3, 7]
liczbaMin = liczby[0]
liczbaMax = liczby[0]

for i in range(len(liczby)):
    if liczbaMin > liczby[i]:
        liczbaMin = liczby[i]
    if liczbaMax < liczby[i]:
        liczbaMax = liczby[i]

print("liczbaMin: ", liczbaMin)
print("liczbaMax: ", liczbaMax)
