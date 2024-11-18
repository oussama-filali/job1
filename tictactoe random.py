import random

def sum(a, b, c ):
    return a + b + c

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1

def computerMove(xState, zState):
    available_moves = [i for i in range(9) if xState[i] == 0 and zState[i] == 0]
    
    # Check if computer can win in the next move
    for move in available_moves:
        zState[move] = 1
        if checkWin(xState, zState) == 0:
            zState[move] = 0
            return move
        zState[move] = 0
    
    # Check if player can win in the next move and block it
    for move in available_moves:
        xState[move] = 1
        if checkWin(xState, zState) == 1:
            xState[move] = 0
            return move
        xState[move] = 0
    
    # Choose center if available
    if 4 in available_moves:
        return 4
    
    # Choose a corner
    corners = [0, 2, 6, 8]
    available_corners = [move for move in corners if move in available_moves]
    if available_corners:
        return random.choice(available_corners)
    
    # Choose a random move
    return random.choice(available_moves) if available_moves else None

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X (player) and 0 for O (computer)
    print("Welcome to Tic Tac Toe")
    print("You are player: X")
    print("The computer is player: O")
    while(True):
        printBoard(xState, zState)
        if(turn == 1):
            print("Your turn (X)")
            while True:
                try:
                    value = int(input("Please chose a value (0-8): "))
                    if 0 <= value <= 8 and xState[value] == 0 and zState[value] == 0:
                        xState[value] = 1
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 8.")
        else:
            print("Computer's turn (O)")
            value = computerMove(xState, zState)
            if value is not None:
                zState[value] = 1
                print(f"Computer  has chosen :{value}")
            else:
                print("No more moves available. It's a draw!")
                break
        cwin = checkWin(xState, zState)
        if(cwin != -1):
            printBoard(xState, zState)
            print("Match over")
            break
        if all(xState[i] == 1 or zState[i] == 1 for i in range(9)):
            printBoard(xState, zState)
            print("It's a draw!")
            break
        turn = 1 - turn
        
       