import numpy as np
import gates


class Archimedes:
    def __init__(self):
        self.locations = ["00110", "01010", "10110", "11110"]
        self.circuit()
        pass


    def circuit(self):
        matrix = np.identity(32)
        circNots = [0]*3

        for i in self.locations:
            targets = []
            for j in range(0, len(i) - 2):
                if i[j] == "0":
                    if circNots[j] % 2 == 0:
                        targets.append(j)
                        circNots[j] += 1
                    elif circNots[j] % 2 == 1:
                        continue
                else:
                    if circNots[j] % 2 == 0:
                        continue
                    elif circNots[j] % 2 == 1:
                        targets.append(j)
                        circNots[j] += 1

            xGate = gates.NOT(5, targets)
            cccnot = gates.CCCNOT(1, 2, 3, 4, 5)

            matrix = np.matmul(cccnot, np.matmul(xGate, matrix))

            print(matrix)







def main():
    Archimedes()

main()