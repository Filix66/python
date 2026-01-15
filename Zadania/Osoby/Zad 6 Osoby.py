# Zad 6
# Dla każdej osoby wypisz:

osoby = [
    "Piotr Kowalski",
    "Anna Nowak",
    "Paweł Kaczmarek",
    "Patrycja Zielińska",
    "Marek Wiśniewski",
    "Paulina Adamska",
    "Jan Piotrowski"
]

    #if osoby[0][i] != ' ':
        #print(osoby[0][i])

for i in range(len(osoby)):
    ilosc = 0
    osoba = osoby[i]
    for j in range(len(osoba)):
        if osoba[j] != ' ':
            ilosc += 1
    print(osoba, " Ilość: ", ilosc)
    
