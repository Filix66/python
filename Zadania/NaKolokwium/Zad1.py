# Zadanie 1
# a) modyfikuje wejściową liste liczb całkowitych w ten sposób, że wszystkie
# elementy oprócz pierwszego i ostatniego zostaną zastąpione swoimi kwadratami

lista = [2,3,4,5,6,7,8]

for i in range(len(lista)):
    if lista[0] == lista[i]:
        print("to jest pierwszye lement")
    elif lista[-1] == lista[i]:
        print("to jest ostatni element lement")
    else:
        lista[i] = lista[i] * lista[i]

#print(lista)

wynik2 = list(map(lambda x: x if x == lista[0] or x == lista[-1] else 1 ,lista))

print(wynik2)
 
#lista = [2,3,4,5,6,7,8]

#wynik = [x if i in (0, len(lista)-1) else x**2 for i, x in enumerate(lista)]

#print(list(wynik))

lista2 = [2,3,4,5,6,7,8,9]
# b) modyfikuje wejściową liste liczb całkowitych w ten sposób, że usuwa z niej wszystkie
# elementy podzielne przez 3

for element in lista2:
    if element % 3 == 0:
        lista2.remove(element)

#lista2[:] = list(filter(lambda x: x % 3 != 0, lista2))

print(lista2)

# c) wczytanie liczb całkowitych a i b, a następnie wprowadzenie do
# listy wszystkich liczb pierwszych z przedziału <a:b>

a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))

#5 / 5 = true
#5 / 4 = false
#5 / 3 = false
#5 / 2 = false
#5 / 1 = true

# 6 / 6 = true
# 6 / 5 = false
# 6 / 4 = false
# 6 / 3 = true
# 6 / 2 = true
# 6 / 1 = true

wynik = 0
liczbyPierwsze = []

for i in range(a,b + 1):
    wynik = 0
    #print("Liczba: ", i)
    for y in range(1,i+1):
        #print("Dzielenie: ", y, " i % y == 0: ", i % y == 0)
        if i % y == 0:
            wynik += 1
    if wynik == 2:
        liczbyPierwsze += [i]
        #print(i, "jest liczbą pierwsza")

print(liczbyPierwsze)
