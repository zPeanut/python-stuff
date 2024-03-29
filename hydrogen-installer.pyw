# made by peanut
# created on 7th sep 2021
from tkinter import Label, Entry, Tk, CENTER, LEFT, END, StringVar, PhotoImage, Checkbutton, BooleanVar
from tkinter import filedialog as fd
from tkinter import messagebox as msg
import tkinter.ttk as ttk

import os
import requests
import urllib.request
import urllib
import webbrowser

global cwd
appdata = os.getenv('APPDATA') + "\.minecraft"
cwd = appdata + "\mods"
verfolder = appdata + "\\versions\\"
versionstring = "v1.3 (02.01.2022)"

def callback(url):
    webbrowser.open_new(url)

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)  # Python 3.x
        return True
    except:
        return False

print('connected' if connect() else 'no internet!')

def main():
    # check for internet connection, if no: exit program
    if (connect()):
        window()
    else:
        nointernet()


    # download (inside tkinter mainloop)

def download(url: str, dest_folder: str):

    # get hydrogen jar from web

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    if not os.path.exists(("%s\%s" % (dest_folder, filename))):
        r = requests.get(url, stream=True)
        if r.ok:
            print("Saving %s to %s." % (filename, os.path.abspath(file_path)))
            with open(file_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024 * 8):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                        os.fsync(f.fileno())
            success()
        else:  # HTTP status code 4XX/5XX
            global errormessage
            errormessage = ("Download failed: status code {}\n{}".format(r.status_code, r.text))
            print(errormessage)
            error()
    else:
        duplicate()

def downloadfile():

        # download hydrogen jar
        global version
        version = dropdown.get()

        if any(x.startswith('1.8.9-forge') for x in os.listdir(verfolder)):
            print("Forge directory exists!")
            if (version == "1.0" or version == "1.1"):
                download(("https://github.com/zPeanut/Hydrogen/releases/download/%s/phosphor-%s.jar" % (version, version)), dest_folder=cwd)
            else:
                # download file from github
                download(("https://github.com/zPeanut/Hydrogen/releases/download/%s/hydrogen-%s.jar" % (version, version)), dest_folder=cwd)
        else:
            print("Forge directory was not found!")
            noforge()


def window():
    # setup window

    window = Tk()
    window.resizable(False, False)
    window.title("Hydrogen Installer")

    # centre window and set size

    window_height = 210
    window_width = 400
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

    # labels

    title = Label(window, text="Hydrogen Client", font="Arial 18 bold")
    subtitle = Label(window, text="for Minecraft 1.8.9", justify=CENTER, font="Arial 11 bold")
    desc1 = "This application will install Hydrogen into your mods\nfolder located inside your Minecraft folder.\n"
    description = Label(window, text=desc1, justify=LEFT, font="Arial 10")
    folder_string = Label(window, text="Directory:", font="Arial 10")
    versionchoose_string = Label(window, text="Version:", font="Arial 10")
    version_string = Label(window, text=versionstring, foreground="gray", font="Arial 8")
    githubview = Label(window, text="view on GitHub", fg="blue", cursor="hand2")
    githubview.bind("<Button-1>", lambda e: callback("https://github.com/zPeanut/Hydrogen/releases/tag/%s" % dropdown.get()))

    # buttons

    btn_install = ttk.Button(window, text="Install", width=20, command=downloadfile)
    btn_path = ttk.Button(window, text="...", width=2, command=directoryopen)
    btn_cancel = ttk.Button(window, text="Cancel", width=20, command=close)

    # dropdown

    VERSIONS = []

    url = "https://raw.githubusercontent.com/zPeanut/Resources/master/versions-hydrogen"
    page = requests.get(url)
    versions = (page.text).strip()

    splitstr = versions.split("\n")

    for i in splitstr:
        VERSIONS.append(i)

    variable = StringVar(window)
    variable.set(VERSIONS[1])

    global dropdown
    dropdown = ttk.Combobox(window, values=VERSIONS, width=7)
    dropdown.configure(state="readonly")
    dropdown.current(0)

    # setup directory entry

    global directory
    directory = Entry(width=44, foreground="black")
    path = directory.get()
    directory.insert(0, cwd)

    # place all widgets on window

    version_string.place(x=1, y=1)
    title.place(x=102, y=10)
    subtitle.place(x=130, y=42)
    description.place(x=20, y=70)

    directory.place(x=84, y=115)
    folder_string.place(x=20, y=113)
    btn_path.place(x=355, y=112)

    dropdown.place(x=84, y=140)
    versionchoose_string.place(x=20, y=139)
    githubview.place(x=150, y=140)

    btn_install.place(x=20, y=170)
    btn_cancel.place(x=248, y=170)

    window.mainloop()



def directoryopen():
    # open directory window

    dir_name = fd.askdirectory()
    global cwd
    cwd = dir_name
    directory.delete(0, END)
    directory.insert(0, cwd)

def success():
    msg.showinfo("Hydrogen Installer", "Successfully Installed!")


def duplicate():
    msg.showerror("Hydrogen Installer", "Hydrogen is already installed!")


def noforge():
    msg.showerror("Hydrogen Installer", "Forge is not installed! Please install forge before continuing.")

def nolauncher():
    msg.showerror("Hydrogen Installer", "Minecraft Launcher Profiles were not found.\nIs the Minecraft launcher correctly installed?")

def nointernet():
    root = Tk()
    root.withdraw()
    msg.showerror("Hydrogen Installer", "Could not connect to the internet!\nAn active internet connection is required for the installation.")

def error():
    global errormessage
    msg.showerror("Hydrogen Installer", errormessage)

def close():
    exit()

if __name__ == '__main__':
    main()
