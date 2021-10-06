import tkinter as tk
import random
from tkinter import messagebox
import numpy as np
import Archimedes

root = tk.Tk()
is_quantum = False

def generate_locations():
    for num in range(0, 4):
        foo = np.binary_repr(random.getrandbits(3), 3)
        print(foo)

def reset():
    r1.deselect()

def fakeBars():
    return bool(random.getrandbits(1))

def run():
    global position
    global q_var
    test = position.get()
    fake = fakeBars()
    # result = Archimedes.main()
    try:
        int(test)
        if 0 <= int(test) <= 7:
            if i.get() == 1:
                messagebox.showinfo("quantum")
            else:
                messagebox.showinfo("not quantum")
        else:
            messagebox.showerror("Wrong input", "integers between 0 and 7 accepted only")

    except ValueError:
        messagebox.showerror("Wrong input", "integers between 0 and 7 accepted only")


text = tk.Label(root,
                text="This is Archimedes problem proposed in Q is for Quantum by Terry Rudolph \n in this program you can" \
                     "choose a location of a gold bar and \n it will test if it is real or fake.").grid(row=0)

i = tk.IntVar()

r1 = tk.Radiobutton(root, text="quantum", value=1, variable = i)
r1.grid(row = 1)

reset_button = tk.Button(root, text = "reset", command = reset())
reset_button.grid(row = 0, column  = 1)





run_button = tk.Button(root, text="run", command=run)
run_button.grid(row=1, column=1)

position_label = tk.Label(root, text="enter test positon").grid(row=2)
position = tk.Entry(root)
position.grid(row=2, column=1)

generate_locations()
#root.mainloop()
