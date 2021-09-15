import random

# Generates a full, solution board
# returns the full, solution board
def BoardGenerateFull():
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]


    fails = 0
    row = 0

    while row < 9:
        boardRow = []
        boardSect = [[], [], []]
        xList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for col in range(9):
            sectRow = row - (row % 3)
            sectCol = col - (col % 3)
            boardSect[0] = board[sectRow][sectCol:sectCol+3]
            boardSect[1] = board[sectRow+1][sectCol:sectCol+3]
            boardSect[2] = board[sectRow+2][sectCol:sectCol+3]

            boardCol = [board[rowTemp][col] for rowTemp, listTemp in enumerate(board)]
            fails = 0

            while True:
                x = random.choice(xList)

                if x not in boardRow and x not in boardCol and not any(x in sublist for sublist in boardSect):
                    xList.remove(x)
                    boardRow.append(x)
                    break

                else:
                    fails += 1
                    if fails > 10:
                        row -= 1
                        board[row] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        break  # breaks while True: loop

            if fails > 10:
                break # breaks for j in range...: loop


        if fails < 10:
            board[row] = boardRow
            row += 1

    # while row < 9 loop ends here
    return board