"""
CSE 210: Tic Tac Toe
Author: Joshua Beale
"""

class board():
    def __init__(self):
        defaults = [1,2,3,4,5,6,7,8,9]
        self.winner = None

        self.drawBoard(defaults);

    def drawBoard(self, values):
        print("\n*---*---*---*")
        print(f"| {values[0]} | {values[1]} | {values[2]} |")
        print("*---*---*---*")
        print(f"| {values[3]} | {values[4]} | {values[5]} |")
        print("*---*---*---*")
        print(f"| {values[6]} | {values[7]} | {values[8]} |")
        print("*---*---*---*\n\n")

    

def updateBoard(game, player, values):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    while not isinstance(values[square-1], int):
        square = int(input(f"That square has already been marked by {values[square-1]}. Please choose another Square (1-9): ")) 
    values[square-1] = player
    game.drawBoard(values)
    game.winner = checkWinner(values, player)

    if player == "X":
        return("O")
    elif player == "O":
        return("X")

def checkWinner(values, player):
    if (values[0] == values[1] == values[2]) \
        or (values[3] == values[4] == values[5]) \
        or (values[6] == values[7] == values[8]) \
        or (values[0] == values[4] == values[8]) \
        or (values[2] == values[4] == values[6]) \
        or (values[0] == values[3] == values[6]) \
        or (values[1] == values[4] == values[7]) \
        or (values[2] == values[5] == values[8]):
    
        winner = player
    
    elif not any(isinstance(value,int) for value in values):
        winner = "Cat's Game"

    else:
        winner = None

    return(winner)
        

def newGame(games):
    player = "X"
    values = [1,2,3,4,5,6,7,8,9]
    games["Game-"+str((len(games)+1))] = board()
    allGames = list(games.keys())
    game = games[allGames[-1]]

    while game.winner == None:
        player = updateBoard(games[allGames[-1]], player, values)

    if game.winner == "Cat's Game":
        print("Cat's Game!")
    else:
        print(f'{game.winner} won this round!')

def results(games):
    Xtotal = 0
    Ototal = 0
    drawTotal = 0

    print("\nFinal Results:")
    for i, key in enumerate(games.keys(), 1):
        if games[key].winner == "X": Xtotal += 1
        elif games[key].winner == "O": Ototal += 1
        else: drawTotal += 1
        print(f"  Game {i}: {games[key].winner}")

    print()
    print(f"  Total won by X: {Xtotal}")
    print(f"  Total won by O: {Ototal}")
    print(f"  Total draws: {drawTotal}")


def main():
    games = {}
    newGame(games)
    playAgain = input("Would you like to play again? (Yes/No):  ")
    if playAgain.lower() != "yes" and playAgain.lower() != "no":
        input("Invalid Input. \nWould you like to play again? (Yes/No):  ")


    while playAgain.lower() == "yes":
        newGame(games)
        playAgain = input("Would you like to play again? (Yes/No):  ")
        if playAgain.lower() != "yes" and playAgain.lower() != "no":
            input("Invalid Input.\nWould you like to play again? (Yes/No):  ")

    results(games)

    print("\nThank you for playing!")

main()