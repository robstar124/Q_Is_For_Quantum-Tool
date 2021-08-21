#this is where gates will be stored and constructed where necessary

import numpy as np

Zero_VECTOR = np.array([1, 0])
One_VECTOR = np.array([0, 1])
hadamard = np.matrix([[1, 1], [1, -1]])

def n_hadamard(n): #n will be a power of 2, will build a nxn hadamard gate
    solution = hadamard
    for i in range(0, int(np.log2(n)) - 1):
        solution = np.kron(hadamard, solution)

    return solution

def state_vector(state):
    pass



print(n_hadamard(8))