# Zad 16
# Wypisz wszystkie osoby z listy.

osoby = [
    "Piotr Kowalski",
    "Anna Nowak",
    "Paweł Kaczmarek",
    "Patrycja Zielińska",
    "Marek Wiśniewski",
    "Paulina Adamska",
    "Jan Piotrowski"
]

print(list(map(lambda x: x,osoby)))


#for i in range(len(osoby)):
    #print(osoby[i], end="\n")
