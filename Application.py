import tkinter as tk
import random
from tkinter import messagebox
import numpy as np
from Archimedes import Archimedes
import gates

root = tk.Tk()
is_quantum = False


def generate_locations():
    locations = []
    for num in range(0, 4):
        foo = np.binary_repr(random.getrandbits(3), 3)
        foo = foo + "1"
        foo = foo + "0"
        locations.append(foo)
    print(locations)
    return locations


def fakeBars():
    p = np.random.random()
    if p < 0.5:
        return True
    else:
        return False


def run():
    global position
    test = position.get()

    if 0 <= int(test) <= 7:
        initial_state = np.binary_repr(int(test), 3)
        initial_state = initial_state + "1"
        initial_state = initial_state + "0"
        if get_results(initial_state):
            messagebox.showinfo("Great Success", "There are real gold bars")
        else:
            messagebox.showinfo("Great Failure", "There are no real gold bars")
    else:
        messagebox.showerror("Wrong input", "integers between 0 and 7 accepted only")


def get_results(initial_state):
    fake = fakeBars()
    locations = generate_locations()
    print(fake)
    print(position)
    x = list(map(int, initial_state))
    vect = gates.state_vector(x)
    arc = Archimedes(vect, locations, fake)
    results = arc.readOutput()
    if results == x:
        return False
    else:
        return True


text = tk.Label(root,
                text="This is Archimedes problem proposed in Q is for Quantum by Terry Rudolph \n in this program you can" \
                     "choose a location of a gold bar and \n it will test if it is real or fake.").grid(row=0)

run_button = tk.Button(root, text="run", command=run)
run_button.grid(row=1, column=1)

position_label = tk.Label(root, text="enter test positon").grid(row=2)
position = tk.Entry(root)
position.grid(row=2, column=1)

root.mainloop()
