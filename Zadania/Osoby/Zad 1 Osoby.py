# Zad 1
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

print("\n".join(map(lambda x: x, osoby)))
