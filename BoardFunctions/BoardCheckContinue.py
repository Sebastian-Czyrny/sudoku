# Check if the board solver needs to continue solving the board
# returns true if yes, and the row and col
# called in SolveBoard
def BoardCheckContinue(board):
    row = 0
    col = 0
    for x in range(9):
        for y in range(9):
            if (board[x][y] == 0):
                row = x
                col = y 
                return True, row, col
    return False, row, col