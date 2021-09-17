import random

kontostand = 0
devmode = False

def main():
    global kontostand
    kontostand = 150
    print("SPIELE AUTOMAT")
    print("made by Mustafa | if11")
    print()
    menu()

def menu():
    global devmode
    global kontostand
    if(devmode):
        print("---- DEV MODE ----");
    else:
        print("---- HAUPTMENÜ ----")
    print()
    print("[1] Spiel eine Runde! (50 Münzen)")
    print("[2] Lade Münzen auf")
    print("[3] Checke deinen Kontostand")
    print("[4] How to play")
    eingabe = int(input("> "))

    if(eingabe == 1): spiel()
    elif(eingabe == 2): money()
    elif(eingabe == 3): konto()
    elif (eingabe == 4): info()
    elif (eingabe == 100): devmode = True; kontostand = 100000; menu()
    else: menu()

def money():
    global kontostand
    print()
    print("---- MÜNZEN AUFLADER ----")
    print()
    print("Du hast zurzeit %d Münzen auf deinem Konto." % kontostand)
    print("Werf Münzen rein um Spielen zu können! 50 max.")
    print()
    money = int(input("> "))
    if(money > 50):
        print()
        print("Zu viele Münzen auf einmal!")
        print()
        menu()
    elif (money <= 50):
        print()
        kontostand += money
        print("Es wurden %d auf dein Konto zugewiesen." % money)
        print("Dein Kontostand beträgt nun: %d" % kontostand)
        print()
        menu()
    else:
        menu()

def konto():
    print()
    print("---- KONTOSTAND ----")
    print()
    print("Dein Kontostand beträgt zurzeit:")
    global kontostand
    print("-- %d Münzen --" % int(kontostand))
    print()
    menu();

def info():
    print()
    print("---- HOW TO PLAY ----")
    print()
    print("Es werden zufällig 5 Zahlen zwischen 1 und 5 generiert.")
    print("Deine Aufgabe ist es, diese 5 Zahlen zu erraten.")
    print()
    print("Es kommen KEINE Zahlen doppelt vor.")
    print()
    print("Ein Spiel kostet 50 Münzen + deinen extra Einwurf. Wenn du keine Münzen mehr hast, hast du verloren!")
    print("Dabei gibt es folgende Preise:")
    print()
    print("Kleiner Gewinn:")
    print("Du errätst die 1. und die 5. Zahl richtig.")
    print("Gewinn: 20 Münzen * deinen Einsatz")
    print()
    print("Großer Gewinn:")
    print("Du errätst die 2, 3 und 4. Zahl richtig.")
    print("Gewinn: 50 Münzen * deinen Einsatz")
    print()
    print("Jackpot:")
    print("Du errätst alle Zahlen richtig.")
    print("Gewinn: 100 Münzen * deinen Einsatz")
    print()
    print("Hast du keine Zahlen richtig, verlierst du 20 Münzen * deinen Einsatz.")
    print()
    menu()

def spiel():

    # 50 Münzen abgezogen
    global kontostand
    if(kontostand <= 0):
        print()
        print("Nicht genug Münzen verfügbar!")
        print()
        menu()
    kontostand_old = kontostand
    kontostand -= 50
    print()
    print("Dein Kontostand:")
    print("%d -> %d" % (kontostand_old, kontostand))
    print("--------------------------------------------")

    # Zahlen Generation
    zahlen = random.sample(range(1, 6), 5)


    # Einsatz
    print("Setze deinen Einsatz!")
    einsatz = int(input("> "))
    if(einsatz > kontostand):
        print("Dein Einsatz war zu hoch!")
        menu()
    elif(einsatz != 0):
        kontostand_before_einsatz = kontostand
        kontostand -= einsatz
        print()
        print("Dein Kontostand:")
        print("%d -> %d" % (kontostand_before_einsatz, kontostand))
        print("--------------------------------------------")
    else:
        einsatz = 1 # damit nicht (gewinn * 0) gerechnet wird, was den gewinn null macht


    # Zahlen Raten
    if(devmode):
        print("dev:", zahlen)
    print("Gebe jetzt deine 5 Zahlen ein!")
    userzahlen = []

    for i in range(5):
        eingabe = int(input("> "))
        userzahlen.append(eingabe)
        if(eingabe > 5 or eingabe <= 0):
            print("Ungültiger Wert!")
            print()
            menu()

    # jackpot

    if (userzahlen == zahlen):
        kontostand_before_gewinn = kontostand
        kontostand += 100 * einsatz
        y = kontostand - kontostand_before_gewinn
        print("--------------------------------------------")
        print("J A C K P O T !")
        print("--------------------------------------------")
        print("%d -> %d | Du hast %d Münzen gewonnen!" % (kontostand_before_gewinn, kontostand, y))
        print()
        print("Deine Zahlen waren", zahlen)
        print()
        menu()

    # kleiner gewinn

    elif (userzahlen[0] == zahlen[0] and userzahlen[4] == zahlen[4]):
        kontostand_before_gewinn = kontostand
        kontostand += 20 * einsatz
        y = kontostand - kontostand_before_gewinn
        print("--------------------------------------------")
        print("K L E I N E R  G E W I N N !")
        print("--------------------------------------------")
        print("%d -> %d | Du hast %d Münzen gewonnen!" % (kontostand_before_gewinn, kontostand, y))
        print()
        print("Deine Zahlen waren", zahlen)
        print()
        menu()

    # großer gewinn
    elif (userzahlen[1] == zahlen[1] and userzahlen[2] == zahlen[2] and userzahlen[3] == zahlen[3]):
        kontostand_before_gewinn = kontostand
        kontostand += 50 * einsatz
        y = kontostand - kontostand_before_gewinn
        print("--------------------------------------------")
        print("G R O ß E R  G E W I N N !")
        print("--------------------------------------------")
        print("%d -> %d | Du hast %d Münzen gewonnen!" % (kontostand_before_gewinn, kontostand, y))
        print()
        print("Deine Zahlen waren", zahlen)
        print()
        menu()

    # jackpot


    # alles andere
    else:
        kontostand_before_loss = kontostand
        kontostand -= 20 + einsatz
        y = kontostand - kontostand_before_loss
        print("--------------------------------------------")
        print("-- V E R L O R E N ! --")
        print("--------------------------------------------")
        print("%d -> %d | Du hast %d Münzen verloren!" % (kontostand_before_loss, kontostand, y))
        print()
        print("Deine Zahlen waren", zahlen)
        print()
        # loss
    if(kontostand <= 0):
        lose()
    menu()

def lose():
    print("--------------------------------------------")
    print("Du hast verloren! Dein Konto hat entweder kein Geld mehr oder du hast Schulden angesammelt.")
    print("Willst du neu anfangen?")
    print("--------------------------------------------")
    antwort = input("[Y/N] ")
    if(antwort == "Y" or antwort == "y"): main()
    elif(antwort == "N" or antwort == "n"): exit()
    else: exit()

if __name__ == '__main__':
    main()