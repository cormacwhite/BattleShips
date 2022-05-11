import numpy as np
from Constants import N, numShips, computer


class Player:
    def __init__(self, name="Computer"):
        self.name = name
        self.shipsDestroyed = 0
        self.__board__ = self.getRandomBoard()
        self.moves = []

    def getRandomBoard(self):
        coordinates = []

        for i in range(numShips):
            coordinates.append(list(np.random.randint(0, N, 2)))

        return coordinates

    def getBoard(self):
        return self.__board__
