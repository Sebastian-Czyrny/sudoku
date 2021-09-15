from .imports import *
from . import TextDisplays



def boardDisplay(screen, board, color, completeBoard=None, solving=False):
    # creates the static numbers
    font = pg.font.SysFont('bahnschrift', GRID_BOX-10)
    strBoard = [list((map(str,i))) for i in board]
    
    if not solving:
        for i in range(9):
            for j in range(9):
                if strBoard[j][i] != '0':
                    pg.draw.rect(screen, color, pg.Rect((GRID_BOX * i, GRID_BOX * j, GRID_BOX, GRID_BOX)))
                    TextDisplays.textDisp(screen, strBoard[j][i], black, GRID_BOX * i + (GRID_BOX/2), GRID_BOX * j + (GRID_BOX/2), 40, colorRect=color, colorRectEx=True )


    elif solving:
        strCompleteBoard = [list((map(str,i))) for i in completeBoard]
        
        for i in range(9):
            for j in range(9):
                if board[j][i] == 0:
                    pg.draw.rect(screen, color, pg.Rect((GRID_BOX * i, GRID_BOX * j, GRID_BOX, GRID_BOX)))
                    TextDisplays.textDisp(screen, strCompleteBoard[j][i], red, GRID_BOX * i + (GRID_BOX/2), GRID_BOX * j + (GRID_BOX/2), 40)
