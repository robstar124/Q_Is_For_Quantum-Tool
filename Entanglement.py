import numpy as np

import gates
import gates as gs


class Entanglement:
    def __init__(self, rounds, classic=False):
        self.roundsLeft = rounds
        self.roundsWon = 0
        self.hasLost = False
        self.classic = classic
        self.guess1 = True  # represents saying "black"
        self.guess2 = True
        self.currentState = self.entangle()
        self.ballsRead = [False, False]
        return

    def entangle(self):
        initState = gs.state_vector([0, 0, 0])
        hadamard = gs.hadamard(3, [1, 2])

        ccnot = gs.Teffoli(3, 1, 2, 3)

        circuit = np.matmul(hadamard, initState)
        circuit = np.matmul(ccnot, circuit)

        entangledCirc, choice = gs.measure(circuit, 3)
        while choice != 0:
            entangledCirc, choice = gs.measure(circuit, 3)

        return entangledCirc

    def readBall(self, target):
        assert (not self.ballsRead[target - 1])  # If the ball has already been read then we shouldn't be here
        #TODO need to change read currentState but account for whether Alice has already changed it (if this is bob)
        return

    def peteReadBall(self, target):
        assert (not self.ballsRead[target - 1])  # If the ball has already been read then we shouldn't be here

        cState = self.currentState
        h = gs.hadamard(2, [target])
        cState = np.matmul(h, cState)

        cState, choice = gs.measure(cState, target)
        self.currentState = cState
        self.ballsRead[target - 1] = True
        return choice

    def runRound(self):
        if not self.classic:
            self.entangle()

    def runGame(self):
        while (self.roundsLeft > 0) and (not self.hasLost):
            self.runRound()
            self.roundsLeft -= 1

    def coinFlip(self):
        alice = np.random.choice([True, False])
        bob = np.random.choice([True, False])
        return alice, bob

    def setGuesses(self, guessOne, guessTwo):
        self.guess1 = guessOne
        self.guess2 = guessTwo

    def setMode(self, isClassic):
        self.classic = isClassic

    def endRound(self):
        self.currentState = self.entangle()
        return


def main():
    a = Entanglement(10)
    while (a.roundsLeft > 0) and (not a.hasLost):
        coinA, coinB = a.coinFlip()
        g1 = input("Alice, the coin was " + str(coinA) + " enter your guess")
        g2 = input("Bob, the coin was " + str(coinB) + " enter your guess")

        a.setGuesses(g1, g2)
        a.endRound()


main()
