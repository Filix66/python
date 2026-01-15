# Zad 5
# Dla każdej osoby wypisz: nazwisko oraz liczbę liter w nazwisku

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
    for i in range(len(nazwisko)):
        ilosc += 1
    print(nazwisko, " ilość liter: ", ilosc)
