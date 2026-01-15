# Zad 3
# Wypisz osoby, których nazwisko zaczyna się na literę „K”.

osoby = [
    "Piotr Kowalski a x x x",
    "Anna Nowak",
    "Paweł Kaczmarek",
    "Patrycja Zielińska",
    "Marek Wiśniewski",
    "Paulina Adamska",
    "Jan Piotrowski"
]

#test
#osoba = osoby[0]
#imie, nazwisko = osoby[0].split()
#print(imie)
#print(nazwisko)

for i in range(len(osoby)):
    imie, nazwisko = osoby[i].split()
    if nazwisko[0] == "K":
        print(osoby[i])

