import random as r

print("Spiel ZAHLENERRATEN")
print()
print("Es wurde zufällig eine Zahl zwischen 1 und 100 ausgewählt!")
print("Deine Aufgabe ist es, die Zahl zu erraten!")
print("Du hast unendlich viele Versuche.")

x = ""
rzahl = r.randint(1, 100)
erzahl = 0
versuche = 1

while(erzahl != rzahl):
    print(x)
    erzahl = int(input("Welche Zahl tippst du? "))
    if(erzahl < rzahl):
        print(x)
        print("%s ist kleiner als die gesuchte Zahl!" % (erzahl))
    else:
        print(x)
        print("%s ist größer als die gesuchte Zahl!" % (erzahl))
    versuche += 1

if(erzahl == rzahl):
    print(x)
    print("Du lagst richtig, die zu erratene Zahl war %s!" % (rzahl))
    print("Du hast %s Versuche gebraucht!" % (versuche))

