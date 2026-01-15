# Zad 4
# Dla każdej osoby wypisz: imię oraz liczbę liter w imieniu

osoby = [
    "Piotr Kowalski",
    "Anna Nowak",
    "Paweł Kaczmarek",
    "Patrycja Zielińska",
    "Marek Wiśniewski",
    "Paulina Adamska",
    "Jan Piotrowski"
]

for i in range(len(osoby)):
    ilosc = 0
    imie, nazwisko = osoby[i].split()
    for i in range(len(imie)):
        ilosc += 1      
    print(imie, " ilość zanków: ", ilosc)

