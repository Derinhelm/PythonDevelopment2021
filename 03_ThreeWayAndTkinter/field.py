import random

class Field:
    def __init__(self):
        self.cells = {(i, j):0 for i in range(1, 5) for j in range(1, 5)}
        self.generateNew()

    def get(self):
        return self.cells

    def generateNew(self):
        # 16-ая клетка - несуществующая
        cellPermutations = [i for i in range(1, 17)]
        random.shuffle(cellPermutations)
        self.cells = dict(zip(self.cells.keys(), cellPermutations))

    def isWin(self):
        return self.cells[(4, 4)] == 16