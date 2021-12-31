import tkinter as tk
import random
from tkinter import messagebox
import numpy as np
from Archimedes import Archimedes
import gates
from ArcGUI import ArcGUI

start = tk.Tk()
start.geometry("600x250")
start.title("Q4Q Tool")


def run_arc():
    window = tk.Toplevel(start)
    # window.geometry("600x250")
    arcBut["state"] = "disabled"
    win = ArcGUI(window)
    start.iconify()

    def close():
        window.destroy()
        arcBut["state"] = "normal"
        start.deiconify()

    window.protocol("WM_DELETE_WINDOW", close)
    window.mainloop()
    return


def run_ent():
    window = tk.Toplevel(start)
    entBut["state"] = "disabled"


    def close():
        window.destroy()
        entBut["state"] = "normal"
        start.deiconify()

    window.protocol("WM_DELETE_WINDOW", close)
    window.mainloop()
    return


def run_instr():
    messagebox.showinfo("More Info", "This is Archimedes problem proposed in Q is for Quantum by Terry Rudolph \n in "
                                     "this program you can choose a location of a gold bar and \n it will test if it "
                                     "is real or fake.")
    return


title = tk.Frame(start, height=50)
title.pack(fill=tk.BOTH, expand=True)
title.grid_rowconfigure([0, 2], weight=1)
title.grid_columnconfigure([0, 2], weight=1, minsize=100)

menu = tk.Frame(start, height=200)
menu.pack(fill=tk.BOTH, expand=True)
menu.grid_rowconfigure([1, 2, 3], weight=1)
menu.grid_columnconfigure([0, 2], weight=1, minsize=100)

QfQ = tk.Label(title, text="Q is for Quantum", font="somethingrandom")
arcBut = tk.Button(menu, text="Archimedes Gold", command=run_arc)
entBut = tk.Button(menu, text="Psychic Entanglement", command=run_ent)
instrBut = tk.Button(menu, text="help", command=run_instr)

QfQ.grid(row=1, column=1, pady=10)
arcBut.grid(row=1, column=1, pady=5)
entBut.grid(row=2, column=1, pady=5)
instrBut.grid(row=3, column=1, pady=5)

menu.mainloop()
