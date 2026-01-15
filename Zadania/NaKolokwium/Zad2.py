# Zadanie 1
# a) modyfikuje wejściową liste liczb całkowitych w ten sposób, że wszystkie
# elementy oprócz pierwszego i ostatniego zostaną zastąpione 0

lista = [2,3,4,5,6,7,8,9]

for i in range(len(lista)):
    if i == lista[0] or i == len(lista)-1:
        continue
    else:
        lista[i] = 0

print(lista)

lista = [2,3,4,5,6,7,8,9]
print(list(map(lambda x: x if x == lista[0] or x == lista[-1] else 0,lista)))

lista[:] = map(
    lambda ix: ix[1] if ix[0] == 0 or ix[0] == len(lista) - 1 else 0,
    enumerate(lista)
)

print(lista)

# enumerate -> daje Ci jednocześnie indeks i wartość elementu
# z listy (lub innej sekwencji).

# b) modyfikuje wejściową listę liczb całkowitych w ten sposób, że usuwa z niej
# wszystkie elementy dodatnie

lista2 = [-2,3,-4,5,-6,7,-8,9]

#lista2[:] = [x for x in lista2 if x<= 0]

lista2 = list(filter(lambda x: x <= 0,lista2))

print(lista2)

# c) wczytanie liczby całkowitej n i prowadzenie do listy cyfr jej
# rozwiniecia dziesietnego. Powtarzajacych się cyfr nie należy
# wprowadzać ponownie.

a = input("liczba: ")
wynik = []

for cyfra in a:
    #print(cyfra)
    #if int(cyfra) not in wynik:
    #print(wynik.count(int(cyfra)))
    if wynik.count(int(cyfra)) < 1:
        wynik.append(int(cyfra))

print(wynik)





















