# created by peanut on the 20th sep 2021
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

import random

# hauptfunktion
def main():

    # vorkmerkungen:
    #
    # "relx=0.5, rely=0.5, anchor=tk.CENTER, y=..." zentriert ein widget
    # ich benutze nur ttk.Buttons weil sie besser aussehen als die standard ones

    # ---------------- HAUPTFENSTER SETUP ---------------------

    window = tk.Tk()
    window.resizable(False, False)
    window.title("Das 1x1")

    # das hier dient dem zweck, das fenster beim startup zu zentrieren

    window_height = 150
    window_width = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

    # -------------- FUNKTIONEN ------------------

    # 1 mal 1 anzeigen lassen

    def ask_1mal1_anzeigen():

        # ein toplevel window vom hauptfenster wird erstellt

        top_ask = tk.Toplevel(window)
        top_ask.geometry("{}x{}+{}+{}".format(window_width - 40, window_height - 40, x_coordinate + 20, y_coordinate + 20))
        top_ask.resizable(False, False)

        # labels

        title = tk.Label(top_ask, text="Soll ich:", font="Arial 18 normal")
        btn_groß = ttk.Button(top_ask, text="Das große 1x1 anzeigen?", command=lambda: [top_ask.destroy(), groß_1mal1_anzeigen()], padding=3)  # zwei commands werden gleichzeitig ausgeführt mit dem lambda befehl
        btn_klein = ttk.Button(top_ask, text="Das kleine 1x1 anzeigen?", command=lambda: [top_ask.destroy(), klein_1mal1_anzeigen()], padding=3)

        title.place(x=40, y=35)
        btn_klein.place(x=180, y=20)
        btn_groß.place(x=180, y=60)

    def klein_1mal1_anzeigen():

        # toplevel wird vom hauptfenster erstellt

        top = tk.Toplevel(window)
        top.geometry("{}x{}+{}+{}".format(window_width - 20, window_height - 20, x_coordinate + 10, y_coordinate + 10))
        top.resizable(False, False)
        top.title("Das kleine 1x1")

        # calc funktion, welche die zahlen berechnet

        def calc():

            # guckt = ist die eingabe ein int?, wenn nicht = valueerror = ungültige eingabe
            # dies dient dem zweck, nicht den base 10 int error auszulösen

            try:

                # eingabe wird in ein int konvertiert

                number = int(eingabe.get())

                # kleiens 1 mal 1, daher alle zahlen unter 11

                if (number <= 10):

                    # zahlen string wird deklariert

                    zahlen = ""

                    for i in range(11):

                        # erstes %d = die eingabe nummer
                        # zweites %d = die wiederholung des loopes (1,2,3,4,5...)
                        # drittes %d = das produkt beider zahlen
                        # die zwei \n dienen dazu, immer 2 leerzeilen unter einem string zu haben

                        # die variable message wird dann zur variable "zahlen" hinzugefügt als eine art liste

                        message = "%dx%d = %d\n\n" % (number, i, (i * number))
                        zahlen += message

                    # messagebox - showinfo, zahlen wird gedruckt
                    # parent ist top, quasi die messagebox wird vom toplevel aus angezeigt

                    msg.showinfo("", zahlen, parent=top)

                    # user nachfrage ob er noch eine reihenfolge sehen will
                    # ja = die eingabe wird gelöscht, und der code wird wiederholt (return)
                    # nein = das fenster wird geschlossen

                    if(msg.askyesno("", "Willst du noch eine Reihenfolge sehen?", parent=top)):
                        eingabe.delete(0, tk.END)
                        return
                    else:
                        top.destroy()

                else:
                    msg.showerror("", "Bitte gebe eine Zahl unter 11 ein!", parent=top)
            except ValueError:
                msg.showerror("Das 1x1", "Keine gültige Nummer!", parent=top)

        # labels

        title = tk.Label(top, text="Die 1x1 Maschine", font="Arial 18 normal")
        text1 = tk.Label(top, text="Tippe eine Nummer ein, um davon das kleine 1x1 zu \nbekommen!", anchor="e", justify=tk.LEFT, font = "Arial 10 normal")
        eingabe = Entry_int(top, width=20, foreground="black", font="Arial 12 normal")
        btn_calc = ttk.Button(top, text="Rechne!", command=calc, width=20)

        title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-40)
        text1.place(x=29, y=50)
        eingabe.place(x=29, y=92)
        btn_calc.place(x=223, y=92)

    def groß_1mal1_anzeigen():

        # hier das selbe, unterschied ist dass der loop nun 21 lang ist, und jede zahl unter 21 als eingabe akzeptiert wird

        top = tk.Toplevel(window)
        top.geometry("{}x{}+{}+{}".format(window_width - 20, window_height - 20, x_coordinate + 10, y_coordinate + 10))
        top.resizable(False, False)
        top.title("Das große 1x1")

        def calc():
            try:
                number = int(eingabe.get())
                if(number <= 20):

                    zahlen = ""

                    for i in range(21):
                        message = "%dx%d = %d\n\n" % (number, i, (i * number))
                        zahlen += message

                    msg.showinfo("", zahlen, parent=top)

                    if (msg.askyesno("", "Willst du noch eine Reihenfolge sehen?", parent=top)):
                        eingabe.delete(0, tk.END)
                        return
                    else:
                        top.destroy()

                else:
                    msg.showerror("", "Bitte gebe eine Zahl unter 21 ein!", parent=top)

            except ValueError:
                msg.showerror("Das 1x1", "Keine gültige Nummer!", parent=top)

        title = tk.Label(top, text="Die 1x1 Maschine", font="Arial 18 normal")
        text1 = tk.Label(top, text="Tippe eine Nummer ein, um davon das große 1x1 zu \nbekommen!", anchor="e", justify=tk.LEFT, font = "Arial 10 normal")
        eingabe = Entry_int(top, width=20, foreground="black", font="Arial 12 normal")
        btn_calc = ttk.Button(top, text="Rechne!", command=calc, width=20)


        title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-40)
        text1.place(x=29, y=50)
        eingabe.place(x=29, y=92)
        btn_calc.place(x=223, y=92)

    # 1 mal 1 übungs fenster

    def ask_1mal1_üben():

        # ein toplevel fenster wird vom hauptfenster aus erstellt

        top_ask = tk.Toplevel(window)

        # hier wirds zentriert, wieder vom hauptfenster aus

        top_ask.geometry("{}x{}+{}+{}".format(window_width - 40, window_height - 40, x_coordinate + 20, y_coordinate + 20))
        top_ask.resizable(False, False)

        # labels

        title = tk.Label(top_ask, text="Willst du:", font="Arial 18 normal")

        # wieder bei command = dieses fenster wird geschlossen, und das neue fenster bei der übungsfunktion wird erstellt

        btn_groß = ttk.Button(top_ask, text="Das große 1x1 üben?", command=lambda: [top_ask.destroy(), groß_1mal1_üben()], padding=3, width=24)
        btn_klein = ttk.Button(top_ask, text="Das kleine 1x1 üben?", command=lambda: [top_ask.destroy(), klein_1mal1_üben()], padding=3, width=24)

        title.place(x=40, y=35)
        btn_klein.place(x=180, y=20)
        btn_groß.place(x=180, y=60)

    def klein_1mal1_üben():

        # fenster wird erstellt

        top = tk.Toplevel(window)
        top.geometry("{}x{}+{}+{}".format(window_width - 20, window_height - 20, x_coordinate + 10, y_coordinate + 10))
        top.resizable(False, False)

        # variablen werden mit dem "global" keyword deklariert
        # einmal die gesamt anzahl der aufgaben, und die anzahl der richtigen und falschen

        global anzahl_aufgaben
        anzahl_aufgaben = 0

        # f_aufgaben = falsche aufgaben

        global f_aufgaben
        f_aufgaben = 0

        # r_aufgaben = richtige aufgaben

        global r_aufgaben
        r_aufgaben = 0

        # calc funktion, welche vom button gerufen wird

        def calc():

            # hier wird wieder nach einem valueerror geguckt, um ungültige zahlen zu vermeiden

            try:

                # zweites toplevel vom vorherigen toplevel wird erstellt

                top2 = tk.Toplevel(top)
                top2.geometry("{}x{}+{}+{}".format(window_width + 40, window_height + 50, x_coordinate - 15, y_coordinate - 10))
                top2.resizable(False, False)

                # hier werden 10 zahlen zwischen 1 und 11 (0 und 10) random ge"sampelt"
                rand_zahlen = random.sample(range(1, 11), 10)
                # diese werden nur debugweise geprintet
                print(rand_zahlen)

                # die eingabe wird wieder in ein int konvertiert
                number = int(eingabe.get())

                if (number <= 10):

                    # eine liste namens "textentries" wird erstellt
                    textentries = list()

                    for i in range(6):
                        # in einem 6 anhaltendem loop, werden zur "textentries" liste, 6 "Entry_int" klassen hinzugefügt
                        textentries.append(Entry_int(top2, width=3, font="Arial 24 normal"))

                        # label_text zeigt die aufgabe über dem entry an (e.g. 2 * 6 = ?)
                        # hierbei wird für %d die random zahlen benutzt, und für %s die eingabe des users
                        # %d zeigt hierbei eine zahl an (als platzhalter)
                        label_text = "%d * %d = ?" % (number, rand_zahlen[i])

                        # dieser text wird dann als normales tkinter label platziert
                        label = tk.Label(top2, text=label_text, font="Arial 10 normal")
                        label.place(x=20 + 70 * i, y=46)

                        # ebenfalls werden alle textentries von i platziert
                        # i wird ebenfalls in den koordinaten erwähnt, damit sie nicht alle aufeinander gestackt sind
                        # z.b. 20 + 70 * 1, 20 + 70 * 2...
                        textentries[i].place(x=20 + 70 * i, y=76)

                    # in der funktion calc() erstelle ich nun eine neue funktion calc_numbers()
                    def calc_numbers():

                        # hier werden erstmal die globalen variablen gerufen und deklariert
                        global anzahl_aufgaben
                        global r_aufgaben
                        global f_aufgaben

                        try:
                            # ich checke hier für einen valueerror, falls ein entry leer steht, damit nicht mit einem invaliden
                            # wert multipliziert wird

                            # python mag sowas nicht anscheinend
                            for i in range(6):
                                # in einem (wie oben) 6er loop, vergleiche ich ob die eingaben der textentries, der aufgabe entsprechen
                                # i steht hierbei wieder für die aufgabe (1,2,3,4,5,6)

                                if(int(textentries[i].get()) == (int(eingabe.get()) * rand_zahlen[i])):
                                    # stimmt die lösung überein, füge ich 1 zu meiner variable "richtige aufgaben" hinzu
                                    r_aufgaben += 1

                                    # ebenfalls färbe ich dann das jeweilige textfeld grün mithilfe von einer hexfarbe
                                    # außerdem setze ich das textfeld auf den status disabled, damit man nicht nach der korrektur noch ins feld reinschreiben kann
                                    textentries[i].configure(disabledbackground="#c5ffc2", state="disabled")
                                else:
                                    # gleiche wie oben, bloß mit der variable "falsche aufgaben" und ich färbe das entry rot
                                    f_aufgaben += 1
                                    textentries[i].configure(disabledbackground="#ffc2c2", state="disabled")

                                # danach adde ich alle bearbeiteten aufgaben zu meiner "alle aufgaben insgesamt" variable hinzu
                                anzahl_aufgaben += 1

                                # wenn die korrektur betätigt wird, wird die lösung unter dem entry angezeigt
                                # ich weiß ich hätte die lösung einfach in eine variable setzen können aber ich bin zu faul dafür
                                label_text = "%d" % (int(eingabe.get()) * rand_zahlen[i])
                                label = tk.Label(top2, text=label_text, font="Arial 10 normal")
                                label.place(x=40 + 65 * i, y=126)

                                # danach setze ich die fertig taste auf "disabled" damit man nicht die ganze zeit die korrektur betätigen kann
                                btn_done.configure(state="disabled")

                        # calc_numbers() wird mit dem valueerror try-except geschlossen
                        except ValueError:
                            msg.showerror("", "Du hast nicht alle Aufgaben erledigt!", parent=top2)
                            btn_done.configure(state="enabled")

                        # dies dient nur zum debugging
                        print("Aufgaben", anzahl_aufgaben)

                    # nach der funktion calc_numbers kommt jetzt die funktion "evaluate()", wo die lösung des users evaluiert wird
                    def evaluate():
                        # ich rufe wieder die globalen variablen
                        global r_aufgaben
                        global f_aufgaben
                        global anzahl_aufgaben
                        # und setze alle in eine schöne messagebox
                        msg.showinfo("", "Gut gemacht! Hier ist deine Rückmeldung:"
                                         "\n\nVon %d Aufgaben, hattest du:"
                                         "\n\n%d richtig gelöst"
                                         "\nund %d falsch gelöst!"
                                         "\n\nDein Ergebnis beträgt: %s!"
                                         "\n\n%s"
                        % (anzahl_aufgaben, r_aufgaben, f_aufgaben, percentage(r_aufgaben, anzahl_aufgaben), evaluatestring())) # hier werden dann alle platzhalter eingesetzt


                    # selbstgeschriebe funktion, um schnell eine prozentanzahl von 2 werten zu bekommen
                    # in diesem fall: richtige aufgaben und gesamt anzahl an aufgaben
                    def percentage(richtig_aufgaben, aufgaben):
                        x = (richtig_aufgaben / aufgaben) * 100
                        return "%d%%" % x # z.b. "59%"
                        # anscheinend muss man %% schreiben, um ein % in einem string anzuzeigen lol

                    # der evaluatestring, guckt sich dann die prozentanzahl an, und gibt daraus dann eine bewertung (welche in der pdf vorgeschrieben war)
                    def evaluatestring():
                        global r_aufgaben
                        global anzahl_aufgaben

                        # prozent anzahl wird berechnet und in x eingesetzt
                        x = percentage(r_aufgaben, anzahl_aufgaben)

                        # y "strippt" x von "%" im string, und vergleicht nur die eigentliche anzahl
                        y = float(x.strip(' \t\n\r%'))

                        if(y == 100):
                            return "Das hast du ganz toll gemacht! Volle Punktzahl!"
                        elif(y > 75 and y < 100):
                            return "Toll, du hattest fast alles richtig!"
                        elif(y > 50 and y < 74):
                            return "Das war schon nicht schlecht, übe noch ein bisschen und du wirst ein Mathekönig!"
                        elif(y > 25 and y < 49):
                            return "Ein paar Aufgaben waren richtig. Übe ruhig noch ein bisschen weiter!"
                        elif(y > 10 and y < 24):
                            return "Du zeigst noch ein paar Ressourcen. Übe weiter oder lass dir die Malfolge nochmal anzeigen!"
                        elif(y > 9 and y < 1):
                            return "Hier besteht noch Nachholbedarf. Versuche es doch nochmal!"
                        elif(y == 0):
                            return "Leider war keine Aufgabe richtig. Du solltest noch ein bisschen üben!"
                        else: 0

                    # labels für das übungs fenster

                    title = tk.Label(top2, text="Übung - kleines 1x1", font="Arial 18 normal")
                    title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-74)

                    anzahl_aufgaben_text = "Bearbeitete Aufgaben: %d" % anzahl_aufgaben
                    anzahl_aufgaben_label = tk.Label(top2, text=anzahl_aufgaben_text, font="Arial 8 normal", foreground="#b0b0b0")
                    anzahl_aufgaben_label.place(x=297, y = 146)

                    btn_done = ttk.Button(top2, text="Fertig", width=20, command = calc_numbers, padding=4)
                    btn_done.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=80, x=-140)

                    btn_other = ttk.Button(top2, text="Weitere Aufgaben", width=20, command=lambda:(top2.destroy(), calc()), padding=4)
                    btn_other.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=80, x=0)

                    btn_exit = ttk.Button(top2, text="Rückmeldung", width=20, command=lambda: (top2.destroy(), evaluate()), padding=4)
                    btn_exit.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=80, x=140)

                else:
                    top2.destroy()
                    msg.showerror("", "Bitte gebe eine Zahl unter 11 ein!", parent=top)
            except ValueError:
                top2.destroy()
                msg.showerror("Das 1x1", "Keine gültige Nummer!", parent=top)

        # labels für das eingabe fenster

        title = tk.Label(top, text="Die 1x1 Maschine", font="Arial 18 normal")
        label1 = tk.Label(top, text="Tippe eine Nummer ein, um davon das 1x1 zu üben!", anchor="e", justify=tk.LEFT, font="Arial 10 normal")
        eingabe = Entry_int(top, width=20, foreground="black", font="Arial 12 normal")

        btn_calc = ttk.Button(top, text="Rechne!", width=20, command=calc)

        title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-40)
        label1.place(x=29, y=50)
        eingabe.place(x=29, y=92)
        btn_calc.place(x=223, y=92)

    def groß_1mal1_üben():

        # die funktion ist literally das selbe wie die andere, aber hierbei wird das große 1x1 verwendet
        # unterschied:

        # line 429: 10 zahlen zwischen 0 und 20, nicht 0 und 10
        # line 434: alle zahlen unter 21, nicht 11

        top = tk.Toplevel(window)
        top.geometry("{}x{}+{}+{}".format(window_width - 20, window_height - 20, x_coordinate + 10, y_coordinate + 10))
        top.resizable(False, False)

        global anzahl_aufgaben
        anzahl_aufgaben = 0

        global f_aufgaben
        f_aufgaben = 0

        global r_aufgaben
        r_aufgaben = 0

        def calc():
            try:
                top2 = tk.Toplevel(top)
                top2.geometry("{}x{}+{}+{}".format(window_width + 40, window_height + 50, x_coordinate - 15, y_coordinate - 10))
                top2.resizable(False, False)

                rand_zahlen = random.sample(range(1, 21), 10)
                print(rand_zahlen)

                number = int(eingabe.get())

                if (number <= 20):

                    textentries = list()

                    for i in range(6):
                        textentries.append(Entry_int(top2, width=3, font="Arial 24 normal"))

                        label_text = "%s * %d = ?" % (eingabe.get(), rand_zahlen[i])
                        label = tk.Label(top2, text=label_text, font="Arial 10 normal")
                        label.place(x=20 + 70 * i, y=46)

                        textentries[i].place(x=20 + 70 * i, y=76)

                    def calc_numbers():

                        global anzahl_aufgaben
                        global f_aufgaben
                        global r_aufgaben

                        try:
                            for i in range(6):
                                print(int(eingabe.get()) * rand_zahlen[i])

                                if(int(textentries[i].get()) == (int(eingabe.get()) * rand_zahlen[i])):
                                    r_aufgaben += 1
                                    textentries[i].configure(disabledbackground="#c5ffc2", state="disabled")
                                else:
                                    f_aufgaben += 1
                                    textentries[i].configure(disabledbackground="#ffc2c2", state="disabled")

                                anzahl_aufgaben += 1

                                label_text = "%d" % (int(eingabe.get()) * rand_zahlen[i])
                                label = tk.Label(top2, text=label_text, font="Arial 10 normal")
                                label.place(x=35 + 70 * i, y=126)

                                btn_done.configure(state="disabled")
                        except ValueError:
                            msg.showerror("", "Du hast nicht alle Aufgaben erledigt!", parent=top2)
                            btn_done.configure(state="enabled")

                        print("Aufgaben", anzahl_aufgaben)

                    def evaluate():
                        global r_aufgaben
                        global f_aufgaben
                        global anzahl_aufgaben
                        msg.showinfo("", "Gut gemacht! Hier ist deine Rückmeldung:\n\nVon %d Aufgaben, hattest du:\n\n%d richtig gelöst\nund %d falsch gelöst!\n\nDein Ergebnis beträgt: %s!\n\n%s" % (anzahl_aufgaben, r_aufgaben, f_aufgaben, percentage(r_aufgaben, anzahl_aufgaben), evaluatestring()))

                    def percentage(richtig_aufgaben, aufgaben):
                        x = (richtig_aufgaben / aufgaben) * 100
                        return "%d%%" % x

                    def evaluatestring():
                        global r_aufgaben
                        global anzahl_aufgaben
                        x = percentage(r_aufgaben, anzahl_aufgaben)
                        y = float(x.strip(' \t\n\r%'))

                        if(y == 100):
                            return "Das hast du ganz toll gemacht! Volle Punktzahl!"
                        elif(y > 75 and y < 100):
                            return "Toll, du hattest fast alles richtig!"
                        elif(y > 50 and y < 74):
                            return "Das war schon nicht schlecht, übe noch ein bisschen und du wirst ein Mathekönig!"
                        elif(y > 25 and y < 49):
                            return "Ein paar Aufgaben waren richtig. Übe ruhig noch ein bisschen weiter!"
                        elif(y > 10 and y < 24):
                            return "Du zeigst noch ein paar Ressourcen. Übe weiter oder lass dir die Malfolge nochmal anzeigen!"
                        elif(y > 9 and y < 1):
                            return "Hier besteht noch Nachholbedarf. Versuche es doch nochmal!"
                        elif(y == 0):
                            return "Leider war keine Aufgabe richtig. Du solltest noch ein bisschen üben!"
                        else: 0

                    title = tk.Label(top2, text="Übung - großes 1x1", font="Arial 18 normal")
                    title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-74)

                    anzahl_aufgaben_text = "Bearbeitete Aufgaben: %d" % anzahl_aufgaben
                    anzahl_aufgaben_label = tk.Label(top2, text=anzahl_aufgaben_text, font="Arial 8 normal", foreground="#b0b0b0")
                    anzahl_aufgaben_label.place(x=297, y = 146)

                    btn_done = ttk.Button(top2, text="Fertig", width=20, command = calc_numbers, padding=4)
                    btn_done.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=80, x=-140)

                    btn_other = ttk.Button(top2, text="Weitere Aufgaben", width=20, command=lambda:(top2.destroy(), calc()), padding=4)
                    btn_other.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=80, x=0)

                    btn_exit = ttk.Button(top2, text="Rückmeldung", width=20, command=lambda: (top2.destroy(), evaluate()), padding=4)
                    btn_exit.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=80, x=140)

                else:
                    top2.destroy()
                    msg.showerror("", "Bitte gebe eine Zahl unter 21 ein!", parent=top)
            except ValueError:
                top2.destroy()
                msg.showerror("Das 1x1", "Keine gültige Nummer!", parent=top)

        title = tk.Label(top, text="Die 1x1 Maschine", font="Arial 18 normal")
        label1 = tk.Label(top, text="Tippe eine Nummer ein, um davon das 1x1 zu üben!", anchor="e", justify=tk.LEFT, font="Arial 10 normal")
        eingabe = Entry_int(top, width=20, foreground="black", font="Arial 12 normal")

        btn_calc = ttk.Button(top, text="Rechne!", width=20, command=calc)

        title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-40)
        label1.place(x=29, y=50)
        eingabe.place(x=29, y=92)
        btn_calc.place(x=223, y=92)

    # ------------ HAUPTFENSTER WIDGETS -------------------

    # labels

    title = tk.Label(window, text="Das 1 mal 1 - Übungscenter", font=("Arial", "22", "normal"))

    # buttons

    btn_print = ttk.Button(window, text="1x1 Anzeigen", width=40, padding=4, command=ask_1mal1_anzeigen)
    btn_practice = ttk.Button(window, text="1x1 Übungen", width=40, padding=4, command=ask_1mal1_üben)

    title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-50)
    btn_print.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-5)
    btn_practice.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=35)
    window.mainloop()

# ein von stackoverflow modifizierte klasse, welche nur zahlen ins entry erlaubt

class Entry_int(tk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar(master)
        self.var.trace('w', self.validate)
        tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.get, self.set = self.var.get, self.var.set
    def validate(self, *args):
        value = self.get()
        if not value.isdigit():
            self.set(''.join(x for x in value if x.isdigit()))


# anzeige, dass das script manuell gestartet werden kann
if __name__ == '__main__':
    main()
