#initiation, blank board user symbol, turn status 
from random import*
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

def gameTurn(userSymbol):#function game loop
    global user
    global turnStatus
    if turnStatus == True:
        # Display board HERE
        for index, square in enumerate(board):
            print(square, end=' ')
            if (index + 1) % 3 == 0:
                print()
        for index, square in enumerate(board):
            if square != '| |':
                print('repeat:(')
        while True:
            try:
                userLocation = int(input("What grid? 1-9, no repeats"))
                break
            except ValueError:
                userLocation = input("Invalid input, make sure is number 1-9")

        while True:
            if userLocation > 9 or userLocation < 1:
                userLocation = input("Invalid input, make sure is number inbetween 1-9")
            else:
                break
        board[userLocation - 1] = userSymbol
    else:
        #computer turn
        computerLocation = 0
        
        
            
            
        turnStatus = True
    gameTurn(userSymbol)
  
gameTurn(userSymbol) 
