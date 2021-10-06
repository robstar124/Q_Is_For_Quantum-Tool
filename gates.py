# this is where gates will be stored and constructed where necessary
import math

import numpy as np

IDENTITY = np.array([[1, 0], [0, 1]])
ZERO_VECTOR = np.array([1, 0])
ONE_VECTOR = np.array([0, 1])
HADAMARD = np.array([[1, 1], [1, -1]])
PAULI_X = np.array([[0, 1], [1, 0]])


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
        if state[i + 1] == 0:
            joint = np.kron(joint, ZERO_VECTOR)

        elif state[i + 1] == 1:
            joint = np.kron(joint, ONE_VECTOR)

    return joint


def Teffoli(size, control1, control2, target):  # Teffoli gates with controls and targets
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
        for j in binary:
            num += j

        number = int(num, 2)

        partial = np.zeros(2 ** size)
        partial[number] = 1
        matrix.append(partial)
    matrix = np.array(matrix)
    return matrix


def CCCNOT(control1, control2, control3, target, aux):  # assume qubit 5 is aux

    gate1 = Teffoli(5, control1, control2, aux)
    gate2 = Teffoli(5, control3, aux, target)

    return np.matmul(np.matmul(gate1, gate2), gate1)


def NOT(size, targets):  # creates not gates targeting specific qubits
    matrix = np.identity(1)
    for i in range(0, size):
        if (i + 1) not in targets:
            matrix = np.kron(matrix, np.identity(2))
        else:
            matrix = np.kron(matrix, PAULI_X)

    return matrix


def hadamard(size, targets):  # creates hadamard which targets specific qubits

    matrix = np.identity(1)

    for i in range(0, size):

        if (i + 1) not in targets:
            matrix = np.kron(matrix, np.identity(2))

        else:
            matrix = np.kron(matrix, HADAMARD)

    return matrix


def probabilities(dens, targetBit):  # helper for measure(), calculates probability of each basis of a pair
    measurement = ONE_VECTOR
    return measurement


def measureOperator(nQbits, target, measurement):   # calculates the measurement operator and its transpose
    measurement = [measurement]
    mBra = np.identity(1)
    mKet = np.identity(1)

    for i in range(0, nQbits):
        if (i + 1) != target:
            mBra = np.kron(np.identity(2), mBra)
            mKet = np.kron(np.identity(2), mKet)

        else:
            mBra = np.kron(measurement, mBra)
            mKet = np.kron(np.transpose(measurement), mKet)

    return mBra, mKet


def measure(densityM, target):  # Returns a reduced circuit after the target qubit is measured
    try:
        dim = np.shape(densityM)
        assert (dim[0] == dim[1])
    except AssertionError:
        print("Density Matrix is not Square")
        raise

    chosenBasis = probabilities(densityM, target)
    bra, ket = measureOperator(int(math.log2(dim[0])), target, chosenBasis)

    matrix = np.matmul(densityM, ket)
    matrix = np.matmul(bra, matrix)
    return matrix


def density(stateVec):  # creates density matrix
    return np.outer(stateVec, stateVec)
