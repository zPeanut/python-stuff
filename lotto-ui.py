import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
import random as r
import threading
print()
print("--- DEBUG CONSOLE ---")
global kontostand
global einsatz
kontostand = 0
einsatz = 0

def main():
    global kontostand
    global einsatz

    window = tk.Tk()
    window.resizable(False, False)
    window.title("Lotto UI")

    def change_kontostand_debug():
        global kontostand
        kontostand = int(input("> "))
        window.after(100, change_kontostand_debug)

    # centre window and set size

    window_height = 200
    window_width = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

    # FUNKTIONEN

    def spiel():
        global kontostand
        global einsatz

        # 50 Münzen abgezogen
        kontostand_old = kontostand
        kontostand -= 50
        if (kontostand < 0):
            msg.showerror("Lotto UI", "Nicht genug Münzen vorhanden!")
            kontostand += 50
            return
        else:
            top = tk.Toplevel(window)
            top.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
            top.resizable(False, False)
            msg.showinfo("Lotto UI", "Dein Kontostand:\n%d -> %d" % (kontostand_old, kontostand), parent=top)
            zahlen = r.sample(range(1, 6), 5)

            # Einsatz ( top 2 )
            def eingabeeinsatz():
                top2 = tk.Toplevel(top)
                top2.geometry("{}x{}+{}+{}".format(window_width - 80, window_height - 80, x_coordinate + 40, y_coordinate + 40))
                top2.resizable(False, False)

                def eingabe2():
                    global einsatz
                    global kontostand
                    data_str = einsatz_entry.get()
                    einsatz = int(data_str)
                    if (einsatz > kontostand):
                        msg.showerror("Lotto UI", "Dein Einsatz war zu hoch!", parent=top2)
                    elif (einsatz != 0):
                        kontostand_before_einsatz = kontostand
                        kontostand -= einsatz
                        msg.showinfo("Lotto UI", "Dein Kontostand:\n%d -> %d" % (kontostand_before_einsatz, kontostand), parent=top2)
                        top2.destroy()
                        zahlenraten()
                    else:
                        einsatz = 1  # damit nicht (gewinn * 0) gerechnet wird, was den gewinn null macht
                        top2.destroy()
                        zahlenraten()

                title = tk.Label(top2, text="Einsatz", font="Arial 16 bold")
                text = tk.Label(top2, text="Setze deinen Einsatz!", anchor="e", justify=tk.LEFT)
                einsatz_entry = Entry_int(top2, width=40, foreground="black", justify=tk.CENTER)
                btn = ttk.Button(top2, text="OK", width=20, command=eingabe2)

                title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-40)
                text.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-15)
                einsatz_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=12)
                btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=43)

                top2.mainloop()

        # eigentliches Spiel
        def zahlenraten():
                global einsatz
                global kontostand

                # Zahlen Raten
                print(einsatz)
                print(zahlen)
                msg.showinfo("Lotto UI", "Gebe jetzt deine 5 Zahlen ein!", parent = top)

                def gewinn():
                    global kontostand
                    global einsatz
                    userzahlen = []
                    userzahlen.extend((int(text1.get()), int(text2.get()), int(text3.get()), int(text4.get()), int(text5.get())))
                    # jackpot
                    if (userzahlen == zahlen):
                        kontostand_before_gewinn = kontostand
                        kontostand += 100 * einsatz
                        y = kontostand - kontostand_before_gewinn
                        msg.showinfo("Lotto UI", "JACKPOT!\n\n%d -> %d | Du hast %d Münzen gewonnen!\n\nDie Zahlen waren:\n%s\n\nDeine Zahlen waren:\n%s" % (kontostand_before_gewinn, kontostand, y, userzahlen, zahlen))
                        print("Kontostand:", kontostand)
                        top.destroy()

                    # kleiner gewinn
                    elif (userzahlen[0] == zahlen[0] and userzahlen[4] == zahlen[4]):
                        kontostand_before_gewinn = kontostand
                        kontostand += 20 * einsatz
                        y = kontostand - kontostand_before_gewinn
                        msg.showinfo("Lotto UI","KLEINER GEWINN!\n\n%d -> %d | Du hast %d Münzen gewonnen!\n\nDie Zahlen waren:\n%s\n\nDeine Zahlen waren:\n%s" % (kontostand_before_gewinn, kontostand, y, userzahlen, zahlen))
                        print("Kontostand:", kontostand)
                        top.destroy()

                    # großer gewinn
                    elif (userzahlen[1] == zahlen[1] and userzahlen[2] == zahlen[2] and userzahlen[3] == zahlen[3]):
                        kontostand_before_gewinn = kontostand
                        kontostand += 50 * einsatz
                        y = kontostand - kontostand_before_gewinn
                        msg.showinfo("Lotto UI", "GROßER GEWINN!\n\n%d -> %d | Du hast %d Münzen gewonnen!\n\nDie Zahlen waren:\n%s\n\nDeine Zahlen waren:\n%s" % (kontostand_before_gewinn, kontostand, y, userzahlen, zahlen))
                        print("Kontostand:", kontostand)
                        top.destroy()

                    # alles andere
                    else:
                        kontostand_before_loss = kontostand
                        kontostand -= 20 * einsatz
                        y = kontostand - kontostand_before_loss
                        msg.showinfo("Lotto UI", "VERLOREN!\n\n%d -> %d | Du hast %d Münzen verloren!\n\nDie Zahlen waren:\n%s\n\nDeine Zahlen waren:\n%s" % (kontostand_before_loss, kontostand, y, userzahlen, zahlen))
                        print("Kontostand:", kontostand)
                        top.destroy()

                        # loss
                    if (kontostand < 0):
                        lose()

                title = tk.Label(top, text="Lotto Eingabe", font="Arial 22 bold")
                text1 = Entry_int(top, width=2, font="Arial 28 bold")
                text2 = Entry_int(top, width=2, font="Arial 28 bold")
                text3 = Entry_int(top, width=2, font="Arial 28 bold")
                text4 = Entry_int(top, width=2, font="Arial 28 bold")
                text5 = Entry_int(top, width=2, font="Arial 28 bold")
                btn = ttk.Button(top, text="Eingabe!", width=20, command=gewinn)

                title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-70)
                text1.place(x=56, y=66)
                text2.place(x=116, y=66)
                text3.place(x=176, y=66)
                text4.place(x=236, y=66)
                text5.place(x=296, y=66)
                btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=43)
                top.mainloop()
        eingabeeinsatz()

    def kontocharge():
        top = tk.Toplevel(window)
        top.geometry("{}x{}+{}+{}".format(window_width - 40, window_height - 40, x_coordinate + 20, y_coordinate + 20))
        top.resizable(False, False)

        def buttonclick_kontocharge():
            global kontostand
            if (eingabe.get() == "86"):
                try:
                    inputeingabe = int(input("Kontostand -> "))
                    kontostand = int(inputeingabe)
                    print("Kontostand:", kontostand)
                    msg.showinfo("Lotto UI", "Es wurden %d Münzen auf dein Konto zugewiesen.\n\nDein Kontostand beträgt nun: %d Münzen." % (inputeingabe, kontostand), parent=top)
                except ValueError:
                    print("Keine gültige Nummer!")
                except RuntimeError:
                    print("Runtime Error!")
            elif (int(eingabe.get()) > 50):
                msg.showerror("Lotto UI", "Zu viele Münzen auf einmal!", parent = top)
            elif (int(eingabe.get()) <= 50):
                kontostand += int(eingabe.get())
                msg.showinfo("Lotto UI", "Es wurden %d Münzen auf dein Konto zugewiesen.\n\nDein Kontostand beträgt nun: %d Münzen." % (int(eingabe.get()), kontostand), parent = top)
                print("Kontostand:", kontostand)
            else:
                # this shouldnt happen
                msg.showerror("Lotto UI", "Ungültiger Wert!")

        title = tk.Label(top, text="Münzen Auflader", font="Arial 16 bold")
        text1 = tk.Label(top, text="Werfe Münzen rein um spielen zu können!\nEs können nur maximal 50 Münzen reingeworfen werden.", anchor = "e", justify = tk.LEFT)
        text2 = tk.Label(top, text="Wieviele Münzen willst du reinwerfen?", anchor = "e", justify = tk.LEFT)
        eingabe = Entry_int(top, width=20, foreground="black")
        button_pay = ttk.Button(top, text="Einzahlen!", command=buttonclick_kontocharge, width=20)
        button_exit = ttk.Button(top, text="Schließen", command = top.destroy, width=20)

        title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-60)
        text1.place(x=6, y=45)
        text2.place(x=6, y=95)
        eingabe.place(x=215, y=96)
        button_pay.place(x=6, y=120)
        button_exit.place(x=213, y=120)

    def tutorial():
        message = "---- HOW TO PLAY ---- " \
                  "\n\nEs werden zufällig 5 Zahlen zwischen 1 und 5 generiert." \
                  "\nDeine Aufgabe ist es, diese 5 Zahlen zu erraten." \
                  "\n\nEs kommen KEINE Zahlen doppelt vor." \
                  "\n\nEin Spiel kostet 50 Münzen + deinen extra Einwurf." \
                  "\nWenn du keine Münzen mehr hast, hast du verloren!" \
                  "\n\nDabei gibt es folgende Preise:" \
                  "" \
                  "\n\nKleiner Gewinn:" \
                  "\nDu errätst die 1. und die 5. Zahl richtig." \
                  "\nGewinn: 20 Münzen * deinen Einsatz." \
                  "" \
                  "\n\nGroßer Gewinn:" \
                  "\nDu errätst die 2, 3 und 4. Zahl richtig." \
                  "\nGewinn: 50 Münzen * deinen Einsatz." \
                  "" \
                  "\n\nJackpot:" \
                  "\nDu errätst alle Zahlen richtig." \
                  "\nGewinn: 100 Münzen * deinen Einsatz."
        msg.showinfo("Lotto UI", message)

    # GUI
    title = tk.Label(window, text="Spieleautomat", font="Arial 22 bold")
    btn_play = ttk.Button(window, text="Spiel eine Runde (50 Münzen!)", width=40, command = spiel)
    btn_charge = ttk.Button(window, text="Lade deine Münzen auf!", width=40, command = kontocharge)
    btn_kontostand = ttk.Button(window, text="Checke deinen Kontostand", width=40, command=kontocheck)
    btn_tutorial = ttk.Button(window, text="Tutorial / How to play", width=40, command = tutorial)
    btn_exit = ttk.Button(window, text="Schließen", width=40, command=exit)

    title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-76)
    btn_play.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-40)
    btn_charge.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-10)
    btn_kontostand.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=20)
    btn_tutorial.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=50)
    btn_exit.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=80)
    print("Kontostand:", kontostand)
    window.mainloop()

def kontocheck():
    global kontostand
    msg.showinfo("Lotto UI", "Dein Kontostand beträgt zurzeit: \n\n%d Münzen." % kontostand)

class Entry_int(ttk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar(master)
        self.var.trace('w', self.validate)
        ttk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.get, self.set = self.var.get, self.var.set
    def validate(self, *args):
        value = self.get()
        if not value.isdigit():
            self.set(''.join(x for x in value if x.isdigit()))

def lose():
    if (msg.askyesno("Lotto UI","Du hast verloren! | GAME OVER!\n\nDein Konto hat entweder kein Geld mehr oder du hast Schulden angesammelt.\n\nWillst du neu anfangen?",icon=msg.ERROR, default=msg.YES)):
        global kontostand
        kontostand = 0
        msg.showinfo("Lotto UI", "Dein Kontostand wurde resettet!")
    else:
        msg.showinfo("Lotto UI", "Danke fürs Spielen!\n\nMade by Mustafa | Informatik 11")
        exit()


# stackoverflow, int entry template

class Entry_int(ttk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar(master)
        self.var.trace('w', self.validate)
        ttk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.get, self.set = self.var.get, self.var.set
    def validate(self, *args):
        value = self.get()
        if not value.isdigit():
            self.set(''.join(x for x in value if x.isdigit()))

if __name__ == "__main__":
    main()
