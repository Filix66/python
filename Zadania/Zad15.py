# Zadanie 15
# Dana lista: f = [2, 5, 8, 11, 14]
# Utwórz listę, w której: każda liczba zostaje zastąpiona:
# 0 jeśli jest parzysta , 1 jeśli jest nieparzysta

f = [2, 5, 8, 11, 14]

#lista = []

#for i in range(len(f)):
    #if f[i] % 2 == 0:
        #lista += [0]
    #else:
        #lista += [1]

#print(lista)

print(list(map(lambda x: 0 if x % 2 == 0 else 1,f)))

# DODATEK     
#wynik = [0 if x % 2 == 0 else 1 for x in f]
#print(wynik)
