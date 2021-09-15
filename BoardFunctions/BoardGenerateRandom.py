import random

# Generates a random board from the solution board passed to it
# returns the random board
def BoardGenerateRandom(board):
    difficulty = 10 # this adjusts difficulty
    for iteration in range(difficulty):  #
        for row in range(9):
            for col in range(9):
               if (row + 1) % 3 == 0 and (col + 1) % 3 == 0:
                   randRow = random.randint(row-2,row)
                   randCol = random.randint(col-2,col)
                   board[randRow][randCol] = 0
    return board