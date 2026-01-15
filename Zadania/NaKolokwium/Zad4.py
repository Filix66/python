# Zadanie 2
# Zamiana liter w liscie duże na małe

#lista = ["x", "d", "b", "x", "z"]
#lista2 = []

#for element in lista:
    #lista2 += str.upper(element)

#print(lista2)


# lista słów i mam zwrócic liste długości słowa każego

lista = ["zółw", "kot", "piesek", "wieloryb"]
#lista2 = []

#for element in lista:
    #x = element
    #lista2 += [len(x)]

#print(lista2)

# zwróc liste w kótórej słow jest odwrócone

#for i in range(-5,0):
    #print(i)

#print(lista[1][2])

#wyraz = ""
#x = 0

#for element in lista:
    #wyraz = ""
    #print(element)
    #for i in range(0,len(element)):
        #wyraz += element[-i-1]

    #lista[x] = wyraz
    #x+=1
    #print("\n")

#print(lista[0][::-1])

#for i in range(len(lista)):
    #lista[i] = lista[i][::-1]

#print(lista)

#print(lista)

# wzróc liste liczb wiekszych niż średnia tej listy

#lista3 = [3,4,1,3,4,5]

#srednia = sum(lista3)/len(lista3)
#print(srednia)

#lista3 = list(filter(lambda x: x>srednia,lista3))

#print(lista3)

# zwróc liste bez duplikatów w tej samej kolejności

#lista4 = [1,2,3,1,2,3]
#lista5 = []

#for element in lista4:
    #if lista5.count(element) < 1:
        #lista5 += [element]

#print(lista5)
    
# zwróć swoła zaczynająć się na samogłowke

#list6 = ["ala","kot","ola","pies"]

#for element in list6:
    
dane = ['ala', 'kot', 'ola', 'pies']

def slowa_na_samogloske(lista):
    samogloski = "aeiouyąęóAEIOUYĄĘÓ"
    return [slowo for slowo in lista if slowo[0] in samogloski]
print(slowa_na_samogloske(dane))  # ['ala', 'ola']


