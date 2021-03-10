import random


class Field:
    def __init__(self):
        self.cells = {(i, j): 0 for i in range(1, 5) for j in range(1, 5)}
        self.winFlag = False
        self.generateNew()

    def get(self):
        return self.cells

    def generateNew(self):
        # 16-ая клетка - несуществующая
        cellPermutations = [i for i in range(1, 17)]
        random.shuffle(cellPermutations)
        self.cells = dict(zip(self.cells.keys(), cellPermutations))
        self.winFlag = False

    def checkWin(self):
        labels = [self.cells[(i, j)] for i in range(1, 5) for j in range(1, 5)]
        self.winFlag = (labels == [i for i in range(1, 17)])

    def isWin(self):
        return self.winFlag

    def move(self, coord):
        '''Передвигаем соседнюю пустышку, если есть'''
        x, y = coord
        for (dx, dy) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            neigh_coord = (x + dx, y + dy)
            if neigh_coord in self.cells and self.cells[neigh_coord] == 16:
                self.cells[coord], self.cells[neigh_coord] = \
                    self.cells[neigh_coord], self.cells[coord]
                self.checkWin()
                break
