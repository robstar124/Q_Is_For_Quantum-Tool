import numpy as np

import gates
import gates as gt


class Entanglement:
    def __init__(self, rounds, classic=False):
        self.roundsLeft = rounds
        self.roundsWon = 0
        self.hasLost = False
        self.classic = classic
        self.guess1 = True  # represents saying "black"
        self.guess2 = True

        self.runGame()
        return

    def probabilities(self):
        pass

    def measure(self, state, target):

        pass

    def entangle(self):
        initState = gt.state_vector([0, 0, 0])
        hadamard = gt.hadamard(3, [1, 2])
        ccnot = gt.Teffoli(3, 1, 2, 3)

        circuit = np.matmul(hadamard, initState)
        circuit = np.matmul(ccnot, circuit)
        circuit = gates.density(circuit)


        print(circuit)

        pass

    def runRound(self):
        if not self.classic:
            self.entangle()

    def runGame(self):
        while (self.roundsLeft > 0) and (not self.hasLost):
            self.runRound()
            self.roundsLeft -= 1

    def setGuesses(self, guessOne, guessTwo):
        self.guess1 = guessOne
        self.guess2 = guessTwo

    def setMode(self, isClassic):
        self.classic = isClassic


def main():
    Entanglement(1)


main()
