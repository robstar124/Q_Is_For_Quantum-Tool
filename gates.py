# this is where gates will be stored and constructed where necessary

import numpy as np

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
    joint = 0

    if state[0] == 1:
        joint = ONE_VECTOR
    elif state[0] == 0:
        joint = ZERO_VECTOR

    for i in range(0, len(state) - 1):
        if state[i] == 0:
            joint = np.kron(joint, ZERO_VECTOR)

        elif state[i] == 1:
            joint = np.kron(joint, ONE_VECTOR)

    return joint


# print(n_hadamard(8))
print(state_vector([1, 0, 0]))
