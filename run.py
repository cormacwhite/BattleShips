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


