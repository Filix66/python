# Zad 7
# Wypisz osoby, których: imię ma więcej niż 5 liter

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
    if len(imie) > 5:
        print(imie)
