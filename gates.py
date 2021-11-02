# this is where gates will be stored and constructed where necessary
import math

import numpy as np

IDENTITY = np.array([[1, 0], [0, 1]])
ZERO_VECTOR = np.array([1, 0])
ONE_VECTOR = np.array([0, 1])
HADAMARD = (1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]])
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


def measureChoose(zero, one):  # chooses between the two states the measured qubit could be
    err = 0.0000000001  # work around the floating point error
    p0 = np.trace(zero)
    p1 = np.trace(one)
    assert ((p0 + p1 > 1 - err) and (p0 + p1 < 1 + err))

    prob = np.random.random()
    if prob <= p0:
        return zero / p0, 0     # normalise matrix
    else:
        return one / p1, 1


def measureOperator(nQbits, target, measurement):  # calculates the measurement operator and its transpose
    measurement = [measurement]
    mBra = np.identity(1)
    mKet = np.identity(1)

    for i in range(0, nQbits):
        if (i + 1) != target:
            mBra = np.kron(mBra, np.identity(2))
            mKet = np.kron(mKet, np.identity(2))

        else:
            mBra = np.kron(mBra, measurement)
            mKet = np.kron(mKet, np.transpose(measurement))

    return mBra, mKet


def extractState(chosenM):  # determines the state vector from a density matrix
    stateVec = []
    for i in range(0, len(chosenM)):
        negative = 0
        for j in range(len(chosenM[i])):

            if i == j:
                elem = np.sqrt(chosenM[i][j])
                if negative % 2 == 1:
                    elem = -elem
                stateVec.append(elem)
                break

            if (chosenM[i][j] < 0) or (chosenM[j][i] < 0):
                negative += 1
    return stateVec


def measure(stateM, target):  # Returns a reduced circuit after the target qubit is measured
    densityM = density(stateM)
    dim = np.shape(densityM)

    zeroBra, zeroKet = measureOperator(int(math.log2(dim[0])), target, ZERO_VECTOR)
    oneBra, oneKet = measureOperator(int(math.log2(dim[0])), target, ONE_VECTOR)

    matrixZero = np.matmul(zeroBra, np.matmul(densityM, zeroKet))
    matrixOne = np.matmul(oneBra, np.matmul(densityM, oneKet))

    chosenM, choice = measureChoose(matrixZero, matrixOne)

    # return the trace of chosenM
    x = extractState(chosenM)
    return x, choice


def density(stateVec):  # creates density matrix
    return np.outer(stateVec, stateVec)
