#This is a game from the no starch book Invent your own computer games with python
#Hopefully I start understanding what i'm actually typing and stuff as i go through it

import random
import sys
import math

#First gonna creat a board you'll use whenever you play.
def getNewBoard():
    board = []
    for x in range(60): #the main list is a list of 60 lists this will be the x axis on the board where it goes 0-9 5 times
        board.append([])
        for y in range(15): #each list is the main list has 15 single-character strings this will be the y-axis on the board where it goes 0-14
            if random.randint(0, 1) == 0: #this if/else statement will help draw the board as an ocean.
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    #drawing what the board lookslike
    tensDigitsLine =  ' ' # Initial space for the numbers down the left side fo the board
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    #printing all 15 rows like it was shown above:

