# Zad 9
# Policz, ile osób ma: imię zaczynające się na „P”

osoby = [
    "Piotr Kowalski",
    "Anna Nowak",
    "Paweł Kaczmarek",
    "Patrycja Zielińska",
    "Marek Wiśniewski",
    "Paulina Adamska",
    "Jan Piotrowski"
]

ilosc = 0

for i in range(len(osoby)):
    imie, nazwisko = osoby[i].split()
    if imie.startswith("P") or imie.startswith("p"):
        ilosc += 1

print(ilosc)
