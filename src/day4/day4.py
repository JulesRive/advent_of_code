# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:52:25 2024

@author: jrive
"""

def tryDirection(row, column, board, word, direction):
    directionX = direction[0]
    directionY = direction[1]
    for wordIndex in range(1,len(word)): # We already have the first letter
        column += directionX
        row += directionY
        if column < 0 or column >= len(board[0]):
            return False
        if row < 0 or row >= len(board):
            return False
        try:
            if not board[row][column] == word[wordIndex]:
                return False
        except:
             print(f'Issue at row {row} column {column}')
             return False
    return True

def checkForWord(row, column, board, word):
    total = 0
    directions = [[-1,0], [1,0], [0,-1], [0,1], [-1,-1], [-1,1], [1,-1], [1,1]]
    for direction in directions:
        if tryDirection(row, column, board, word, direction):
            total += 1      
    return total   

def checkForX(row, column, board, word):
    # Check boundaries
    if row == 0 or row == len(board)-1:
        return False
    if column == 0 or column == len(board[0])-1:
        return False
    # Make a copy of the word, and check first diagonal
    wordCopy = word.copy()
    upperLeft = board[row-1][column-1]
    lowerRight = board[row+1][column+1]
    if not upperLeft in wordCopy:
        return False
    wordCopy.remove(upperLeft)
    if not lowerRight in wordCopy:
        return False
    
    # Check second diagonal
    wordCopy = word.copy()
    upperRight = board[row-1][column+1]
    lowerLeft = board[row+1][column-1]
    if not upperRight in wordCopy:
        return False
    wordCopy.remove(upperRight)
    if not lowerLeft in wordCopy:
        return False
    return True

board = []
f = open("input.txt", "r")
for line in f:
    crtLine = []
    for letter in line:
        crtLine.append(letter)
    board.append(crtLine)

word = ["X", "M", "A", "S"]
word2 = ["M", "S"]
total1 = 0
total2 = 0
# Go through each line, for each X, look in every direction for XMAS.
for row in range(len(board)):
    for column in range(len(board[0])-1): # Don't take the endline character
        # if board[row][column] == word[0]:
        #     total1 += checkForWord(row, column, board, word)
        if board[row][column] == 'A':
            if checkForX(row, column, board, word2):
                total2 += 1
    
print(word)