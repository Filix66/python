# Zad 2
# Wypisz osoby zaczynajace się na litere P

osoby = [
    "Piotr Kowalski",
    "Anna Nowak",
    "Paweł Kaczmarek",
    "Patrycja Zielińska",
    "Marek Wiśniewski",
    "Paulina Adamska",
    "Jan Piotrowski"
]

#for i in range(len(osoby)):
   #osoba = osoby[i]
   #if osoba[0] == "P":
       #print(osoby[i])

wynik = list(filter(lambda x: x.startswith("Pat"), osoby))

print("\n".join(wynik))


# join -> metoda typu str
# łaczy wile napisów (stringów) w jeden
# separator.join(iterable)
# separator -> np. " ","\n" / iterable -> lista

# startswith -> metoda typu str
# sprawdza, czy napis zaczyna się od danego fragmentu
# string.startswith(prefix) / zwaraca True lub False
# "Piotr".startswith("P") -> True
# "Anna".startswith("P") -> False
