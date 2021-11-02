import sys

import numpy as np
import gates


# 4th bit is the target
# 5th bit is the dummy
class Archimedes:
    def __init__(self, initState, locations, fake=False, classic=False):
        self.matrix = initState
        if fake:
            self.locations = ["11110", "11110", "11110", "11110"]
        else:
            self.locations = locations  # "real" locations for the gold bars

        if classic:
            self.buildCircuit()
        else:
            self.matrix = np.matmul(gates.hadamard(5, [1, 2, 3, 4]), self.matrix)  # initial 4 hadamards
            self.buildCircuit()
            self.matrix = np.matmul(gates.hadamard(5, [1, 2, 3]), self.matrix)

        return

    def buildCircuit(
            self):  # builds the circuit as one major transformation matrix before applying it to the initial state
        circNots = [0] * 3  # counts the amount of X gates applied to specific qubits so far
        for i in self.locations:
            targets = []  # target for the X gates
            for j in range(0, len(i) - 2):
                if i[j] == "0":
                    if circNots[j] % 2 == 0:
                        targets.append(j + 1)
                        circNots[j] += 1
                    elif circNots[j] % 2 == 1:
                        continue
                else:
                    if circNots[j] % 2 == 0:
                        continue
                    elif circNots[j] % 2 == 1:
                        targets.append(j + 1)
                        circNots[j] += 1

            xGate = gates.NOT(5, targets)
            cccnot = gates.CCCNOT(1, 2, 3, 4, 5)

            self.matrix = np.matmul(cccnot, np.matmul(xGate, self.matrix))
        return self.matrix

    def readOutput(self):   # Reads every qubit to give us a determined output
        state = []
        mat = self.matrix
        for i in range(0, 5):
            mat, ch = gates.measure(mat, 1)
            state.append(ch)
        return state

def main():
    initState = gates.state_vector([0, 0, 0, 1, 0])
    locations = ["00110", "01010", "10110", "11110"]
    Archimedes(initState, locations)


main()
