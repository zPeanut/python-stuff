from time import sleep

print("TEXT-BASIERTES ABENTEUER SPIEL")
print()
name = input("Guten Morgen Schüler, was ist dein Name? ")
print()
print("Willkommen", name, "zu diesem Text-Basiertem Abenteuerspiel, welches in deiner Schule handelt.")
print("Es ist zurzeit Freitag, 7 Uhr morgens. Dein Wecker reißt dich aus dem Schlaf.")
print()
print("Stehst du auf?")
print("[A] Ja, ich stehe auf.")
print("[B] Nein, ich bleibe im Bett.")
schlaf = input("> ")

if (schlaf == "a" or schlaf == "A"):

    # duschen / schlafen

    print()
    print("Du stehst aus deinem Bett auf. Du gehst raus aus deinem Zimmer und hast nun die Wahl.")
    print()
    print("Gehst du entweder:")
    print("[A] Frühstücken")
    print("[B] Duschen")
    entscheidung2 = input("> ")
    aufstehen = True;
    duschen = False;
    frühstück = False;

    # frühstück

    if (entscheidung2 == "a" or entscheidung2 == "A"):
        print()
        print("Du startest energiereich in den Tag und musst dich in der Schule nicht mit Hunger quälen.")
        frühstück = True;

    if (entscheidung2 == "b" or entscheidung2 == "B"):
        print()
        print(
            "Du startest frisch und gut gelaunt in den Tag aber du verspürst Hunger, da du nicht mehr Zeit hattest zu frühstücken.")
        duschen = True;

if (schlaf == "b" or schlaf == "B"):
    print()
    print(
        "Du hast deinen gesamten Schultag unentschuldigt verpasst. Dies war dein letzter Verweis, somit wirst du nun von der Schule verwiesen.")
    print("GAME OVER - schlechtes Ende.")
    duschen = False;
    frühstück = False;

# SPORT BLOCK

if (duschen or frühstück):
    print()
    print("Es ist 8 Uhr morgens. Dein erster Block heute ist Sport.")

    if (duschen):
        print()
        print("Deine Freunde komplimentieren deinen Duft")
        print("\"Wow,", name, "du riechst heute ja sehr gut!\", sagt dein Scharm.")
        print("Du fühlst dich für den restlichen Tag viel selbstbewusster.")

        sleep(4)

        print()
        print("Dir wird bei der Aufwärmung aufeinmal schwindelig.")

        sleep(2)

        print()
        print("...")

        sleep(2)

        print()
        print(
            "Du kippst im weiterem Sportverlauf um. Ein Krankenwagen wird gerufen und du verlässt die Schule für den restlichen Tag.")
        print()
        print("GAME OVER - neutrales Ende.")

    if (frühstück):
        print()
        print(
            "Der Sportunterricht verläuft normal, jedoch kommst du danach verschwitzt in den 2. Block deines Unterrichttages.")
        sleep(2)
        print()
        print("Du siehst aufeinmal, dass neben deinem Schwarm ein Platz frei ist.")
        print("Was machst du?")
        print("[A] Du setzt dich neben ihr hin.")
        print("[B] Du setzt dich alleine an einen anderen Tisch hin.")
        entscheidung3 = input("> ")

        if (entscheidung3 == "a" or entscheidung3 == "A"):
            print()
            print("Du setzt dich neben deinen Schwarm hin. Sie guckt jedoch angeekelt auf dich und sagt:")
            print("\"Ihhhh, wie riechst du denn", name,
                  "? Geh weg und setz dich in Zukunft bitte nicht mehr neben mir.")
            print()
            print("Du wurdest soeben von deinem Schwarm mies abgewiesen. Du bist nun depressiv und fühlst dich für den Rest des Tages absolut miserabel.")
            print("GAME OVER - schlechtes Ende.")

        if (entscheidung3 == "b" or entscheidung3 == "B"):
            print()
            print(
                "Du setzt dich an eine leere Bank und passt im Unterricht fleißig ungestört auf. Dein Mathetest nächste Woche schaffst du mit links!")
            print("Du gehst zufrieden nach Hause und genießt deine Freizeit.")
            print()
            print("GAME OVER - gutes Ende.")
print("Danke fürs spielen! - made by Mustafa and Vera.")