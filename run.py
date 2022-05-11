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

    