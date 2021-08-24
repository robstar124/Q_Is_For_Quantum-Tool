# this is where gates will be stored and constructed where necessary

import numpy as np

IDENTITY = np.matrix([[1, 0], [0, 1]])
ZERO_VECTOR = np.array([1, 0])
ONE_VECTOR = np.array([0, 1])
HADAMARD = np.matrix([[1, 1], [1, -1]])
PAULI_X = np.matrix([[0, 1], [1, 0]])


def n_hadamard(n):  # n will be a power of 2, will build a nxn hadamard gate
    solution = HADAMARD
    for i in range(0, int(np.log2(n)) - 1):
        solution = np.kron(HADAMARD, solution)

    return solution


def state_vector(state):  # create the state vector from a list
    joint = None

    if state[0] == 1:
        joint = ONE_VECTOR
    elif state[0] == 0:
        joint = ZERO_VECTOR

    for i in range(0, len(state) - 1):
        if state[i+1] == 0:
            joint = np.kron(joint, ZERO_VECTOR)

        elif state[i+1] == 1:
            joint = np.kron(joint, ONE_VECTOR)

    return joint

def Teffoli(size, control1, control2, target):
    matrix = []

    for i in range(0, 2 ** size):
        binary = np.binary_repr(i, size)
        binary = list(binary)
        if binary[control1 - 1] == "1" and binary[control2 - 1] == "1":
            if binary[target - 1] == "1":
                binary[target - 1] = "0"
            else:
                binary[target - 1] = "1"

        num = ""
        for i in binary:
            num += i

        number = int(num, 2)

        partial = np.zeros(2 ** size)
        partial[number] = 1
        matrix.append(partial)
    matrix = np.array(matrix)
    return matrix

