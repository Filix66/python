# Zadanie 14
# Dana lista: e = [-3, -2, -1, 0, 1, 2, 3]
# wybierz liczby dodatnie, podnieś je do kwadratu

e = [-3, -2, -1, 0, 1, 2, 3]

print(list(map(lambda x: x * x,filter(lambda y: y >= 0,e))))
