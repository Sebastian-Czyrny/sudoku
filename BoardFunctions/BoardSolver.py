from . import BoardCheckContinue
from . import BoardIsValid


# Calling this method solves the board
def BoardSolver(board):
    boardCheckContinue, row, col = BoardCheckContinue.BoardCheckContinue(board)

    # base case: no more spots to fill
    if not boardCheckContinue:
        return True

    # every other case: unassigned spots
    for num in range(1, 10):
        if BoardIsValid.IsValid(board, row, col, num):
            board[row][col] = num
            if BoardSolver(board):
                return True
        # BoardSolver failed, unassign and try again
        board[row][col] = 0

    return False

        

