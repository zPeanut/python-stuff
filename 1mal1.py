# created by peanut on the 20th sep 2021
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

import random
import time

def main():

    # ---------------- HAUPTFENSTER SETUP ---------------------

    window = tk.Tk()
    window.resizable(False, False)
    window.title("Das 1x1")
    img = tk.PhotoImage(file="resources/hydrogen20.png")
    window.tk.call('wm', 'iconphoto', window._w, img)

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
        top_ask = tk.Toplevel(window)
        top_ask.geometry("{}x{}+{}+{}".format(window_width - 40, window_height - 40, x_coordinate + 20, y_coordinate + 20))
        top_ask.resizable(False, False)

        title = tk.Label(top_ask, text="Soll ich:", font="Arial 18 normal")
        btn_groß = ttk.Button(top_ask, text="Das große 1x1 anzeigen?", command=lambda: [top_ask.destroy(), große_1mal1_anzeigen()], padding=3)
        btn_klein = ttk.Button(top_ask, text="Das kleine 1x1 anzeigen?", command=lambda: [top_ask.destroy(), klein_1mal1_anzeigen()], padding=3)

        title.place(x=40, y=35)
        btn_klein.place(x=180, y=20)
        btn_groß.place(x=180, y=60)

    def klein_1mal1_anzeigen():
        top = tk.Toplevel(window)
        top.geometry("{}x{}+{}+{}".format(window_width - 20, window_height - 20, x_coordinate + 10, y_coordinate + 10))
        top.resizable(False, False)
        top.title("Das kleine 1x1")

        def calc():
            try:
                number = int(eingabe.get())
                if (number <= 10):

                    zahlen = ""

                    for i in range(11):
                        message = "%dx%d = %d\n\n" % (number, i, (i * number))
                        zahlen += message

                    msg.showinfo("", zahlen, parent=top)

                    if(msg.askyesno("", "Willst du noch eine Reihenfolge sehen?", parent=top)):
                        eingabe.delete(0, tk.END)
                        return
                    else:
                        top.destroy()

                else:
                    msg.showerror("", "Bitte gebe eine Zahl unter 11 ein!", parent=top)
            except ValueError:
                msg.showerror("Das 1x1", "Keine gültige Nummer!", parent=top)

        title = tk.Label(top, text="Die 1x1 Maschine", font="Arial 18 normal")
        text1 = tk.Label(top, text="Tippe eine Nummer ein, um davon das kleine 1x1 zu \nbekommen!", anchor="e", justify=tk.LEFT, font = "Arial 10 normal")
        eingabe = Entry_int(top, width=20, foreground="black", font="Arial 12 normal")
        btn_calc = ttk.Button(top, text="Rechne!", command=calc, width=20)

        title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-40)
        text1.place(x=29, y=50)
        eingabe.place(x=29, y=92)
        btn_calc.place(x=223, y=92)

    def große_1mal1_anzeigen():
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

    # 1 mal 1 üben

    def ask_1mal1_üben():
        top_ask = tk.Toplevel(window)
        top_ask.geometry("{}x{}+{}+{}".format(window_width - 40, window_height - 40, x_coordinate + 20, y_coordinate + 20))
        top_ask.resizable(False, False)

        title = tk.Label(top_ask, text="Willst du:", font="Arial 18 normal")
        btn_groß = ttk.Button(top_ask, text="Das große 1x1 üben?", command=lambda: [top_ask.destroy()], padding=3, width=24)
        btn_klein = ttk.Button(top_ask, text="Das kleine 1x1 üben?", command=lambda: [top_ask.destroy(), klein_1mal1_üben()], padding=3, width=24)

        title.place(x=40, y=35)
        btn_klein.place(x=180, y=20)
        btn_groß.place(x=180, y=60)

    def klein_1mal1_üben():
        top = tk.Toplevel(window)
        top.geometry("{}x{}+{}+{}".format(window_width - 20, window_height - 20, x_coordinate + 10, y_coordinate + 10))
        top.resizable(False, False)

        rand_zahlen = random.sample(range(1, 11), 10)
        print(rand_zahlen)

        def calc():
            try:
                top2 = tk.Toplevel(top)
                top2.geometry("{}x{}+{}+{}".format(window_width + 40, window_height + 40, x_coordinate - 15, y_coordinate - 10))
                top2.resizable(False, False)

                number = int(eingabe.get())

                if (number <= 10):

                    textentries = list()

                    for i in range(6):
                        textentries.append(Entry_int(top2, width=2, font="Arial 28 bold"))

                        label_text = "%s * %d = ?" % (eingabe.get(), rand_zahlen[i])
                        label = tk.Label(top2, text=label_text, font="Arial 10 normal")
                        label.place(x=35 + 65 * i, y=46)

                        textentries[i].place(x=35 + 65 * i, y=76)

                    def calc_numbers():

                        anzahl_richtig = 0
                        anzahl_falsch = 0

                        for i in range(6):

                            print(int(eingabe.get()) * rand_zahlen[i])

                            if(int(textentries[i].get()) == (int(eingabe.get()) * rand_zahlen[i])):
                                anzahl_richtig += 1
                                textentries[i].configure(background="#c5ffc2")
                            else:
                                anzahl_falsch += 1
                                textentries[i].configure(background="#ffc2c2")


                        msg.showinfo("", "Von 6 Aufgaben aus dem kleinem 1x1 mit der Zahl %s, hattest du:\n\n%d Aufgaben richtig\n\nund %d Aufgaben falsch!" % (eingabe.get(), anzahl_richtig, anzahl_falsch), parent=top2)

                    title = tk.Label(top2, text="Übung - kleines 1x1", font="Arial 18 normal")
                    title.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-74)

                    btn_done = ttk.Button(top2, text="Fertig", width=20, command = calc_numbers, padding=4)
                    btn_done.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=64)
                else:
                    top2.destroy()
                    msg.showerror("", "Bitte gebe eine Zahl unter 11 ein!", parent=top)
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

# stackoverflow, int entry template

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

if __name__ == '__main__':
    main()