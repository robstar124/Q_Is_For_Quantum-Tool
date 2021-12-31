import tkinter as tk
from tkinter import messagebox
import gates
import numpy as np
import random
from PIL import Image, ImageTk

from Archimedes import Archimedes


def fakeBars():
    p = np.random.random()
    if p < 0.5:
        return True
    else:
        return False


def generate_locations():
    locations = []
    while len(locations) != 4:
        foo = np.binary_repr(random.getrandbits(3), 3)
        foo = foo + "1"
        foo = foo + "0"

        if foo in locations:
            continue
        else:
            locations.append(foo)

    return locations


class ArcGUI(tk.Frame):
    def __init__(self, master=None):
        self.quantum = False
        self.input_bits = [0, 0, 0, 0, 0]
        self.output_bits = [0, 0, 0, 0, 0]
        self.outputSame = False
        self.locations = generate_locations()
        self.fake = fakeBars()  # fakeBars()

        super().__init__(master)
        self.master = master
        self.frameR = tk.Frame(self.master, width=600, bg="white")
        self.frameL = tk.Frame(self.master)

        self.create_frames()
        self.pack()
        self.create_widgets()

    def create_frames(self):
        self.frameL.pack(side="left", expand=True, fill=tk.BOTH)
        self.frameL.grid_rowconfigure([1, 6], weight=1, minsize=30)
        self.frameL.grid_columnconfigure([0, 2], weight=1, minsize=50)

        self.frameR.pack(side="right", expand=True, fill=tk.BOTH)
        self.frameR.grid_rowconfigure([0, 4], weight=1, minsize=70)
        self.frameR.grid_columnconfigure([0, 5], weight=1, minsize=150)

    def create_widgets(self):
        # Left Frame
        self.title = tk.Label(self.frameL, text="Gold Bars Vault", font="somethingrandom")
        self.qButton = tk.Button(self.frameL, text="Add Hadamards", command=self.change_Hs, relief="raised")
        self.help = tk.Button(self.frameL, text="Help", command=self.info)
        self.cheatBut = tk.Button(self.frameL, text="Cheat", command=self.cheat)
        self.changeVault = tk.Button(self.frameL, text="Change Vault Type", command=self.changeVaultType)


        self.title.grid(row=0, column=1, pady=20)
        self.qButton.grid(row=2, column=1, pady=5)
        self.help.grid(row=3, column=1, pady=5)
        self.cheatBut.grid(row=4, column=1, pady=5)
        self.changeVault.grid(row=5, column=1, pady=5)

        # Right Frame
        self.locbuts = []
        for i in range(4):
            num = i
            a = tk.Button(self.frameR, text="0")
            self.locbuts.append(a)

        self.locbuts[0]["command"] = (lambda: self.location_buttons(0))
        self.locbuts[1]["command"] = (lambda: self.location_buttons(1))
        self.locbuts[2]["command"] = (lambda: self.location_buttons(2))
        self.locbuts[3]["command"] = (lambda: self.location_buttons(3))

        self.locbuts[0].grid(row=1, column=1, padx=10, pady=10, ipadx=5)
        self.locbuts[1].grid(row=1, column=2, padx=10, pady=10, ipadx=5)
        self.locbuts[2].grid(row=1, column=3, padx=10, pady=10, ipadx=5)
        self.locbuts[3].grid(row=1, column=4, padx=10, pady=10, ipadx=5)

        load1 = Image.open("Classic Archimedes.png")
        load2 = Image.open("Quantum Archimedes.png")
        self.render1 = ImageTk.PhotoImage(load1)
        self.render2 = ImageTk.PhotoImage(load2)

        self.img = tk.Label(self.frameR, image=self.render1)
        self.img.image = self.render1
        self.img.grid(row=2, column=1, columnspan=4, pady=5)

        self.observe = tk.Button(self.frameR, text="Observe", command=self.run)
        self.observe.grid(row=4, column=5)

    def change_Hs(self):
        if self.quantum:
            self.img["image"] = self.render1
            self.img.image = self.render1
            self.img.grid(row=2, column=1, columnspan=4, pady=5)

            self.quantum = False
            self.qButton["text"] = "Add Hadamards"
            self.qButton["relief"] = "raised"

        else:
            self.img["image"] = self.render2
            self.img.image = self.render2
            self.img.grid(row=2, column=1, columnspan=4, pady=5)

            self.quantum = True
            self.qButton["text"] = "Remove Hadamards"
            self.qButton["relief"] = "sunken"

    def location_buttons(self, i):
        if self.input_bits[i]:
            self.input_bits[i] = 0
            self.locbuts[i]["text"] = "0"
            self.locbuts[i]["relief"] = "raised"
        else:
            self.input_bits[i] = 1
            self.locbuts[i]["text"] = "1"
            self.locbuts[i]["relief"] = "sunken"

    def info(self):
        # TODO: messagebox giving instructions and context
        messagebox.showerror("So how does this work?", "Read Terry's book")
        return

    def run(self):

        vect = gates.state_vector(self.input_bits)
        arc = Archimedes(vect, self.locations, self.fake, classic=(not self.quantum))
        self.output_bits = arc.readOutput()

        self.outlabel1 = tk.Label(self.frameR, text=str(self.output_bits[0]))
        self.outlabel2 = tk.Label(self.frameR, text=str(self.output_bits[1]))
        self.outlabel3 = tk.Label(self.frameR, text=str(self.output_bits[2]))
        self.outlabel4 = tk.Label(self.frameR, text=str(self.output_bits[3]))

        self.outlabel1.grid(row=3, column=1, padx=10, pady=10, ipadx=5)
        self.outlabel2.grid(row=3, column=2, padx=10, pady=10, ipadx=5)
        self.outlabel3.grid(row=3, column=3, padx=10, pady=10, ipadx=5)
        self.outlabel4.grid(row=3, column=4, padx=10, pady=10, ipadx=5)

    def cheat(self):
        locations = [x[:-2] for x in self.locations]
        if self.fake:
            messagebox.showinfo("Cheating are we??", "We're in a phony vault, every bar in here is fake. There are no "
                                                     "real bars. Theres no time to waste. ITS ALL FAKE!")
        else:
            messagebox.showinfo("Cheating are we??", f"We're in a vault with real gold bars!!! \nThe locations of the "
                                                     f"real bars are: {locations}")
        return

    def changeVaultType(self):
        self.fake = not self.fake
        print(self.fake)
        return

