from Player import Player, np
from Constants import N, numShips, computer


def divider():
    print("  ----------------------------------------    ")


def welcomeScreen():
    print("\n\n")
    divider()
    print("     Welcome to ULTIMATE BATTLESHIP!!    ")
    print(f"     Board Size: {N}. Number of Ships: {numShips}.    ")
    print("     Top left corner is row: 0, col: 0    ")
    divider()
    name = input('  Please enter your name:\n   ')
    divider()
    return name


def printBoard(name, coordinates):

    isComputer = False
    if name == computer:
        isComputer = True

    print(f"{name}'s Board:")
    for i in range(N):
        for j in range(N):
            if [i, j] in coordinates and not isComputer:
                print('# ', end="")
            else:
                print(". ", end="")
        print()


class GamePlay:
    def __init__(self, name):
        self.name = name
        self.computer = Player()
        self.player = Player(name)

    def inputNumber(self, name):
        number = -1

        try:
            number = int(input(f"Guess a {name}:\n"))
            if number < 0 or number > numShips:
                print(f"\nValues must be between 0 and {numShips}!")
                return -1
            else:
                return number
        except:
            print("\nYou must enter a number!")
            return -1

    def inputRowCol(self):
        row = col = -1

        print(self.computer.getBoard())
        print(self.player.getBoard())

        while True:
            row = self.inputNumber('row')
            if row == -1:
                continue

            col = self.inputNumber('column')
            if col != -1:
                break
            else:
                continue

        return [row, col]

    def play(self):
        printBoard(self.player.name, self.player.getBoard())
        printBoard(self.computer.name, self.computer.getBoard())

        while self.computer.shipsDestroyed != numShips or self.player.shipsDestroyed != numShips:
            divider()

            coordinates = []
            while True:
                coordinates = self.inputRowCol()
                if coordinates in self.player.moves:
                    print(
                        '\nYou cannot guess the same coordinates more than once.')
                    continue
                else:
                    break

            print(f'Player Guessed: ({coordinates[0]},{coordinates[1]})')
            self.player.moves.append(coordinates)

            if coordinates in self.computer.getBoard():
                self.player.shipsDestroyed += 1
                print('Congrats! You destroyed the ship!')
            else:
                print('Player missed this time.')

            