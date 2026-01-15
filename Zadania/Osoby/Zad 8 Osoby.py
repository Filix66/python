# Zad 8
# Wypisz osoby, których: nazwisko ma dokładnie 6 liter

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
    imie, nazwisko = osoby[i].split()
    if len(nazwisko) == 6:
        print(nazwisko)
