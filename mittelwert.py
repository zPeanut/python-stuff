print("Programm zur Mittelwertsbestimmung")
print()
anzahl = input("Wie viele Zahlen möchtest du eingeben? ")
print("Gib nun deine", anzahl, "Zahlen ein!")
summe = 0

for i in range(int(anzahl)):
    zahl = int(input("Zahl: "))
    summe = summe + zahl

mittelwert = summe / int(anzahl)

print("Dein Mittelwert beträgt", float(mittelwert))