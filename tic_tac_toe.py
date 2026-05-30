#initiation, blank board user symbol, turn status 
from random import*
from time import sleep
print("Welcome to Naughts and Crosses! The grid is numbered 1-9, starting from the top left corner and going across each row. Naughts goes first, so if you choose naughts you will be playing first. If you choose crosses, the computer will play first. Good luck!")
board = ['| |', '| |','| |', '| |', '| |', '| |', '| |', '| |', '| |']
user = input("Naughts or Crosses? Naughts is first  ").lower()
turnStatus = False
userSymbol = ''
while True: #does user go first
    if user == "naughts":
        turnStatus = True
        userSymbol = '|O|'
        break
    elif user == "crosses":
        turnStatus = False
        userSymbol = '|X|'
        break
    else:
        user = input("Invalid input, Try again")
if userSymbol == '|X|':
    computerSymbol = '|O|'
if userSymbol == '|O|':
    computerSymbol = '|X|'
            # Display board HERE
for index, square in enumerate(board):
    print(square, end=' ')
    if (index + 1) % 3 == 0:
        print()
def gameTurn(userSymbol):#function game loop
    while True:
        try:
            userLocation = int(input("What grid? 1-9, no repeats: "))
        except ValueError:
            print("Invalid input, make sure it's a number 1-9")
            continue  # go back to top of while loop
        
        # Range check
        if userLocation > 9 or userLocation < 1:
            print("Invalid input, make sure it's between 1-9")
            continue
        
        # Repeat check
        if board[userLocation - 1] != '| |':
            print("That grid is already taken, try again")
            continue
        else:
            break  # valid input, exit loop    
    board[userLocation - 1] = userSymbol
    for index, square in enumerate(board):
        print(square, end=' ')
        if (index + 1) % 3 == 0:
            print()
def computerTurn(computerSymbol):#computer turn
    sleep(0.5)
    print("Computer's turn")
    sleep(0.5)
    print("Computer is thinking...")
    sleep(1)
    while True:
        computerLocation = randint(0,8)
        if board[computerLocation] == '| |':
            board[computerLocation] = computerSymbol
            break
        elif '| |' not in board:  # board is full, stop trying
            break
    for index, square in enumerate(board):
        print(square, end=' ')
        if (index + 1) % 3 == 0:
            print()
def checkboard():
    if '| |' not in board:  # board is full, stop trying
        print("The board is full,checking for victory...")
        sleep(1)
        victorycheck()
def victorycheck():
    WINNING_COMBOS = [
    [0, 1, 2],  # top row
    [3, 4, 5],  # middle row
    [6, 7, 8],  # bottom row
    [0, 3, 6],  # left column
    [1, 4, 7],  # middle column
    [2, 5, 8],  # right column
    [0, 4, 8],  # diagonal \
    [2, 4, 6],  # diagonal /
    ]
    #FOR VICTORY
    for combo in WINNING_COMBOS:
        global game_over
        if all(board[i] == userSymbol for i in combo):
            print(f"{userSymbol.strip('|')} wins!")
            print("Congratulations!")
            game_over = True
            return
        elif all(board[i] == computerSymbol for i in combo):
            print(f"{computerSymbol.strip('|')} wins!")
            print("Better luck next time!")
            game_over = True
            return
        elif '| |' not in board:  # board is full, stop trying
            print("It's a draw!")
            game_over = True
            return
def main():
    global game_over
    global turnStatus
    game_over = False
    checkboard()
    while not game_over:
        if turnStatus:
            gameTurn(userSymbol)
            victorycheck()
            turnStatus = False
        else:
            computerTurn(computerSymbol)
            victorycheck()
            turnStatus = True
main()
