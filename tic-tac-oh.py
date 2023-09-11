#tictactoe game that i'm copying from a book, hope it works out well. 

import random

def drawBoard(board):
        #This function prints out the board that it was passed.

        #"board" is actually a list of 10 strings representing the board (ignore index 0).
    print('   |  ' + '   |  ')
    print(board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('-+-+-' * 3)
    print(board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('   |  ' + '   |  ')
    print('-+-+-' * 3)
    print(board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('   |  ' + '   |  ')

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item and the computer's letter as the second.
    
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print ('Do you want to be X or O?')
        letter = input().upper()
    
    # The first element in the list is the player's letter; the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    #Randomly choose which player goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
    
def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # using "bo" instead of board and "le" instead of letter soless typytype cause it's bout to get wonky.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def getBoardCopy(board):
    #make a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Return True if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    #let the polpayer enter their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('what is your next move? (1-9)')
        move = input()
    return int (move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #First, check if we can win in the next move.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
            
  # Check if the player could win on their next move and block them.          
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    
    #goign for the center spot, its like 11pm and im tired of writing code

    if isSpaceFree(board, 5):
        return 5

    #try and take the flanks
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    #returns true if every space has been taken and stuff else, its false

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True
    
print('WELCOME TO MY TIC-TAC-TOE GAME!! =p')

while True:
    #Reset the board.
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('the ' + turn + ' will go first.' )
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            
        #this is the players turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('you won by sheer luck')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Could\'nt even beat the computer?')
                    break
                else:
                    turn = 'Computer'    

        else:
            # Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Couldn\'t even beat the computer?')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break  