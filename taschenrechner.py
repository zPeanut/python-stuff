print("Ein einfacher Taschenrechner")

zahl1 = float(input("Gebe deine erste Zahl ein: "))
zahl2 = float(input("Gebe deine zweite Zahl ein: "))
print("Addition, Subtraktion, Division, Multiplikation, Potenz")
print("Bei der Potenzrechnung wird deine zweite Zahl als Exponent genommen.")
method = input("Gebe deine Art von Rechnung ein: ")

if(method == "Addition"):
  resultAdd = zahl1 + zahl2
  print("Dein Ergebnis ist:", resultAdd)

if(method == "Substraktion"):
  resultSub = zahl1 - zahl2
  print("Dein Ergebnis ist:", resultSub)

if(method == "Division"):
  resultDiv = zahl1 / zahl2
  print("Dein Ergebnis ist:", resultDiv)

if(method == "Multiplikation"):
  resultMul = zahl1 * zahl2
  print("Dein Ergebnis ist:", resultMul)

if(method == "Potenz"):
  resultPot = zahl1 ** zahl2
  print("Dein Ergebnis ist:", resultPot)



