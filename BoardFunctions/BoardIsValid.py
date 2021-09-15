# checks if the placement is valid
# called in SolveBoard
def IsValid(board, row, col, num):
    # Row and col check
    for x in range(9):
        if num == board[row][x] or num == board[x][col]:
            return False
    
    # check the sector
    sr = row % 3    # either 0,1,2 -> the position in the sect (0 indexed)
    sc = col % 3
    for x in range(3):
        for y in range(3):
            if num == board[row - sr + x][col - sc + y]:
                return False
    return True

# checks if the imported board is valid
def ImportIsValid(board):
    entries = 0
    for row in range(9):
        for col in range(9):
            boardSect = [[], [], []]
            sectRow = row - (row % 3)
            sectCol = col - (col % 3)
            boardSect[0] = board[sectRow][sectCol:sectCol+3]
            boardSect[1] = board[sectRow+1][sectCol:sectCol+3]
            boardSect[2] = board[sectRow+2][sectCol:sectCol+3]

            boardCol = [board[rowTemp][col] for rowTemp, listTemp in enumerate(board)]
            if board[row][col] != 0:
                entries += 1

                # check if the row is valid
                for newRow in range(9):
                    if (board[row][col] == boardCol[newRow]) and (row != newRow):
                        return False

                # check if the col is valid
                for newCol in range(9):
                    if (board[row][col] == board[row][newCol]) and (col != newCol):
                        # print("row fails")
                        return False

                # check if the board sector is valid
                for newRow in range(3):
                    for newCol in range(3):
                        if (board[row][col] == boardSect[newRow][newCol]) and ((row % 3) != newRow) and ((col % 3) != newCol):
                            # print("sector fails")
                            return False
    # to minimize chance that user imports an incorret board
    # if entries < 20:
    #     # print("entry fails")
    #     return False

    return True